from django.contrib import admin

from .models import Survey, Question, Option, Submission, Answer, DefaultQuestion, AgeRange, Gender, Industry

admin.site.register(Survey)
admin.site.register(Question)
admin.site.register(DefaultQuestion)
admin.site.register(AgeRange)
admin.site.register(Gender)
admin.site.register(Industry)
admin.site.register(Option)
admin.site.register(Submission)
admin.site.register(Answer)
