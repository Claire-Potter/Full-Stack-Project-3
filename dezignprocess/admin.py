from django.contrib import admin
from .models import Step
from .models import KnowledgeResource
from .models import Template

admin.site.register(Step)
admin.site.register(KnowledgeResource)
admin.site.register(Template)
