"""
Xperiencedezignwiz dezigntools app  views

The following site provided a Django project
blueprint to build a survey app. This was
followed alongside the git hub page. I then customised
the views to align with my
site's design and functionality.
https://mattsegal.dev/django-survey-project.html.

survey-list: User can view all their surveys that they
have created.

detail: User can view an active survey which
they have created.

send_email: User can complete the EmailForm
to be able to send their survey url out to multiple
recipients.

create: User can create a survey.

delete: User can delete a survey.

edit: User can add questions to a draft survey,
then acitvate the survey.

question_create: User can add a question to a
draft survey.

option-create: User can add options to
a survey question.

start: Survey-taker can start a survey

submit: Survey-taker submit their
completed survey.

thanks: Survey-taker receives a thank-you message.
"""

from django.db import transaction
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.forms.formsets import formset_factory
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import (Survey, Question, Answer, Submission,
                     AgeRange, Gender, Industry, AgeQuestion,
                     GenderQuestion, IndustryQuestion, DefaultOptions,
                     DefaultAnswers
                     )
from .forms import (SurveyForm, QuestionForm, OptionForm, AnswerForm,
                    BaseAnswerFormSet, EmailForm,
                    DefaultOptionsForm, DefaultAnswerForm)


# @login_required checks if the user is logged in to display
# the view, if they are not, they will be required to login
# before they can access the page
@login_required
def survey_list(request):
    """
    User can view all their surveys that they
    have created. The options view and delete will
    be available if the survey is active. The options
    edit and delete will be available if the survey is not active.

    request: The requests module allows you to send HTTP
    requests using Python.The HTTP request returns a Response
    Object with all the response data (content, encoding, status, etc).
    Definition from https://www.w3schools.com/python/module_requests.asp
    """
    surveys = (Survey.objects
               .filter(creator=request.user).order_by('-created_at').all())
    # only surveys created by the logged in user will display
    return render(request, 'survey/list.html', {'surveys': surveys})


