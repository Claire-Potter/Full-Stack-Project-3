from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


STATUS = ((0, "Draft"), (1, "Published"))


class Steps(models.Model):
    title = models.CharField(max_length=80, unique=True)
    slug = models.SlugField(max_length=80, unique=True)
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    knowledge_resources = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="knowledge_resources"
    )
    doc_templates = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="document_templates"
    )
    status = models.IntegerField(choices=STATUS, default=0)
    order_number = models.IntegerField()

    class Meta:
        ordering = ["-order_number"]

    def __str__(self):
        return self.title
