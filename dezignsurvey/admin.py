from django.contrib import admin
from .models import Survey, Gender, AgeRange

admin.site.register(Survey)
admin.site.register(Gender)
admin.site.register(AgeRange)
