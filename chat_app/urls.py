from django.urls import path
from chat_app.views import get_markmap_from_pdf, get_all_chat_responses

app_name = "chat_app"

urlpatterns = [
    path("chat/", get_markmap_from_pdf, name="upload_pdfs"),
    path("", get_all_chat_responses, name="chat_responses"),
]
