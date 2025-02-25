import io
from django.shortcuts import render
from chat_app.forms import PDFUploadForm
from chat_app.gemini_chatbot import GeminiChatBot


def get_markmap_from_pdf(request):
    chat_bot = GeminiChatBot(system_instruction="""Eres un asistente que convierte contenido de PDF en mapas mentales.
         Analiza el texto proporcionado y genera un mapa mental en formato Markdown compatible con Markmap. 
         No incluyas saludos, despedidas ni explicaciones adicionales; proporciona únicamente el contenido en Markdown.
         """)
    if request.method == 'POST':
        form = PDFUploadForm(request.POST, request.FILES)
        if form.is_valid():
            files = form.cleaned_data['pdfs']
            uploaded_files = []
            for f in files:
                pdf_data = io.BytesIO(f.read())
                uploaded_pdf = chat_bot.upload_file(pdf_data, mime_type='application/pdf')
                uploaded_files.append(uploaded_pdf)
            prompt = "Analiza el texto proporcionado y genera un mapa mental en formato Markdown compatible con Markmap."
            response_text = chat_bot.generate_response(prompt)
            print(response_text)
            return render(request, 'chat_app/index.html', {"form": form, "response_text": response_text})
    else:
        form = PDFUploadForm()
    return render(request, 'chat_app/index.html', {"form": form})
