# PDF to Markmap

A Django web application that transforms PDF documents into interactive mind maps using Google's Gemini AI. Upload your PDFs and get instant visual representations of your documents in an easy-to-understand mind map format.

## Features

- 📄 Multiple PDF file upload support
- 🤖 AI-powered content analysis using Google Gemini
- 🗺️ Automatic mind map generation
- 🎨 Three response styles:
  - Normal: Balanced content presentation
  - Concise: Streamlined key points
  - Explanatory: Detailed breakdown
- 🔥 Firebase storage integration
- 📱 Responsive Bootstrap 5 interface
- 📊 Response history tracking

## Tech Stack

- Python 3.10
- Django
- Google Gemini AI
- Firebase Storage
- Bootstrap 5

## Setup

1. Create a `.env` file with:
```env
GOOGLE_API_KEY=your_gemini_api_key
FIREBASE_BUCKET_NAME=your_firebase_bucket
FIREBASE_CREDENTIALS=path_to_firebase_credentials.json
SECRET_KEY=your_django_secret_key
DEBUG=True/False
```
1. Install dependencies:
```bash
pip install -r requirements.txt
```
2. Run migrations:
```bash
python manage.py migrate
```
3. Start the server:
```bash
python manage.py runserver
```
