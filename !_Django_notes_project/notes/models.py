from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
    title = models.CharField(max_length=200)  # Заголовок заметки
    content = models.TextField()  # Текст заметки
    created_at = models.DateTimeField(auto_now_add=True)  # Когда заметка создана
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Автор заметки

    def __str__(self):
        return self.title