# @login_required checks if the user is logged in to display
# the view, if they are not, they will be required to login
# before they can access the page
@login_required
def detail(request, p_k):
    """
    User can view an active survey which
    they have created. This includes a link
    to start the survey and number of submissions.
    Chart-js is utilised to display the percentage
    of the default question option which has been selected for
    gender, age range and industry. The custom questions
    and their options are displayed with the percentage
    figure of each option selection from the submitted
    completed surveys.

    request: The requests module allows you to send HTTP
    requests using Python.The HTTP request returns a Response
    Object with all the response data (content, encoding, status, etc).
    Definition from https://www.w3schools.com/python/module_requests.asp

    pk: Regardless of whether you define a primary key field yourself,
    or let Django supply one for you, each model will have a property
    called pk. It behaves like a normal attribute on the model, but
    is actually an alias for whichever attribute is the primary key field
    for the model. You can read and set this value,
    just as you would for any other attribute,
    and it will update the correct field in the model.
    description from:
    https://www.kite.com/python/docs/django.db.models.Model.pk
    """
    try:
        survey = (Survey.objects
                  .prefetch_related('question_set__option_set')
                  .get(pk=p_k, creator=request.user, is_active=True))
    # the following warning  was displaying:
    # Consider explicitly re-raising using the 'from' keyword
    # Stack overflow solution added to all cases to resolve:
    # https://stackoverflow.com/questions/63738900/pylint-raise-missing-from
    except Survey.DoesNotExist as survey_no_exist:
        raise Http404() from survey_no_exist
    # Calculate the results of user added questions
    questions = survey.question_set.all()
    for question in questions:
        # for every question in all questions
        # get the list of option primary keys and add them to
        # option_pks
        option_pks = question.option_set.values_list('pk', flat=True)
        # count the number of option pks in the total answers for the survey
        # match per option pk
        total_answers_q = (Answer.objects.
                           filter(option_id__in=option_pks).count())
        for option in question.option_set.all():
            num_answers = Answer.objects.filter(option=option).count()
            # convert to a percentage of total answers
            option.percent = (100.0 * num_answers /
                              total_answers_q if total_answers_q else 0)

    total_answers = DefaultAnswers.objects.filter(survey_id=p_k).count()
    age_18_under_answers = (DefaultAnswers.objects
                            .filter(age_range=8, survey_id=p_k).count())
    age_18_24_answers = (DefaultAnswers.objects.filter(age_range=9,
                                                       survey_id=p_k).count())
    age_25_34_answers = (DefaultAnswers.objects.filter(age_range=10,
                                                       survey_id=p_k).count())
    age_35_44_answers = (DefaultAnswers.objects.filter(age_range=11,
                                                       survey_id=p_k).count())
    age_45_54_answers = (DefaultAnswers.objects.filter(age_range=12,
                                                       survey_id=p_k).count())
    age_55_64_answers = (DefaultAnswers.objects.filter(age_range=13,
                                                       survey_id=p_k).count())
    age_65_plus_answers = (DefaultAnswers.objects.filter(age_range=14).count())
    # convert to a percentage of total answers
    under_18_age_range_percentage = (100.0 * age_18_under_answers /
                                     total_answers if total_answers else 0)
    up_to_24_age_range_percentage = (100.0 * age_18_24_answers /
                                     total_answers if total_answers else 0)
    up_to_34_age_range_percentage = (100.0 * age_25_34_answers /
                                     total_answers if total_answers else 0)
    up_to_44_age_range_percentage = (100.0 * age_35_44_answers /
                                     total_answers if total_answers else 0)
    up_to_54_age_range_percentage = (100.0 * age_45_54_answers /
                                     total_answers if total_answers else 0)
    up_to_64_age_range_percentage = (100.0 * age_55_64_answers /
                                     total_answers if total_answers else 0)
    up_to_65_plus_age_range_percentage = (100.0 * age_65_plus_answers /
                                          total_answers if
                                          total_answers else 0)

    # fetch the hosting url
    host = request.get_host()
    # fetch the survey-start path and add the survey primary key
    public_path = reverse('survey-start', args=[p_k])
    # create an accessible url by adding http / https with the host
    # and the path
    public_url = f'{request.scheme}://{host}{public_path}'
    # count the total number of submissions received for the survey
    num_submissions = survey.submission_set.filter(is_complete=True).count()

    return render(
        request,
        'survey/detail.html',
        {
            'survey': survey,
            'public_url': public_url,
            'questions': questions,
            'num_submissions': num_submissions,
            'under_18_age_range_percentage': under_18_age_range_percentage,
            'up_to_24_age_range_percentage': up_to_24_age_range_percentage,
            'up_to_34_age_range_percentage': up_to_34_age_range_percentage,
            'up_to_44_age_range_percentage': up_to_44_age_range_percentage,
            'up_to_54_age_range_percentage': up_to_54_age_range_percentage,
            'up_to_64_age_range_percentage': up_to_64_age_range_percentage,
            'up_to_65_plus_age_range_percentage':
            up_to_65_plus_age_range_percentage,
        },
    )


