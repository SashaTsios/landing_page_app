from django.contrib import admin
from .models import Feedback_new, Subject, Author, NumOfParticipant
# Register your models here.


@admin.register(Feedback_new)
class FeedbacksAdmin(admin.ModelAdmin):
    list_display  = ("name_m", "text_m", "is_active", "created_at")
    list_editable = ("is_active",)


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display  = ("subject_name_s", "bot_name_s", "description_s", "is_active_s", "author", "statistic_s")
    list_editable = ("is_active_s", "author", "statistic_s")


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display  = ("name_a",)


@admin.register(NumOfParticipant)
class AuthorAdmin(admin.ModelAdmin):
    list_display  = ("name_num",)