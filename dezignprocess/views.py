from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.contrib import messages
from .models import Step, Template
from .forms import CommentForm


def search(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        steps = Step.objects.filter(title=searched)

        return render(
            request, 'search.html',
            {
                'searched': searched,
                'steps': steps,
            },
        )
    else:

        return render(
            request, 'search.html',
            {},)


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
    template_name = 'next.html'
    paginate_by: 3


class StepDetail(View):

    def get(self, request, slug,):
        queryset = Step.objects.all()
        step = get_object_or_404(queryset, slug=slug)
        comments = ""
        template_01 = ""
        template_02 = ""
        template_03 = ""
        step_display_prev = ""
        step_display_next = ""
        if step.title == 'Getting Started':
            step_display_prev = 'finishing-off'
            step_display_next = 'empathy'
            template_01 = 'No Template Required'
            template_02 = ""
            template_03 = ""
        elif step.title == 'Empathy':
            step_display_prev = 'getting-started'
            step_display_next = 'define'
            template_01 = 'Survey'
            template_02 = 'Interview Guide'
            template_03 = 'Persona'
        elif step.title == 'Define':
            step_display_prev = 'empathy'
            step_display_next = 'ideate'
            template_01 = 'Problem Statement'
            template_02 = ""
            template_03 = ""
        elif step.title == 'Ideate':
            step_display_prev = 'define'
            step_display_next = 'prototype'
            template_01 = 'Round Robin'
            template_02 = 'Opposite Thinking'
            template_03 = ""
        elif step.title == 'Prototype':
            step_display_prev = 'ideate'
            step_display_next = 'test'
            template_01 = 'Types Of Prototypes'
            template_02 = ""
            template_03 = ""
        elif step.title == 'Test':
            step_display_prev = 'prototype'
            step_display_next = 'finishing-off'
            template_01 = 'How To Conduct a User Test'
            template_02 = ""
            template_03 = ""
        elif step.title == 'Finishing Off':
            step_display_prev = 'test'
            step_display_next = 'getting-started'
            template_01 = 'No Template Required'
            template_02 = ""
            template_03 = ""
        else:
            ""
        if step.comments.filter(name=self.request.user.username).exists():
            comments = step.comments.filter(name=self.request.user.username).order_by("-created_on")
        return render(
            request,
            "step_detail.html",
            {
                "step": step,
                "template_01": template_01,
                "template_02": template_02,
                "template_03": template_03,
                "comments": comments,
                "comment_form": CommentForm(),
                "step_display_prev": step_display_prev,
                "step_display_next": step_display_next
            },
        )

    def post(self, request, slug,):
        queryset = Step.objects
        step = get_object_or_404(queryset, slug=slug)
        step_display_prev = ""
        step_display_next = ""
        template_01 = ""
        template_02 = ""
        template_03 = ""
        comments = ""
        if step.title == 'Getting Started':
            step_display_prev = 'finishing-off'
            step_display_next = 'empathy'
            template_01 = 'No Template Required'
            template_02 = ""
            template_03 = ""
        elif step.title == 'Empathy':
            step_display_prev = 'getting-started'
            step_display_next = 'define'
            template_01 = 'Survey'
            template_02 = 'Interview Guide'
            template_03 = 'Persona'
        elif step.title == 'Define':
            step_display_prev = 'empathy'
            step_display_next = 'ideate'
            template_01 = 'Problem Statement'
            template_02 = ""
            template_03 = ""
        elif step.title == 'Ideate':
            step_display_prev = 'define'
            step_display_next = 'prototype'
            template_01 = 'Round Robin'
            template_02 = 'Opposite Thinking'
            template_03 = ""
        elif step.title == 'Prototype':
            step_display_prev = 'ideate'
            step_display_next = 'test'
            template_01 = 'Types Of Prototypes'
            template_02 = ""
            template_03 = ""
        elif step.title == 'Test':
            step_display_prev = 'prototype'
            step_display_next = 'finishing-off'
            template_01 = 'How To Conduct a User Test'
            template_02 = ""
            template_03 = ""
        elif step.title == 'Finishing Off':
            step_display_prev = 'test'
            step_display_next = 'getting-started'
            template_01 = 'No Template Required'
            template_02 = ""
            template_03 = ""
        else:
            ""
        if step.comments.filter(name=self.request.user.username).exists():
            comments = step.comments.filter(name=self.request.user.username).order_by("-created_on")

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():

            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.step = step
            comment.save()
            messages.success(request, 'Comment submission successful')
        else:
            comment_form = CommentForm()

        return render(
            request,
            "step_detail.html",
            {
                "step": step,
                "template_01": template_01,
                "template_02": template_02,
                "template_03": template_03,
                "comments": comments,
                "comment_form": CommentForm(),
                "step_display_prev": step_display_prev,
                "step_display_next": step_display_next,

            },
        )


class TemplatesList(View):
    """
    Model created to store the data required for creating
    the different Steps within the Design Thinking Process.
    Steps include: Getting Started, Empathy, Define
    """
    def get(self, request, slug,):
        queryset = Template.objects
        template = get_object_or_404(queryset, slug=slug)
        return_to_step = ""
        if template.step == 'Getting Started':
            return_to_step = 'getting-started'
        elif template.step == 'Empathy':
            return_to_step = 'empathy'
        elif template.step == 'Define':
            return_to_step = 'define'
        elif template.step == 'Ideate':
            return_to_step = 'ideate'
        elif template.step == 'Prototype':
            return_to_step = 'prototype'
        elif template.step == 'Test':
            return_to_step = 'test'
        elif template.step == 'Finishing Off':
            return_to_step = 'finishing-off'
        else:
            return_to_step = 'getting-started'
        return render(
            request,
            "step_templates.html",
            {
                "template": template,
                "return_to_step": return_to_step,
            },
        )
