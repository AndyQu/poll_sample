from django.contrib import admin
from polls.models import *

class QuestionAdminA(admin.ModelAdmin):
    fields = ['pub_date', 'question_text']

class QuestionAdminB(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse'] }),
        ('Choices',          {'fields': ['choice_set']})
    ]
admin.site.register(Question, QuestionAdminB)
admin.site.register(Choice)