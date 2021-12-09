"""
XperienceDezignWiz dezignprocess app views configuration

The Search view is set up to render the search results
page when a user searches for a step by name.
The SearchList and SearchNext views are created to render the data
required to display the different Steps within
the Design Thinking Process.


"""

from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.contrib import messages
from django.db.models import Q
from .models import Step, Tool, Progress
from .forms import CommentForm, ProgressForm


class Search(View):
    """
    the Search view is set up to render the search results
    page when a user searches for a step by name.
    """

    def post(self, request):
        """
        The post function was created by following this you tube video:
        https://youtu.be/AGtae4L5BbI
        It was customised for the site.
        Complex lookups with Q objects was referenced here:
        https://docs.djangoproject.com/en/3.2/topics/db/queries/ to create the
        lookups.
        """
        if request.method == 'POST':
            searched = request.POST['searched']
            steps = Step.objects.filter(title=searched)
            step = get_object_or_404(steps)
            progress = ''
            if step.progress.filter(name=self.request.user.username).exists():
                progress = step.progress.filter(
                                                  Q(name=self.request
                                                    .user
                                                    .username) |
                                                  Q(name='admin')).latest()
            else:
                progress = step.progress.filter(
                                                 progress='Not'
                                                 ' Started').latest()

            return render(
                request, 'search.html',
                {
                    'searched': searched,
                    'steps': steps,
                    'progress': progress,
                },
            )
        else:

            return render(
                request, 'search.html',
                {},)


class StepList(generic.ListView):
    """
    View created to render the data required to display the
    different Steps within the Design Thinking Process.
    Steps include: Getting Started, Empathy, Define.
    """
    model = Step
    model_two = Progress
    context_object_name = 'step_list'
    queryset = Step.objects.filter(list_number='1')
    template_name = 'first.html'
    paginate_by: 3

    def get_context_data(self, **kwargs):
        """
        The get_context_data function is setup to return
        the latest progress status as created by a user and
        stored to the Progress model per step. If a user is not logged in
        the progress status will return as 'Not Started' for each step.
        If a user is logged in, but has not as yet created a progress status
        within the Progress model, the function will look for the latest
        progress status created by the admin user. This has been setup on the
        admin site to return 'Not Started' per step.
        the get_context_data function was written by referencing
        the following article: (https://medium.com/@hassanraza/
        when-to-use-get-get-queryset-get-context-data-in-django-952df6be036a).
        Complex lookups with Q objects was referenced here:
        https://docs.djangoproject.com/en/3.2/topics/db/queries/ to create the
        lookups.
        """
        queryset_two = Progress.objects.all()
        if queryset_two.filter(name=self.request.user
                               .username).exists():
            context = super().get_context_data(**kwargs)
            context['progress'] = queryset_two.filter(
                                                      Q(name=self.request
                                                        .user
                                                        .username) |
                                                      Q(name='admin'),
                                                      step='1').latest()
            context['progress_02'] = queryset_two.filter(
                                                      Q(name=self.request
                                                        .user
                                                        .username) |
                                                      Q(name='admin'),
                                                      step='2').latest()
            context['progress_03'] = queryset_two.filter(
                                                      Q(name=self.request
                                                        .user
                                                        .username) |
                                                      Q(name='admin'),
                                                      step='3').latest()
            return context
        else:
            context = super().get_context_data(**kwargs)
            context['progress'] = queryset_two.filter(step='1',
                                                      progress='Not'
                                                      ' Started').latest()
            context['progress_02'] = queryset_two.filter(step='2',
                                                         progress='Not'
                                                         ' Started').latest()
            context['progress_03'] = queryset_two.filter(step='3',
                                                         progress='Not'
                                                         ' Started').latest()
            return context