# @login_required checks if the user is logged in to display
# the view, if they are not, they will be required to login
# before they can access the page
@login_required
def send_email(request, p_k):
    """
    User can complete the EmailForm
    to be able to send their survey url out to multiple
    recipients.

    request: The requests module allows you to send HTTP
    requests using Python.The HTTP request returns a Response
    Object with all the response data (content, encoding, status, etc).
    Definition from https://www.w3schools.com/python/module_requests.asp

    pk: Regardless of whether you define a primary key field yourself,
    or let Django supply one for you, each model will have a property
    called pk. It behaves like a normal attribute on the model, but
    is actually an alias for whichever attribute is the primary key field
    for the model. You can read and set this value,
    just as you would for any other attribute,
    and it will update the correct field in the model.
    description from:
    https://www.kite.com/python/docs/django.db.models.Model.pk

    Set up according to django EmailMultiAlternatives
    https://docs.djangoproject.com/en/4.0/topics/email/
    and include Sendgrid email template
    """
    try:
        # try to fetch the survey if it exists
        survey = (Survey.objects
                  .prefetch_related('question_set__option_set')
                  .get(pk=p_k, creator=request.user, is_active=True))
    except Survey.DoesNotExist as survey_no_exist:
        raise Http404() from survey_no_exist
    # create the url for the survey
    host = request.get_host()
    public_path = reverse('survey-start', args=[p_k])
    public_url = f'{request.scheme}://{host}{public_path}'

    # create a variable to keep track of the form
    message_sent = False
    recipient_list = ''

    # check request method
    if request.method == 'POST':

        form = EmailForm(request.POST)

        # check if data from the form is clean
        if form.is_valid():
            quiz_link = public_url
            c_d = form.cleaned_data
            subject = c_d['subject']
            message = c_d['message']
            recipient_list = c_d['recipients']

            # send the email to the recipent using the Sendgrid template
            # set up for xperiencedezignwiz
            email_message = EmailMultiAlternatives(from_email=settings
                                                   .DEFAULT_FROM_EMAIL,
                                                   reply_to=['xperience'
                                                             'dezignwiz'
                                                             '@gmail.com'],
                                                   to=['xperiencedezignwiz'
                                                       '@gmail.com'],
                                                   bcc=recipient_list,
                                                   body=message,
                                                   subject=subject)
            email_message.template_id = 'd-9430602ecd0f411f8caa22367da72cbd'
            email_message.dynamic_template_data = {'body': message,
                                                   'body_two': 'Please follow'
                                                   ' the link to complete the'
                                                   ' survey:',
                                                   'body_three': quiz_link,
                                                   'subject': subject}
            email_message.send(fail_silently=False)

            # set the variable initially created to True
            message_sent = True

    else:
        form = EmailForm(initial={'subject': 'XperienceDezignWiz'
                                             ' Survey',
                                             'message': 'You have been sent'
                                             ' a survey to complete.'})

    return render(request, 'survey/email.html', {

        'form': form,
        'message_sent': message_sent,
        'recipient_list': recipient_list,
        'survey': survey,
        'public_url': public_url,

    })


# @login_required checks if the user is logged in to display
# the view, if they are not, they will be required to login
# before they can access the page
@login_required
def create(request):
    """
    User can create a new survey

    request: The requests module allows you to send HTTP
    requests using Python.The HTTP request returns a Response
    Object with all the response data (content, encoding, status, etc).
    Definition from https://www.w3schools.com/python/module_requests.asp

    """
    context = dict(form=SurveyForm())
    if request.method == 'POST':
        # if the request method is equal to post
        # fetch the posted form
        form = SurveyForm(request.POST,
                          initial={'title': 'Add a'
                                   ' Survey Title',
                                   })
        # add the initial text to the title field in the
        # SurveyForm
        context['posted'] = form.instance
        # check if data from the form is clean
        # add creator as user and save
        if form.is_valid():
            survey = form.save(commit=False)
            survey.creator = request.user
            survey.save()
            return redirect('survey-default-options-create', p_k=survey.id)
    else:
        form = SurveyForm(initial={'title': 'Add a'
                                   ' Survey Title', })

    return render(request, 'survey/create.html',
                  {'form': form})


# @login_required checks if the user is logged in to display
# the view, if they are not, they will be required to login
# before they can access the page
@login_required
def delete(request, p_k):
    """
    User can delete an existing survey

    request: The requests module allows you to send HTTP
    requests using Python.The HTTP request returns a Response
    Object with all the response data (content, encoding, status, etc).
    Definition from https://www.w3schools.com/python/module_requests.asp

    pk: Regardless of whether you define a primary key field yourself,
    or let Django supply one for you, each model will have a property
    called pk. It behaves like a normal attribute on the model, but
    is actually an alias for whichever attribute is the primary key field
    for the model. You can read and set this value,
    just as you would for any other attribute,
    and it will update the correct field in the model.
    description from:
    https://www.kite.com/python/docs/django.db.models.Model.pk
    """
    survey = get_object_or_404(Survey, pk=p_k, creator=request.user)
    # fetch the survey if it exists
    if request.method == 'POST':
        # if the request method is post then delete
        survey.delete()

    return redirect('survey-list')


