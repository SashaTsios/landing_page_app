from django.db import models

# Create your models here.
class Feedback_new(models.Model):
    name_m = models.CharField(max_length=32)
    text_m = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created_at',) # сортуємо в  зворотньому порядку. найновіше буде зверху

    def __str__(self):
        return (f'{self.created_at}: {self.name_m} + {self.text_m} and is {self.is_active}')


class Subject(models.Model):
    subject_name_s = models.CharField(max_length=50)
    bot_name_s = models.CharField(max_length=50)
    description_s = models.TextField(max_length=1000)
    is_active_s = models.BooleanField(default=False)