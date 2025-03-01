from firebase_admin import storage


def upload_file_to_firebase(file_content, filename: str, content_type: str | None = None):
    try:
        bucket = storage.bucket()
        blob = bucket.blob(filename)
        blob.upload_from_string(file_content, content_type=content_type)
        blob.make_public()
        return blob.public_url
    except Exception as e:
        print(e)
