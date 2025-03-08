import io
from google import genai
from google.genai import types
from pdf_to_markmap.config import get_settings


class GeminiChatBot:
    def __init__(self, model_name: str = "models/gemini-2.0-flash-thinking-exp-01-21", system_instruction: str = None):
        settings = get_settings()
        if not settings or not settings.GOOGLE_API_KEY:
            raise ValueError("API key for Gemini is not set in environment variables.")

        self.client = genai.Client(api_key=settings.GOOGLE_API_KEY)
        self.model_name = model_name
        self.system_instruction = system_instruction
        self.uploaded_files = []

    def upload_file(self, file_data: io.BytesIO, mime_type: str = 'application/pdf'):
        """
        Sube un archivo a Gemini y lo almacena en `uploaded_files`.

        :param file_data: Un objeto io.BytesIO que contenga el contenido del archivo.
        :param mime_type: Tipo MIME del archivo, por defecto 'application/pdf'.
        :return: La referencia del archivo subido.
        """
        uploaded_file = self.client.files.upload(
            file=file_data,
            config={'mime_type': mime_type}
        )
        self.uploaded_files.append(uploaded_file)
        return uploaded_file

    def generate_response(self, message: str):
        """
        Genera una respuesta incluyendo, si existen, los archivos subidos.
        Los contenidos se conforman de los archivos y el mensaje.

        :param message: Prompt o mensaje a enviar a la AI.
        :return: Texto de respuesta generado.
        """
        if self.uploaded_files:
            contents = self.uploaded_files + [message]
        else:
            contents = [message]
        response = self.client.models.generate_content(
            model=self.model_name,
            contents=contents,
            config=types.GenerateContentConfig(
                system_instruction=self.system_instruction,
                temperature=0,
            ),
        )
        return response.text


custom_instructions: dict[str, str] = {
    "prompt": "Analiza el texto proporcionado y genera un mapa mental en formato Markmap.",
    "system_instruction": """Eres un asistente que convierte contenido de PDF en mapas mentales.
         Analiza el texto proporcionado y genera un mapa mental en formato Markmap. 
         No incluyas saludos, despedidas ni explicaciones adicionales; proporciona únicamente el contenido en Markmap.
         """,
}
