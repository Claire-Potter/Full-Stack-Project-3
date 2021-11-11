from django.shortcuts import render
from django.views import generic
from .models import Step


class StepList(generic.ListView):
    """
    Model created to store the data required for creating
    the different Steps within the Design Thinking Process.
    Steps include: Getting Started, Empathy, Define, Ideate,
    Prototype, Test and Finishing Off.
    """
    model = Step
    template_name = "index.html"
    paginate_by = 7
