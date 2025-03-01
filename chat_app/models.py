from django.db import models


class ChatBotResponse(models.Model):
    RESPONSE_STYLES = [
        ('CONCISE', 'Resumida'),
        ('NORMAL', 'Normal'),
        ('EXPLANATORY', 'Extendida')
    ]

    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='gemini_user')
    title = models.CharField(max_length=300, null=False)
    response_file = models.URLField(null=False)
    response_style = models.CharField(
        max_length=20,
        choices=RESPONSE_STYLES,
        default='NORMAL',
        verbose_name='Estilo de respuesta'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
