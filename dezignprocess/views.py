from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.contrib import messages
from .models import Step
from .forms import CommentForm


class StepList(generic.ListView, View):
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


def StepSearch(request):
    queryset = Step.objects
    step_f = queryset.all().order_by('order_number')
    step_f_html = []
    for instance in queryset.all():
        step_f_html.append({'title': instance.title,
                            'excerpt': instance.excerpt,
                            'order_number': instance.order_number,
                            'progress': instance.progress})
    step_dic = {'step_f': step_f, 'ac_tab_n': 'ac_tab', 'step_f_html': step_f_html}
    return render(request, "first.html", step_dic)


class StepDetail(View):

    def get(self, request, slug,):
        queryset = Step.objects
        step = get_object_or_404(queryset, slug=slug)
        comments = ""
        if step.comments.filter(name=self.request.user.username).exists():
            comments = step.comments.filter(name=self.request.user.username).order_by("-created_on")

        return render(
            request,
            "step_detail.html",
            {
                "step": step,
                "comments": comments,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug,):
        queryset = Step.objects
        step = get_object_or_404(queryset, slug=slug)
        comments = ""
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
                "comments": comments,
                "comment_form": CommentForm()
            },
        )