class StepNext(generic.ListView):
    """
    View created to render the data required to display the
    different Steps within the Design Thinking Process.
    Steps include: Ideate, Prototype, Test
    """
    model = Step
    model_two = Progress
    context_object_name = 'step_next'
    queryset = Step.objects.filter(list_number='2')
    template_name = 'next.html'
    paginate_by: 3

    def get_context_data(self, **kwargs):
        """
        The get_context_data function is setup to return
        the latest progress status as created by a user and
        stored to the Progress model per step. If a user is not logged in
        the progress status will return as 'Not Started' for each step.
        If a user is logged in, but has not as yet created a progress status
        within the Progress model, the function will look for the latest
        progress status created by the admin user. This has been setup on the
        admin site to return 'Not Started' per step.
        the get_context_data function was written by referencing
        the following article: (https://medium.com/@hassanraza/
        when-to-use-get-get-queryset-get-context-data-in-django-952df6be036a).
        Complex lookups with Q objects was referenced here:
        https://docs.djangoproject.com/en/3.2/topics/db/queries/ to create the
        lookups.
        """
        queryset_two = Progress.objects.all()
        if queryset_two.filter(name=self.request.user.username).exists():
            context = super().get_context_data(**kwargs)
            context['progress'] = queryset_two.filter(
                                                      Q(name=self.request
                                                        .user
                                                        .username) |
                                                      Q(name='admin'),
                                                      step='4').latest()
            context['progress_02'] = queryset_two.filter(
                                                      Q(name=self.request
                                                        .user
                                                        .username) |
                                                      Q(name='admin'),
                                                      step='5').latest()
            context['progress_03'] = queryset_two.filter(
                                                      Q(name=self.request
                                                        .user
                                                        .username) |
                                                      Q(name='admin'),
                                                      step='6').latest()
            context['progress_04'] = queryset_two.filter(
                                                         Q(name=self.request
                                                           .user
                                                           .username) |
                                                         Q(name='admin'),
                                                         step='8').latest()
            return context

        else:
            context = super().get_context_data(**kwargs)
            context['progress'] = queryset_two.filter(step='4',
                                                      progress='Not'
                                                      ' Started').latest()
            context['progress_02'] = queryset_two.filter(step='5',
                                                         progress='Not'
                                                         ' Started').latest()
            context['progress_03'] = queryset_two.filter(step='6',
                                                         progress='Not'
                                                         ' Started').latest()
            context['progress_04'] = queryset_two.filter(step='8',
                                                         progress='Not'
                                                         ' Started').latest()
            return context


