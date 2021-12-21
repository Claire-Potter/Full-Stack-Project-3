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
                     GenderQuestion, IndustryQuestion)
from .forms import (SurveyForm, QuestionForm, OptionForm, AnswerForm,
                    BaseAnswerFormSet, EmailForm, AgeForm, GenderForm,
                    IndustryForm)


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
    total_answers_a = (Answer.objects.
                       filter(option_id__in=option_pks).count())
    age_ranges = AgeRange.objects.all()
    age_pks = age_ranges.values_list('pk', flat=True)
    total_answers_a = (Answer.objects.
                       filter(age_range_id__in=age_pks).count())
    for age in age_ranges:
        num_answers = Answer.objects.filter(age_range=age).count()
        # convert to a percentage of total answers
        age.percent = (100.0 * num_answers /
                       total_answers_a if total_answers_a else 0)
    genders = Gender.objects.all()
    gender_pks = genders.values_list('pk', flat=True)
    total_answers_g = (Answer.objects.
                       filter(gender_id__in=gender_pks).count())
    for gender in genders:
        num_answers = Answer.objects.filter(gender=gender).count()
        # convert to a percentage of total answers
        gender.percent = (100.0 * num_answers /
                          total_answers_g if total_answers_g else 0)
    industries = Industry.objects.all()
    industry_pks = industries.values_list('pk', flat=True)
    total_answers_i = (Answer.objects.
                       filter(industry_id__in=industry_pks).count())
    for industry in industries:
        num_answers = Answer.objects.filter(industry=industry).count()
        # convert to a percentage of total answers
        industry.percent = (100.0 * num_answers /
                            total_answers_i if total_answers_i else 0)
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
            'age_ranges': age_ranges,
            'genders': genders,
            'industries': industries,
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
            return redirect('survey-edit', p_k=survey.id)
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
                  .prefetch_related('question_set__option_set',
                                    'agequestion_set__agerange_set',
                                    'genderquestion_set__gender_set',
                                    'industryquestion_set__industry_set')
                  .get(pk=p_k, creator=request.user, is_active=False))
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
        age_question = survey.agequestion_set.all()
        gender_question = survey.genderquestion_set.all()
        industry_question = survey.industryquestion_set.all()
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
    if request.method == 'POST':
        # if request method is equal to post,
        # fetch the completed QuestionForm
        form = QuestionForm(request.POST)
        age_form = AgeForm(request.POST,
                           initial={'age_question':
                                    'Please select your age range:'})
        gender_form = GenderForm(request.POST,
                                 initial={'gender_question':
                                          'Please select your preferred'
                                          ' gender:'})
        industry_form = IndustryForm(request.POST,
                                     initial={'industry_question':
                                              'Please select your'
                                              ' Industry of employment:'})
        # if the form is valid save the created
        # question to the survey
        if form.is_valid():
            question = form.save(commit=False)
            question.survey = survey
            question.save()
        if age_form.is_valid():
            age_question = age_form.save(commit=False)
            age_question.survey = survey
            age_question.save()
        if gender_form.is_valid():
            gender_question = gender_form.save(commit=False)
            gender_question.survey = survey
            gender_question.save()
        if industry_form.is_valid():
            industry_question = industry_form.save(commit=False)
            industry_question.survey = survey
            industry_question.save()
            # open the page to add options to
            # the created question
            return redirect('survey-option-create',
                            survey_pk=p_k, question_pk=question.pk,
                            age_question_pk=age_question.pk,
                            gender_question_pk=gender_question.pk,
                            industry_question_pk=industry_question.pk,)
    else:
        form = QuestionForm()
        age_form = AgeForm(initial={'age_question':
                                    'Please select your age range:'})
        gender_form = GenderForm(initial={'gender_question':
                                          'Please select your preferred'
                                          ' gender:'})
        industry_form = IndustryForm(initial={'industry_question':
                                              'Please select your'
                                              ' Industry of employment:'})

    return render(request, 'survey/question.html',
                  {'survey': survey, 'form': form,
                   'age_form': age_form, 'gender_form':
                   gender_form, 'industry_form':
                   industry_form})


