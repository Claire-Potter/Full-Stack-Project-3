from django.contrib import admin

from .models import Survey, Question, Option, Submission, Answer, DefaultQuestions, AgeRange, Gender

admin.site.register(Survey)
admin.site.register(Question)
admin.site.register(DefaultQuestions)
admin.site.register(AgeRange)
admin.site.register(Gender)
admin.site.register(Option)
admin.site.register(Submission)
admin.site.register(Answer)
