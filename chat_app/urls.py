from django.urls import path
from chat_app.views import get_markmap_from_pdf

app_name = "chat_app"

urlpatterns = [
    path("", get_markmap_from_pdf, name="upload_pdfs"),
]