# @login_required checks if the user is logged in to display
# the view, if they are not, they will be required to login
# before they can access the page
@login_required
def edit(request, p_k):
    """
    User can add questions to a draft survey,
    then activate the survey

    request: The requests module allows you to send HTTP
    requests using Python.The HTTP request returns a Response
    Object with all the response data (content, encoding, status, etc).
    Definition from https://www.w3schools.com/python/module_requests.asp

    pk: Regardless of whether you define a primary key field yourself,
    or let Django supply one for you, each model will have a property
    called pk. It behaves like a normal attribute on the model, but
    is actually an alias for whichever attribute is the primary key field
    for the model. You can read and set this value,
    just as you would for any other attribute,
    and it will update the correct field in the model.
    description from:
    https://www.kite.com/python/docs/django.db.models.Model.pk
    """
    try:
        # if the survey and related questions and options
        # created by the logged in user exists and it is
        # still a draft not active, fetch it. If it does
        # not exist raise an http404 error.
        survey = (Survey.objects
                  .prefetch_related('question_set__option_set')
                  .get(pk=p_k, creator=request.user, is_active=False))
        default_options = DefaultOptions.objects.all()
        default_option = get_object_or_404(default_options, survey_id=p_k)
    except Survey.DoesNotExist as survey_no_exist:
        raise Http404() from survey_no_exist

    if request.method == 'POST':
        # if the request method is equal to post
        # set the survey is active to True and
        # save. Redirect to the send-survey-email
        # page
        survey.is_active = True
        survey.save()
        return redirect('send-survey-email', p_k=p_k)
    else:
        questions = survey.question_set.all()
        age_question = default_option.age_question
        gender_question = default_option.gender_question
        industry_question = default_option.industry_question
        # if the request method is not post, return
        # survey edit page, with the questions that
        # the user has already added
        return render(request, 'survey/edit.html',
                      {'survey': survey, 'questions': questions,
                       'age_question': age_question,
                       'gender_question': gender_question,
                       'industry_question': industry_question})


# @login_required checks if the user is logged in to display
# the view, if they are not, they will be required to login
# before they can access the page
@login_required
def default_options_create(request, p_k):
    """
    User can add options to a survey question

    request: The requests module allows you to send HTTP
    requests using Python.The HTTP request returns a Response
    Object with all the response data (content, encoding, status, etc).
    Definition from https://www.w3schools.com/python/module_requests.asp

    pk: Regardless of whether you define a primary key field yourself,
    or let Django supply one for you, each model will have a property
    called pk. It behaves like a normal attribute on the model, but
    is actually an alias for whichever attribute is the primary key field
    for the model. You can read and set this value,
    just as you would for any other attribute,
    and it will update the correct field in the model.
    description from:
    https://www.kite.com/python/docs/django.db.models.Model.pk
    """
    survey = get_object_or_404(Survey, pk=p_k, creator=request.user)
    age_question = get_object_or_404(AgeQuestion)
    gender_question = get_object_or_404(GenderQuestion)
    industry_question = get_object_or_404(IndustryQuestion)
    age_ranges = AgeRange.objects.all()
    genders = Gender.objects.all()
    industries = Industry.objects.all()
    # fetch the survey from the survey model with the matching survey pk
    # and the creator equal to the logged in user
    if request.method == 'POST':
        # if the request method is post
        # fetch the completed OptionForm
        default_options_form = DefaultOptionsForm(request.POST)
        if default_options_form.is_valid():
            default_options = default_options_form.save(commit=False)
            default_options.id = p_k
            default_options.survey_id = p_k
            default_options.age_question_id = age_question.pk
            default_options.gender_question_id = gender_question.pk
            default_options.industry_question_id = industry_question.pk
            default_options.save()
            return redirect("survey-question-create",
                            p_k=p_k)
    else:
        default_options_form = DefaultOptionsForm(request.POST)
    age_ranges = AgeRange.objects.all()
    genders = Gender.objects.all()
    industries = Industry.objects.all()
    return render(
        request,
        'survey/default_options.html',
        {'survey': survey,
         'age_question': age_question, 'gender_question':
         gender_question, 'industry_question': industry_question,
         'age_ranges': age_ranges, 'genders': genders,
         'industries': industries,
         'default_options_form': default_options_form},
    )


