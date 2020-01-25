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

class NumOfParticipant(models.Model):
    name_num = models.CharField(max_length=32)
    description_num = models.TextField(null=True, max_length=1000)

    def __str__(self):
        return (f'(__str__)NumOfParticipant: {self.name_num}')

class Author(models.Model):
    name_a = models.CharField(max_length=32)
    email_a = models.CharField(max_length=50)
    webpage_a = models.CharField(max_length=50)

    def __str__(self):
        return (f'(__str__)Author: {self.name_a}')


class Subject(models.Model):
    subject_name_s = models.CharField(max_length=50)
    bot_name_s = models.CharField(max_length=50)
    description_s = models.TextField(max_length=1000)
    is_active_s = models.BooleanField(default=False)
    author = models.ForeignKey(Author, null=True, on_delete=models.CASCADE)
    statistic_s = models.ForeignKey(NumOfParticipant, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return (f'Subject: {self.subject_name_s},\nBot: {self.bot_name_s}')