class StepDetail(View):
    """
    View created to render the data required to display the
    individual Step selected within the Design Thinking Process.
    The view iterates through the steps within the Step Model
    rendering the required fields. The view also references
    the Progress and the Comments models and forms in order
    to update the fields within the models as well as return
    the stored data.
    """

    def get(self, request, slug):
        """
        The get function retrieves the data
        to generate the step details page.
        """
        queryset = Step.objects.all()
        step = get_object_or_404(queryset, slug=slug)
        step_display_prev = ''
        step_display_next = ''
        template_01 = ''
        template_02 = ''
        template_03 = ''
        temp_slug_01 = ''
        temp_slug_02 = ''
        temp_slug_03 = ''
        comments = ''
        progress = ''
        if step.title == 'Getting Started':
            step_display_prev = 'finishing-off'
            step_display_next = 'empathy'
            template_01 = 'How to Start'
            template_02 = 'The Non-Linear Nature of Design Thinking'
            template_03 = 'placeholder'
            temp_slug_01 = 'how-to-start'
            temp_slug_02 = 'non-linear'
            temp_slug_03 = ''
        elif step.title == 'Empathy':
            step_display_prev = 'getting-started'
            step_display_next = 'define'
            template_01 = 'Survey'
            template_02 = 'Interview Guide'
            template_03 = 'placeholder'
            temp_slug_01 = 'survey-details'
            temp_slug_02 = 'interview-guide'
            temp_slug_03 = ''
        elif step.title == 'Define':
            step_display_prev = 'empathy'
            step_display_next = 'ideate'
            template_01 = 'Problem Statement'
            template_02 = 'Persona'
            template_03 = 'placeholder'
            temp_slug_01 = 'problem-statement'
            temp_slug_02 = 'persona'
            temp_slug_03 = ''
        elif step.title == 'Ideate':
            step_display_prev = 'define'
            step_display_next = 'prototype'
            template_01 = 'Brainstorming'
            template_02 = 'The Worst Possible Idea'
            template_03 = 'placeholder'
            temp_slug_01 = 'brainstorming'
            temp_slug_02 = 'the-worst-possible-idea'
            temp_slug_03 = ''
        elif step.title == 'Prototype':
            step_display_prev = 'ideate'
            step_display_next = 'test'
            template_01 = 'Types Of Prototypes'
            template_02 = 'Which Prototype Should I Build?'
            template_03 = 'placeholder'
            temp_slug_01 = 'types-of-prototypes'
            temp_slug_02 = 'which-prototype-should-i-build'
            temp_slug_03 = ''
        elif step.title == 'Test':
            step_display_prev = 'prototype'
            step_display_next = 'finishing-off'
            template_01 = 'How To Conduct a User Test'
            template_02 = 'placeholder'
            template_03 = 'placeholder'
            temp_slug_01 = 'conduct-user-test'
            temp_slug_02 = ''
            temp_slug_03 = ''
        elif step.title == 'Finishing Off':
            step_display_prev = 'test'
            step_display_next = 'getting-started'
            template_01 = 'Storytelling'
            template_02 = 'placeholder'
            template_03 = 'placeholder'
            temp_slug_01 = 'storytelling'
            temp_slug_02 = ''
            temp_slug_03 = ''

        if step.comments.filter(name=self.request.user.username).exists():
            comments = step.comments.filter(
                       name=self.request.user.username).order_by('-created_on')
        if step.progress.filter(name=self.request.user.username).exists():
            progress = step.progress.filter(
                                            Q(name=self.request
                                              .user
                                              .username) |
                                            Q(name='admin')).latest()
        else:
            progress = step.progress.filter(
                                            progress='Not'
                                            ' Started').latest()

        return render(
            request,
            'step_detail.html',
            {
                'step': step,
                'template_01': template_01,
                'template_02': template_02,
                'template_03': template_03,
                'temp_slug_01': temp_slug_01,
                'temp_slug_02': temp_slug_02,
                'temp_slug_03': temp_slug_03,
                'comments': comments,
                'comment_form': CommentForm(),
                'progress': progress,
                'progress_form': ProgressForm(),
                'step_display_prev': step_display_prev,
                'step_display_next': step_display_next
            },
        )

    def post(self, request, slug):
        """
        The post function retrieves the data
        captured by the user and stores the Progress
        update in the Progress table and the Comment
        update in the Comments table.
        """
        queryset = Step.objects
        step = get_object_or_404(queryset, slug=slug)
        step_display_prev = ''
        step_display_next = ''
        template_01 = ''
        template_02 = ''
        template_03 = ''
        temp_slug_01 = ''
        temp_slug_02 = ''
        temp_slug_03 = ''
        comments = ''
        progress = ''
        if step.title == 'Getting Started':
            step_display_prev = 'finishing-off'
            step_display_next = 'empathy'
            template_01 = 'How to Start'
            template_02 = 'The Non-Linear Nature of Design Thinking'
            template_03 = 'placeholder'
            temp_slug_01 = 'how-to-start'
            temp_slug_02 = 'non-linear'
            temp_slug_03 = ''
        elif step.title == 'Empathy':
            step_display_prev = 'getting-started'
            step_display_next = 'define'
            template_01 = 'Survey'
            template_02 = 'Interview Guide'
            template_03 = 'placeholder'
            temp_slug_01 = 'survey-details'
            temp_slug_02 = 'interview-guide'
            temp_slug_03 = ''
        elif step.title == 'Define':
            step_display_prev = 'empathy'
            step_display_next = 'ideate'
            template_01 = 'Problem Statement'
            template_02 = 'Persona'
            template_03 = 'placeholder'
            temp_slug_01 = 'problem-statement'
            temp_slug_02 = 'persona'
            temp_slug_03 = ''
        elif step.title == 'Ideate':
            step_display_prev = 'define'
            step_display_next = 'prototype'
            template_01 = 'Brainstorming'
            template_02 = 'The Worst Possible Idea'
            template_03 = 'placeholder'
            temp_slug_01 = 'brainstorming'
            temp_slug_02 = 'the-worst-possible-idea'
            temp_slug_03 = ''
        elif step.title == 'Prototype':
            step_display_prev = 'ideate'
            step_display_next = 'test'
            template_01 = 'Types Of Prototypes'
            template_02 = 'Which Prototype Should I Build?'
            template_03 = 'placeholder'
            temp_slug_01 = 'types-of-prototypes'
            temp_slug_02 = 'which-prototype-should-i-build'
            temp_slug_03 = ''
        elif step.title == 'Test':
            step_display_prev = 'prototype'
            step_display_next = 'finishing-off'
            template_01 = 'How To Conduct a User Test'
            template_02 = 'placeholder'
            template_03 = 'placeholder'
            temp_slug_01 = 'conduct-user-test'
            temp_slug_02 = ''
            temp_slug_03 = ''
        elif step.title == 'Finishing Off':
            step_display_prev = 'test'
            step_display_next = 'getting-started'
            template_01 = 'Storytelling'
            template_02 = 'placeholder'
            template_03 = 'placeholder'
            temp_slug_01 = 'storytelling'
            temp_slug_02 = ''
            temp_slug_03 = ''

        if step.comments.filter(name=self.request.user.username).exists():
            comments = step.comments.filter(
                       name=self.request.user.username).order_by('-created_on')

        if step.progress.filter(name=self.request.user.username).exists():
            progress = step.progress.filter(
                                            Q(name=self.request
                                              .user
                                              .username) |
                                            Q(name='admin')).latest()
        else:
            progress = step.progress.filter(
                                            progress='Not'
                                            ' Started').latest()

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
            messages.success(request,
                             'Progress status update submission successful')
        else:
            progress_form = ProgressForm()

        return render(
            request,
            'step_detail.html',
            {
                'step': step,
                'template_01': template_01,
                'template_02': template_02,
                'template_03': template_03,
                'temp_slug_01': temp_slug_01,
                'temp_slug_02': temp_slug_02,
                'temp_slug_03': temp_slug_03,
                'comments': comments,
                'progress': progress,
                'comment_form': CommentForm(),
                'progress_form': ProgressForm(),
                'step_display_prev': step_display_prev,
                'step_display_next': step_display_next,

            },
        )


class ToolsList(View):
    """
    View created to render the data required to display the
    different Tools per step within the Design Thinking Process.
    """
    def get(self, request, slug,):
        """
        The get function retrieves the data
        to generate the tools details page.
        """
        queryset = Tool.objects
        template = get_object_or_404(queryset, slug=slug)
        return render(
            request,
            'step_tools.html',
            {
                'template': template,
            },
        )
