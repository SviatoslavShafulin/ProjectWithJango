from django.db import models

class Post(models.Model):
    # Оголошення полів моделі
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
