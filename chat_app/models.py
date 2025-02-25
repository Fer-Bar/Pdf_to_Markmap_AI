from django.db import models


class ChatBot(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='gemini_user')
    title = models.CharField(max_length=300, null=False)
    response_file = models.URLField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
