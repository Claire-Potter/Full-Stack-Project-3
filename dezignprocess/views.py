from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.contrib import messages
from .models import Step, Tool, Progress
from .forms import CommentForm, ProgressForm


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
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if Step.objects.filter(username_id=self.request.user).exists():
            context['progress'] = Progress.objects.filter(username_id=self.request.user).latest()
        else:
            context['progress'] = Progress.objects.filter(progress='Not Started').latest()
        return context


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
        step_display_prev = ""
        step_display_next = ""
        template_01 = ""
        template_02 = ""
        template_03 = ""
        temp_slug_01 = ""
        temp_slug_02 = ""
        temp_slug_03 = ""
        comments = ""
        progress = ""
        if step.title == 'Getting Started':
            step_display_prev = 'finishing-off'
            step_display_next = 'empathy'
            template_01 = 'How to Start'
            template_02 = 'The Non-Linear Nature of Design Thinking'
            template_03 = 'placeholder'
            temp_slug_01 = "how-to-start"
            temp_slug_02 = "non-linear"
            temp_slug_03 = ""
        elif step.title == 'Empathy':
            step_display_prev = 'getting-started'
            step_display_next = 'define'
            template_01 = 'Survey'
            template_02 = 'Interview Guide'
            template_03 = 'placeholder'
            temp_slug_01 = "survey-details"
            temp_slug_02 = "interview-guide"
            temp_slug_03 = ""
        elif step.title == 'Define':
            step_display_prev = 'empathy'
            step_display_next = 'ideate'
            template_01 = 'Problem Statement'
            template_02 = 'Persona'
            template_03 = 'placeholder'
            temp_slug_01 = "problem-statement"
            temp_slug_02 = "persona"
            temp_slug_03 = ""
        elif step.title == 'Ideate':
            step_display_prev = 'define'
            step_display_next = 'prototype'
            template_01 = 'Brainstorming'
            template_02 = 'The Worst Possible Idea'
            template_03 = 'placeholder'
            temp_slug_01 = "brainstorming"
            temp_slug_02 = "the-worst-possible-idea"
            temp_slug_03 = ""
        elif step.title == 'Prototype':
            step_display_prev = 'ideate'
            step_display_next = 'test'
            template_01 = 'Types Of Prototypes'
            template_02 = 'Which Prototype Should I Build?'
            template_03 = 'placeholder'
            temp_slug_01 = "types-of-prototypes"
            temp_slug_02 = "which-prototype-should-i-build"
            temp_slug_03 = ""
        elif step.title == 'Test':
            step_display_prev = 'prototype'
            step_display_next = 'finishing-off'
            template_01 = 'How To Conduct a User Test'
            template_02 = 'placeholder'
            template_03 = 'placeholder'
            temp_slug_01 = "conduct-user-test"
            temp_slug_02 = ""
            temp_slug_03 = ""
        elif step.title == 'Finishing Off':
            step_display_prev = 'test'
            step_display_next = 'getting-started'
            template_01 = 'Storytelling'
            template_02 = 'placeholder'
            template_03 = 'placeholder'
            temp_slug_01 = "storytelling"
            temp_slug_02 = ""
            temp_slug_03 = ""
        else:
            ""
        if step.comments.filter(name=self.request.user.username).exists():
            comments = step.comments.filter(
                       name=self.request.user.username).order_by("-created_on")
        if step.progress.filter(name=self.request.user.username).exists():
            progress = step.progress.filter(
                       name=self.request.user.username).latest()
    
        return render(
            request,
            "step_detail.html",
            {
                "step": step,
                "template_01": template_01,
                "template_02": template_02,
                "template_03": template_03,
                "temp_slug_01": temp_slug_01,
                "temp_slug_02": temp_slug_02,
                "temp_slug_03": temp_slug_03,
                "comments": comments,
                "comment_form": CommentForm(),
                "progress": progress,
                "progress_form": ProgressForm(),
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
        temp_slug_01 = ""
        temp_slug_02 = ""
        temp_slug_03 = ""
        comments = ""
        progress = ""
        if step.title == 'Getting Started':
            step_display_prev = 'finishing-off'
            step_display_next = 'empathy'
            template_01 = 'How to Start'
            template_02 = 'The Non-Linear Nature of Design Thinking'
            template_03 = 'placeholder'
            temp_slug_01 = "how-to-start"
            temp_slug_02 = "non-linear"
            temp_slug_03 = ""
        elif step.title == 'Empathy':
            step_display_prev = 'getting-started'
            step_display_next = 'define'
            template_01 = 'Survey'
            template_02 = 'Interview Guide'
            template_03 = 'placeholder'
            temp_slug_01 = "survey-details"
            temp_slug_02 = "interview-guide"
            temp_slug_03 = ""
        elif step.title == 'Define':
            step_display_prev = 'empathy'
            step_display_next = 'ideate'
            template_01 = 'Problem Statement'
            template_02 = 'Persona'
            template_03 = 'placeholder'
            temp_slug_01 = "problem-statement"
            temp_slug_02 = "persona"
            temp_slug_03 = ""
        elif step.title == 'Ideate':
            step_display_prev = 'define'
            step_display_next = 'prototype'
            template_01 = 'Brainstorming'
            template_02 = 'The Worst Possible Idea'
            template_03 = 'placeholder'
            temp_slug_01 = "brainstorming"
            temp_slug_02 = "the-worst-possible-idea"
            temp_slug_03 = ""
        elif step.title == 'Prototype':
            step_display_prev = 'ideate'
            step_display_next = 'test'
            template_01 = 'Types Of Prototypes'
            template_02 = 'Which Prototype Should I Build?'
            template_03 = 'placeholder'
            temp_slug_01 = "types-of-prototypes"
            temp_slug_02 = "which-prototype-should-i-build"
            temp_slug_03 = ""
        elif step.title == 'Test':
            step_display_prev = 'prototype'
            step_display_next = 'finishing-off'
            template_01 = 'How To Conduct a User Test'
            template_02 = 'placeholder'
            template_03 = 'placeholder'
            temp_slug_01 = "conduct-user-test"
            temp_slug_02 = ""
            temp_slug_03 = ""
        elif step.title == 'Finishing Off':
            step_display_prev = 'test'
            step_display_next = 'getting-started'
            template_01 = 'Storytelling'
            template_02 = 'placeholder'
            template_03 = 'placeholder'
            temp_slug_01 = "storytelling"
            temp_slug_02 = ""
            temp_slug_03 = ""
        else:
            ""
        if step.comments.filter(name=self.request.user.username).exists():
            comments = step.comments.filter(
                       name=self.request.user.username).order_by("-created_on")
        
        if step.progress.filter(name=self.request.user.username).exists():
            progress = step.progress.filter(
                       name=self.request.user.username).latest()

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

        progress_form = ProgressForm(data=request.POST)

        if progress_form.is_valid():

            progress_form.instance.email = request.user.email
            progress_form.instance.name = request.user.username
            progress = progress_form.save(commit=False)
            progress.step = step
            progress.save()
            messages.success(request, 'Progress status update submission successful')
        else:
            progress_form = ProgressForm()

        return render(
            request,
            "step_detail.html",
            {
                "step": step,
                "template_01": template_01,
                "template_02": template_02,
                "template_03": template_03,
                "temp_slug_01": temp_slug_01,
                "temp_slug_02": temp_slug_02,
                "temp_slug_03": temp_slug_03,
                "comments": comments,
                "progress": progress,
                "comment_form": CommentForm(),
                "progress_form": ProgressForm(),
                "step_display_prev": step_display_prev,
                "step_display_next": step_display_next,

            },
        )


class ToolsList(View):
    """
    Model created to store the data required for creating
    the different Steps within the Design Thinking Process.
    Steps include: Getting Started, Empathy, Define
    """
    def get(self, request, slug,):
        queryset = Tool.objects
        template = get_object_or_404(queryset, slug=slug)
        return render(
            request,
            "step_tools.html",
            {
                "template": template,
            },
        )
