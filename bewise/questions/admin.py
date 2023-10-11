from django.contrib import admin

from questions.models import Question


@admin.register(Question)
class MenuAdmin(admin.ModelAdmin):
    list_display = ['question_id', 'question', 'answer', 'created_at', 'inserted_at']