# @login_required checks if the user is logged in to display
# the view, if they are not, they will be required to login
# before they can access the page
@login_required
def option_create(request, survey_pk, question_pk,
                  age_question_pk, gender_question_pk,
                  industry_question_pk):
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
    age_question = AgeQuestion.objects.get(pk=age_question_pk)
    gender_question = GenderQuestion.objects.get(pk=gender_question_pk)
    industry_question = IndustryQuestion.objects.get(pk=industry_question_pk)
    if request.method == 'POST':
        # if the request method is post
        # fetch the completed OptionForm
        age_ranges = AgeRange.objects.all()
        for age_range in age_ranges:
            age_range.age_question_id = age_question_pk
        genders = Gender.objects.all()
        for gender in genders:
            gender.gender_question_id = gender_question_pk
        industries = Industry.objects.all()
        for industry in industries:
            industry.industry_question_id = industry_question_pk
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
    age_ranges = age_question.agerange_set.all()
    genders = gender_question.gender_set.all()
    industries = industry_question.industry_set.all()
    return render(
        request,
        'survey/options.html',
        {'survey': survey, 'question': question,
         'age_question': age_question, 'gender_question':
         gender_question, 'industry_question': industry_question,
         'options': options, 'age_ranges': age_ranges,
         'genders': genders, 'industries': industries, 'form': form},
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
                  .prefetch_related('question_set__option_set',
                                    'agequestion_set__agerange_set',
                                    'genderquestion_set__gender_set',
                                    'industryquestion_set__industry_set')
                  .get(pk=survey_pk, is_active=True))
    except Survey.DoesNotExist as survey_no_exist:
        raise Http404() from survey_no_exist
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
    age_question = survey.agequestion_set.all()
    gender_question = survey.genderquestion_set.all()
    industry_question = survey.industryquestion_set.all()
    # questions is equal to all questions created for
    # a survey
    options = [q.option_set.all() for q in questions]
    age_ranges = [a.agerange_set.all() for a in age_question]
    genders = [g.gender_set.all() for g in gender_question]
    industries = [i.industry_set.all() for i in industry_question]
    # options is equal to all options created for a question
    form_kwargs = {'empty_permitted': False, 'options': options,
                   'age_ranges': age_ranges, 'genders': genders,
                   'industries': industries}
    # the options can not be submitted as empty i.e. the user has
    # to select an option
    AnswerFormSet = (formset_factory(AnswerForm,
                     extra=len(questions, age_question,
                               gender_question, industry_question),
                     formset=BaseAnswerFormSet))
    # create the AnswerFormSet by taking the answerform per question and
    # adding it to the BaseAnswerFormSet
    if request.method == 'POST':
        # if the request method is post
        # the formset is the completed AnswerFormSet
        # options cannot be empty
        formset = AnswerFormSet(request.POST, form_kwargs=form_kwargs)
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
                             age_range_id=form.cleaned_data['age_range'],
                             gender_id=form.cleaned_data['gender'],
                             industry_id=form.cleaned_data['industry'],
                             submission_id=sub_pk,))
                    # for every completed form in the formset, create it
                    # as an object in the Answer model

                sub.is_complete = True
                sub.save()
                # mark submission is complete as true and save
            return redirect('survey-thanks', p_k=survey_pk)
            # redirect to the survey thanks page

    else:
        formset = AnswerFormSet(form_kwargs=form_kwargs)

    question_forms = zip(questions, formset)
    age_question_forms = zip(age_question, formset)
    gender_question_forms = zip(gender_question, formset)
    industry_question_forms = zip(industry_question, formset)
    return render(
        request,
        'survey/submit.html',
        {'survey': survey, 'question_forms': question_forms,
         'age_question_forms': age_question_forms,
         'gender_question_forms': gender_question_forms,
         'industry_question_forms': industry_question_forms,
         'formset': formset},
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
