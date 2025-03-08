from django.urls import path
from chat_app.views import get_markmap_from_pdf, get_all_chat_responses, delete_response

app_name = "chat_app"

urlpatterns = [
    path("chat/", get_markmap_from_pdf, name="upload_pdfs"),
    path("", get_all_chat_responses, name="chat_responses"),
    path("delete_response/<int:response_id>/", delete_response, name="delete_response"),
]
