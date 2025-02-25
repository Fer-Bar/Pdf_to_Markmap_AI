from django import forms


class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = [single_file_clean(data, initial)]
        return result


class PDFUploadForm(forms.Form):
    title = forms.CharField(label="Title", max_length=100)
    pdfs = MultipleFileField(label="PDFs", help_text="Select multiple PDF files to upload.")

    def clean_pdfs(self):
        files = self.files.getlist('pdfs')
        for file in files:
            if file.size > 20 * 1024 * 1024:  # 20MB
                raise forms.ValidationError(f"El archivo {file.name} supera los 20MB.")
        return files
