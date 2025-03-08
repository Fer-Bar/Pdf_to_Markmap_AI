import io

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.template.loader import render_to_string

from chat_app.forms import PDFUploadForm
from chat_app.gemini_chatbot import GeminiChatBot, custom_instructions
from chat_app.firebase_storage import upload_file_to_firebase
from chat_app.models import ChatBotResponse


@login_required
def get_all_chat_responses(request):
    chat_responses = ChatBotResponse.objects.filter(user=request.user)
    return render(request,
                  'chat_app/all_responses.html',
                  {
                      "chat_responses": chat_responses,
                      "style_responses": ChatBotResponse.RESPONSE_STYLES
                  }
                  )


@login_required
def delete_response(request, response_id):
    response = ChatBotResponse.objects.get(id=response_id)
    response.delete()
    return redirect('chat_app:chat_responses')


@login_required
def get_markmap_from_pdf(request):
    if request.method == 'POST':
        chat_bot = GeminiChatBot(system_instruction=custom_instructions["system_instruction"])
        form = PDFUploadForm(request.POST, request.FILES)
        if form.is_valid():
            files = form.cleaned_data['pdfs']
            title = form.cleaned_data['title']
            response_style = form.cleaned_data['response_style']
            uploaded_files = []
            for f in files:
                pdf_data = io.BytesIO(f.read())
                uploaded_pdf = chat_bot.upload_file(pdf_data, mime_type='application/pdf')
                uploaded_files.append(uploaded_pdf)
            # delete files from upload file maybe after response
            response_text = chat_bot.generate_response(
                custom_instructions["prompt"] + f"Hazlo de manera {response_style}"
            )
            if response_text:
                html_content = render_to_string('chat_app/markmap_template.html', {
                    'response_text': response_text.replace("```", "")
                })
                file_uploaded_url = upload_file_to_firebase(
                    html_content,
                    f"files/{title}.html",
                    "text/html"
                )
                if file_uploaded_url:
                    _ = ChatBotResponse.objects.create(
                        title=title,
                        user=request.user,
                        response_file=file_uploaded_url,
                        response_style=response_style,
                    )
            return redirect('chat_app:chat_responses')
    else:
        form = PDFUploadForm()
    return render(request, 'chat_app/pdf_form.html', {"form": form})