# @login_required checks if the user is logged in to display
# the view, if they are not, they will be required to login
# before they can access the page
@login_required
def question_create(request, p_k):
    """
    User can add a question to a draft survey
    Survey: the Survey model
    pk: Regardless of whether you define a primary key field yourself,
    or let Django supply one for you, each model will have a property
    called pk. It behaves like a normal attribute on the model, but
    is actually an alias for whichever attribute is the primary key field
    for the model. You can read and set this value,
    just as you would for any other attribute,
    and it will update the correct field in the model.
    description from:
    https://www.kite.com/python/docs/django.db.models.Model.pk
    creator: request the logged in user details
    """
    survey = get_object_or_404(Survey, pk=p_k, creator=request.user)
    # fetch the survey from the survey model with the matching pk and
    # creator equal to the logged in user
    if request.method == "POST":
        # if request method is equal to post,
        # fetch the completed QuestionForm
        form = QuestionForm(request.POST)
        # if the form is valid save the created
        # question to the survey
        if form.is_valid():
            question = form.save(commit=False)
            question.survey = survey
            question.save()
            # open the page to add options to
            # the created question
            return redirect("survey-option-create",
                            survey_pk=p_k, question_pk=question.pk)
    else:
        form = QuestionForm()

    return render(request, "survey/question.html",
                  {"survey": survey, "form": form})


# @login_required checks if the user is logged in to display
# the view, if they are not, they will be required to login
# before they can access the page
@login_required
def option_create(request, survey_pk, question_pk):
    """
    User can add options to a survey question
    request: The requests module allows you to send HTTP
    requests using Python.The HTTP request returns a Response
    Object with all the response data (content, encoding, status, etc).
    Definition from https://www.w3schools.com/python/module_requests.asp
    pk: Regardless of whether you define a primary key field yourself,
    or let Django supply one for you, each model will have a property
    called pk. It behaves like a normal attribute on the model, but
    is actually an alias for whichever attribute is the primary key field
    for the model. You can read and set this value,
    just as you would for any other attribute,
    and it will update the correct field in the model.
    description from:
    https://www.kite.com/python/docs/django.db.models.Model.pk
    """
    survey = get_object_or_404(Survey, pk=survey_pk, creator=request.user)
    # fetch the survey from the survey model with the matching survey pk
    # and the creator equal to the logged in user
    question = Question.objects.get(pk=question_pk)
    if request.method == "POST":
        # if the request method is post
        # fetch the completed OptionForm
        form = OptionForm(request.POST)
        # if the form is valid save the
        # option to the question
        if form.is_valid():
            option = form.save(commit=False)
            option.question_id = question_pk
            option.save()
    else:
        form = OptionForm()

    options = question.option_set.all()
    return render(
        request,
        "survey/options.html",
        {"survey": survey, "question": question,
         "options": options, "form": form},
    )


def start(request, p_k):
    """
    Survey-taker can start a survey

    request: The requests module allows you to send HTTP
    requests using Python.The HTTP request returns a Response
    Object with all the response data (content, encoding, status, etc).
    Definition from https://www.w3schools.com/python/module_requests.asp

    pk: Regardless of whether you define a primary key field yourself,
    or let Django supply one for you, each model will have a property
    called pk. It behaves like a normal attribute on the model, but
    is actually an alias for whichever attribute is the primary key field
    for the model. You can read and set this value,
    just as you would for any other attribute,
    and it will update the correct field in the model.
    description from:
    https://www.kite.com/python/docs/django.db.models.Model.pk
    """
    survey = get_object_or_404(Survey, pk=p_k, is_active=True)
    # fetch the matching survey from the Survey
    # model, with the equal pk and active set to true
    # if it exists
    if request.method == 'POST':
        # if request method is equal to post
        sub = Submission.objects.create(survey=survey)
        # create the submission object as the survey object
        return redirect('survey-submit',
                        survey_pk=survey.pk, sub_pk=sub.pk)
        # go to the submit default questions page

    return render(request, 'survey/start.html', {'survey': survey})


