from firebase_admin import storage


def upload_html_to_firebase(html_content, filename):
    bucket = storage.bucket()
    blob = bucket.blob(filename)
    blob.upload_from_string(html_content, content_type="text/html")
    blob.make_public()
    return blob.public_url
