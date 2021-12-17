"""
XperienceDezignWiz dezignprocess app views configuration

The Search view is set up to render the search results
page when a user searches for a step by name.
The SearchList and SearchNext views are created to render the data
required to display the different Steps within
the Design Thinking Process.
The Step Detail view is created to render the data required to display the
individual Step selected within the Design Thinking Process. It includes
the forms to update the progress status as well as to add comments.
The ToolList view  is created to render the data required to display the
different Tools per step within the Design Thinking Process.
"""

from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.contrib import messages
from django.db.models import Q
from .models import Step, Tool, Progress
from .forms import CommentForm, ProgressForm


def search(request):
    """
    The post function posts the searched term i.e. the title of the
    step, it then returns the step title, which is the link
    to the step detail page, the step image,and the step
    excerpt.

    request: The requests module allows you to send HTTP
    requests using Python.The HTTP request returns a Response
    Object with all the response data (content, encoding, status, etc).
    Definition from https://www.w3schools.com/python/module_requests.asp

    The search function was created by following this you tube video:
    https://youtu.be/AGtae4L5BbI
    It was customised for the site.
    """
    # The first if statement will check if the user has posted a search term
    if request.method == 'POST':
        searched = request.POST['searched']
        # The objects member will be added when the page is rendered
        queryset = Step.objects.all()
        # The step object uses get_object_or_404 to determine if the
        # title of the search term matches a step title, i.e. the step
        # exists in the Step model
        # image is set up to return the step_mage from the step model

        if searched == 'Getting Started':
            step = get_object_or_404(queryset, title=searched)
            image = step.steps_image
            click = ('Click the step name:'
                     ' Getting Started to be directed to the step.')
        elif searched == 'Empathy':
            step = get_object_or_404(queryset, title=searched)
            image = step.steps_image
            click = ('Click the step name: Empathy'
                     ' to be directed to the step.')
        elif searched == 'Define':
            step = get_object_or_404(queryset, title=searched)
            image = step.steps_image
            click = ('Click the step name: Define to be'
                     ' directed to the step.')          
        elif searched == 'Ideate':
            step = get_object_or_404(queryset, title=searched)
            image = step.steps_image
            click = ('Click the step name: Ideate to be'
                     ' directed to the step.')         
        elif searched == 'Prototype':
            step = get_object_or_404(queryset, title=searched)
            image = step.steps_image
            click = ('Click the step name:'
                     ' Prototype to be directed to the step.')
        elif searched == 'Test':
            step = get_object_or_404(queryset, title=searched)
            image = step.steps_image
            click = 'Click the step name: Test to be directed to the step.'
        elif searched == 'Finishing Off':
            step = get_object_or_404(queryset, title=searched)
            image = step.steps_image
            click = ('Click the step name:'
                     ' Finishing Off to be directed to the step.')
            image = step.steps_image
        elif searched != Step.objects.filter(title=searched):
            step = get_object_or_404(queryset, title='None')
            image = step.steps_image
            click = ('You searched for an incorrect term.'
                     ' This search is set up to return the'
                     ' pages for the steps within the'
                     ' Design Thinking process.'
                     ' Please search for one of the steps:'
                     ' Getting Started,'
                     ' Empathy,'
                     ' Define,'
                     ' Ideate,'
                     ' Prototype,'
                     ' Test or'
                     ' Finishing Off.'
                     ' The search field is case sensitive.')

        return render(
            request, 'search.html',
            {
                    'searched': searched,
                    'step': step,
                    'click': click,
                    'image': image,
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
        stored to the Progress table per step.

        If a user is not logged in, the progress status will return
        as 'Not Started' for each step.
        If a user is logged in, but has not as yet created a progress status
        within the Progress table, the function will look for the latest
        progress status created by the admin user. This has been setup on the
        admin site to return 'Not Started' per step.

        self: The self is used to represent the instance of the class.
        **kwargs (Keyword Arguments):  passes variable number of keyword
        arguments dictionary to function on which operation of a dictionary
        can be performed.
        Definition from:
        https://www.programiz.com/python-programming/args-and-kwargs

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
        Docstring as per get_context_data above under
        Class StepList.
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
    to update the fields within the model tables as well as return
    the stored data.
    """

    def get(self, request, slug):
        """
        The get function retrieves the data
        to generate the step details page.

        self: The self is used to represent the instance of the class.
        request: The requests module allows you to send HTTP
        requests using Python.The HTTP request returns a Response
        Object with all the response data (content, encoding, status, etc).
        Definition from https://www.w3schools.com/python/module_requests.asp
        slug: A 'slug' is a way of generating a valid URL, generally using
        data already obtained. It is utilised in this function to retrieve
        the slug created within the Step table and using it to generate the
        URL for the step detail page.

        If and elif statements are utilised to set up navigation between the
        different steps so that the user can navigate back to the previous step
        and forward to the next step.

        An If statement is used to return
        the latest progress status as created by a user and
        stored to the Progress model table per step.
        If a user is logged in, but has not as yet created a progress status
        within the Progress model table, the function will look for the latest
        progress status created by the admin user. This has been set up on the
        admin site to return 'Not Started' per step.
        If a user is not logged in, the progress status will return
        as 'Not Started' for each step.

        An If statement is used to return
        the comments created per step by a user if the user is logged in. If no
        comments have been created, nothing will be returned.
        If the user is not logged in, nothing will be returned.
        """
        queryset = Step.objects.all()
        step = get_object_or_404(queryset, slug=slug)
        resources = step.resources.all()
        tools = step.tools.all()
        image = step.steps_image
        step_display_prev = ''
        step_display_next = ''
        comments = ''
        progress = ''
        if step.title == 'Getting Started':
            step_display_prev = 'finishing-off'
            step_display_next = 'empathy'
        elif step.title == 'Empathy':
            step_display_prev = 'getting-started'
            step_display_next = 'define'
        elif step.title == 'Define':
            step_display_prev = 'empathy'
            step_display_next = 'ideate'
        elif step.title == 'Ideate':
            step_display_prev = 'define'
            step_display_next = 'prototype'
        elif step.title == 'Prototype':
            step_display_prev = 'ideate'
            step_display_next = 'test'
        elif step.title == 'Test':
            step_display_prev = 'prototype'
            step_display_next = 'finishing-off'
        elif step.title == 'Finishing Off':
            step_display_prev = 'test'
            step_display_next = 'getting-started'

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
                'resources': resources,
                'tools': tools,
                'image': image,
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

        The docstring from the get function also applies
        to the post function.

        Additional functionality:
        If the user is logged in, they can complete the comment
        form. If the comment form is valid the user input and
        generated fields will be saved to the Comments table,
        this data can then be fetched to display on the step detail
        page.
        If the user is logged in, they can complete the progress
        form. If the progress form is valid the user input and
        generated fields will be saved to the Progress table,
        this data can then be fetched to display on the step detail
        page.
        """
        queryset = Step.objects
        step = get_object_or_404(queryset, slug=slug)
        resources = step.resources.all()
        tools = step.tools.all()
        image = step.steps_image
        step_display_prev = ''
        step_display_next = ''
        comments = ''
        progress = ''
        if step.title == 'Getting Started':
            step_display_prev = 'finishing-off'
            step_display_next = 'empathy'
        elif step.title == 'Empathy':
            step_display_prev = 'getting-started'
            step_display_next = 'define'
        elif step.title == 'Define':
            step_display_prev = 'empathy'
            step_display_next = 'ideate'
        elif step.title == 'Ideate':
            step_display_prev = 'define'
            step_display_next = 'prototype'
        elif step.title == 'Prototype':
            step_display_prev = 'ideate'
            step_display_next = 'test'
        elif step.title == 'Test':
            step_display_prev = 'prototype'
            step_display_next = 'finishing-off'
        elif step.title == 'Finishing Off':
            step_display_prev = 'test'
            step_display_next = 'getting-started'

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
                'resources': resources,
                'tools': tools,
                'image': image,
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

        self: The self is used to represent the instance of the class.
        request: The requests module allows you to send HTTP
        requests using Python.The HTTP request returns a Response
        Object with all the response data (content, encoding, status, etc).
        Definition from https://www.w3schools.com/python/module_requests.asp
        slug: A 'slug' is a way of generating a valid URL, generally using
        data already obtained. It is utilised in this function to retrieve
        the slug created within the Tool table and using it to generate the
        URL for the step tools page.
        """
        queryset = Tool.objects
        template = get_object_or_404(queryset, slug=slug)
        image = template.image
        return render(
            request,
            'step_tools.html',
            {
                'template': template,
                'image': image,
            },
        )