def submit(request, survey_pk, sub_pk):
    """
    Survey-taker submit their completed survey.

    request: The requests module allows you to send HTTP
    requests using Python.The HTTP request returns a Response
    Object with all the response data (content, encoding, status, etc).
    Definition from https://www.w3schools.com/python/module_requests.asp

    pk: Regardless of whether you define a primary key field yourself,
    or let Django supply one for you, each model will have a property
    called pk. It behaves like a normal attribute on the model, but
    is actually an alias for whichever attribute is the primary key field
    for the model. You can read and set this value,
    just as you would for any other attribute,
    and it will update the correct field in the model.
    description from:
    https://www.kite.com/python/docs/django.db.models.Model.pk
    """
    try:
        survey = (Survey.objects
                  .prefetch_related('question_set__option_set',)
                  .get(pk=survey_pk, is_active=True))
    except Survey.DoesNotExist as survey_no_exist:
        raise Http404() from survey_no_exist

    default_options = DefaultOptions.objects.all()
    default_option = get_object_or_404(default_options, survey_id=survey_pk)
    # Get the survey object related fields question(s) and option(s),
    # pk is equal to the survey pk and it is active if it exists, if not
    #  raise an http404 error

    try:
        sub = survey.submission_set.get(pk=sub_pk, is_complete=False)
    except Survey.DoesNotExist as survey_no_exist:
        raise Http404() from survey_no_exist
        # Get the survey submission with matching pk and complete
        # set to false if it exists, if not raise an http404 error

    questions = survey.question_set.all()
    age_question = default_option.age_question
    gender_question = default_option.gender_question
    industry_question = default_option.industry_question
    # questions is equal to all questions created for
    # a survey
    options = [q.option_set.all() for q in questions]
    # options is equal to all options created for a question
    option_form_kwargs = {'empty_permitted': False, 'options': options}
    # the options can not be submitted as empty i.e. the user has
    # to select an option
    AnswerFormSet = (formset_factory(AnswerForm,
                     extra=len(questions),
                     formset=BaseAnswerFormSet))
    # create the AnswerFormSet by taking the answerform per question and
    # adding it to the BaseAnswerFormSet
    if request.method == 'POST':
        default_answer_form = DefaultAnswerForm(request.POST)
        if default_answer_form.is_valid():
            default_answer = default_answer_form.save(commit=False)
            default_answer.submission_id = sub_pk
            default_answer.survey_id = survey_pk
            default_answer.save()
        # if the request method is post
        # the formset is the completed AnswerFormSet
        # options cannot be empty
        formset = AnswerFormSet(request.POST, form_kwargs=option_form_kwargs)
        if formset.is_valid():
            # for a valid formset
            with transaction.atomic():
                # An operation is atomic if it cannot be interrupted.
                # In Python, these operations are atomic: reading or
                # replacing a single instance attribute. reading or
                # replacing a single global variable.
                # fetching an item from a list.
                # http://larsyencken.github.io/gitbook-mcpy/data_structures/atomic.html
                for form in formset:
                    (Answer.objects
                     .create(option_id=form.cleaned_data['option'],
                             submission_id=sub_pk,))
                    # for every completed form in the formset, create it
                    # as an object in the Answer model
        sub.is_complete = True
        sub.save()
        # mark submission is complete as true and save
        return redirect('survey-thanks', p_k=survey_pk)
        # redirect to the survey thanks page

    else:
        formset = AnswerFormSet(form_kwargs=option_form_kwargs)
        default_answer_form = DefaultAnswerForm()

    question_forms = zip(questions, formset)
    return render(
        request,
        'survey/submit.html',
        {'survey': survey, 'question_forms': question_forms,
         'age_question': age_question,
         'gender_question': gender_question,
         'industry_question': industry_question,
         'formset': formset, 'default_answer_form':
         default_answer_form},
    )


def thanks(request, p_k):
    """
    Survey-taker receives a thank-you message.

    request: The requests module allows you to send HTTP
    requests using Python.The HTTP request returns a Response
    Object with all the response data (content, encoding, status, etc).
    Definition from https://www.w3schools.com/python/module_requests.asp

    pk: Regardless of whether you define a primary key field yourself,
    or let Django supply one for you, each model will have a property
    called pk. It behaves like a normal attribute on the model, but
    is actually an alias for whichever attribute is the primary key field
    for the model. You can read and set this value,
    just as you would for any other attribute,
    and it will update the correct field in the model.
    description from:
    https://www.kite.com/python/docs/django.db.models.Model.pk
    """
    survey = get_object_or_404(Survey, pk=p_k, is_active=True)
    return render(request, 'survey/thanks.html', {'survey': survey})
