from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Step
from .forms import CommentForm


class StepList(generic.ListView):
    """
    Model created to store the data required for creating
    the different Steps within the Design Thinking Process.
    Steps include: Getting Started, Empathy, Define
    """
    model = Step
    context_object_name = 'step_list'
    queryset = Step.objects.filter(list_number='1')
    template_name = "first.html"
    paginate_by: 3


class StepNext(generic.ListView):
    """
    Model created to store the data required for creating
    the different Steps within the Design Thinking Process.
    Steps include: Ideate, Prototype, Test
    """
    model = Step
    context_object_name = 'step_next'
    queryset = Step.objects.filter(list_number='2')
    template_name = "next.html"
    paginate_by: 3


class StepDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Step.objects
        step = get_object_or_404(queryset, slug=slug)
        comments = ""
        if step.comments.filter(id=self.request.user.id).exists():
            comments = step.comments.order_by("created_on")
        
       

        return render(
            request,
            "step_detail.html",
            {
                "step": step,
                "comments": comments,
                "comment_form": CommentForm()
            },
        )
