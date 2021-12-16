from django.db import transaction
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.forms.formsets import formset_factory
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import (Survey, Question, Answer, Submission,
                     DefaultQuestion, AgeRange, Gender, Industry)
from .forms import (SurveyForm, QuestionForm, OptionForm, AnswerForm,
                    BaseAnswerFormSet, DefaultQuestionsAnswerForm, EmailForm)


@login_required
def survey_list(request):
    """User can view all their surveys"""
    surveys = (Survey.objects
               .filter(creator=request.user).order_by("-created_at").all())
    return render(request, "survey/list.html", {"surveys": surveys})


def jls_extract_def(date_dict):
    return date_dict


@login_required
def detail(request, pk):
    """User can view an active survey"""
    try:
        survey = (Survey.objects
                  .prefetch_related("question_set__option_set")
                  .get(pk=pk, creator=request.user, is_active=True))
    except Survey.DoesNotExist:
        raise Http404()

    default_questions = DefaultQuestion.objects.filter(survey=pk)
    total_answers = default_questions.count()
    age_range = AgeRange.objects.all()
    for question in default_questions:
        answer_age_range = question.age_range
        for age in age_range:
            if age == answer_age_range:
                n_o = int(1)
                number_sum = 0
                for num in range(0, n_o+1, 1):
                    sum_total = number_sum+num
                    total_age_number = sum_total
                    age.percent = float(100.0 * total_age_number /
                                        total_answers if total_answers else 0)

    gender_range = Gender.objects.all()
    for question in default_questions:
        answer_gender = question.gender
        for gender in gender_range:
            if gender == answer_gender:
                n_o = int(1)
                number_sum = 0
                for num in range(0, n_o+1, 1):
                    sum_total = number_sum+num
                    total_gender_number = sum_total
                    gender.percent = float(100.0 * total_gender_number /
                                           total_answers if total_answers else 0)
    
    industry_range = Industry.objects.all()
    for question in default_questions:
        answer_industry = question.industry
        for industry in industry_range:
            if industry == answer_industry:
                n_o = int(1)
                number_sum = 0
                for num in range(0, n_o+1, 1):
                    sum_total = number_sum+num
                    total_industry_number = sum_total
                    industry.percent = float(100.0 * total_industry_number /
                                             total_answers if total_answers else 0)

    # Calculate the results.
    # This is a naive implementation and it could be optimised
    #  to hit the database less.
    # See here for more info on how you might improve this code:
    #  https://docs.djangoproject.com/en/3.1/topics/db/aggregation/
    questions = survey.question_set.all()
    for question in questions:
        option_pks = question.option_set.values_list("pk", flat=True)
        total_answers_q = Answer.objects.filter(option_id__in=option_pks).count()
        for option in question.option_set.all():
            num_answers = Answer.objects.filter(option=option).count()
            option.percent = (100.0 * num_answers /
                              total_answers_q if total_answers_q else 0)

    host = request.get_host()
    public_path = reverse("survey-start", args=[pk])
    public_url = f"{request.scheme}://{host}{public_path}"
    num_submissions = survey.submission_set.filter(is_complete=True).count()

    return render(
        request,
        "survey/detail.html",
        {
            "survey": survey,
            "public_url": public_url,
            "questions": questions,
            "num_submissions": num_submissions,
            'default_questions': default_questions,
            'total_answers': total_answers,
            'age_range': age_range,
            'gender_range': gender_range,
            'industry_range': industry_range,
        },
    )


@login_required
def send_email(request, pk):
    try:
        survey = (Survey.objects
                  .prefetch_related("question_set__option_set")
                  .get(pk=pk, creator=request.user, is_active=True))
    except Survey.DoesNotExist:
        raise Http404()

    host = request.get_host()
    public_path = reverse("survey-start", args=[pk])
    public_url = f"{request.scheme}://{host}{public_path}"

    # create a variable to keep track of the form
    message_sent = False
    recipient_list = ""

    # check if form has been submitted
    if request.method == 'POST':

        form = EmailForm(request.POST)

        # check if data from the form is clean
        if form.is_valid():
            quiz_link = public_url
            c_d = form.cleaned_data
            subject = c_d['subject']
            message = c_d['message']
            recipient_list = c_d['recipients'] 

            # send the email to the recipent
            email_message = EmailMultiAlternatives(from_email=settings
                                                   .DEFAULT_FROM_EMAIL,
                                                   reply_to=['xperience'
                                                             'dezignwiz@gmail.com'],
                                                   to=['xperiencedezignwiz@gmail.com'],
                                                   bcc=recipient_list,
                                                   body=message,
                                                   subject=subject)
            email_message.template_id = "d-9430602ecd0f411f8caa22367da72cbd"
            email_message.dynamic_template_data = {"body": message,
                                                   "body_two": "Please follow"
                                                   " the link to complete the"
                                                   " survey:",
                                                   "body_three": quiz_link,
                                                   "subject": subject}
            email_message.send(fail_silently=False)

            # Unsubscribe groups
            # https://sendgrid.com/docs/ui/sending-email/unsubscribe-groups/
            email_message.asm = {'group_id': 138000, 'groups_to_display': [
                       'XperienceDezignWiz']}

            # set the variable initially created to True
            message_sent = True

    else:
        form = EmailForm(initial={'subject': 'XperienceDezignWiz'
                                             ' Survey',
                                             'message': 'You have been sent'
                                             ' a survey to complete.'
                                             ' Please follow this link'
                                             ' to access the survey:'})

    return render(request, 'survey/email.html', {

        'form': form,
        'message_sent': message_sent,
        'recipient_list': recipient_list,
        "survey": survey,
        "public_url": public_url,

    })


@login_required
def create(request):
    """User can create a new survey"""
    context = dict(form=SurveyForm())
    if request.method == "POST":
        form = SurveyForm(request.POST, request.FILES,
                          initial={'title': 'Add a'
                                   ' Survey Title',
                                   'survey_image': 'Upload an image'})
        context['posted'] = form.instance
        if form.is_valid():
            survey = form.save(commit=False)
            survey.creator = request.user
            survey.save()
            return redirect("survey-edit", pk=survey.id)
    else:
        form = SurveyForm(initial={'title': 'Add a'
                                   ' Survey Title',
                                   'survey_image': 'Upload an'
                                   ' image'})

    return render(request, "survey/create.html",
                  {'form': form})


@login_required
def delete(request, pk):
    """User can delete an existing survey"""
    survey = get_object_or_404(Survey, pk=pk, creator=request.user)
    if request.method == "POST":
        survey.delete()

    return redirect("survey-list")


@login_required
def edit(request, pk):
    """User can add questions to a draft survey, then acitvate the survey"""
    try:
        survey = (Survey.objects
                  .prefetch_related("question_set__option_set")
                  .get(pk=pk, creator=request.user, is_active=False))
    except Survey.DoesNotExist:
        raise Http404()

    if request.method == "POST":
        survey.is_active = True
        survey.save()
        return redirect("send-survey-email", pk=pk)
    else:
        questions = survey.question_set.all()
        return render(request, "survey/edit.html",
                      {"survey": survey, "questions": questions})


@login_required
def question_create(request, pk):
    """User can add a question to a draft survey"""
    survey = get_object_or_404(Survey, pk=pk, creator=request.user)
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.survey = survey
            question.save()
            return redirect("survey-option-create",
                            survey_pk=pk, question_pk=question.pk)
    else:
        form = QuestionForm()

    return render(request, "survey/question.html",
                  {"survey": survey, "form": form})


@login_required
def option_create(request, survey_pk, question_pk):
    """User can add options to a survey question"""
    survey = get_object_or_404(Survey, pk=survey_pk, creator=request.user)
    question = Question.objects.get(pk=question_pk)
    if request.method == "POST":
        form = OptionForm(request.POST)
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


def start(request, pk):
    """Survey-taker can start a survey"""
    survey = get_object_or_404(Survey, pk=pk, is_active=True)
    if request.method == "POST":
        sub = Submission.objects.create(survey=survey)
        return redirect("submit-default", survey_pk=pk, sub_pk=sub.pk)

    return render(request, "survey/start.html", {"survey": survey})


def submit_default(request, survey_pk, sub_pk):
    """Survey-taker submit their completed survey."""
    try:
        survey = Survey.objects.prefetch_related("defaultquestions_set").get(
            pk=survey_pk, is_active=True
        )
    except Survey.DoesNotExist:
        raise Http404()

    try:
        sub = survey.submission_set.get(pk=sub_pk, is_complete=False)
    except Submission.DoesNotExist:
        raise Http404()

    if request.method == "POST":
        form = DefaultQuestionsAnswerForm(request.POST)
        if form.is_valid():
            form.instance.email = request.user.email
            form.instance.name = request.user.username
            question = form.save(commit=False)
            question.survey = survey
            question.save()
            sub.is_complete = False
            sub.save()
            return redirect("survey-submit",
                            survey_pk=survey.pk, sub_pk=sub.pk)

    else:
        form = DefaultQuestionsAnswerForm(request.POST)

    return render(
        request,
        "survey/default_submit.html",
        {"survey": survey, "form": form},
    )


def submit(request, survey_pk, sub_pk):
    """Survey-taker submit their completed survey."""
    try:
        survey = (Survey.objects
                  .prefetch_related("question_set__option_set")
                  .get(pk=survey_pk, is_active=True))
    except Survey.DoesNotExist:
        raise Http404()

    try:
        sub = survey.submission_set.get(pk=sub_pk, is_complete=False)
    except Submission.DoesNotExist:
        raise Http404()

    questions = survey.question_set.all()
    options = [q.option_set.all() for q in questions]
    form_kwargs = {"empty_permitted": False, "options": options}
    AnswerFormSet = (formset_factory(AnswerForm,
                     extra=len(questions), formset=BaseAnswerFormSet))
    if request.method == "POST":
        formset = AnswerFormSet(request.POST, form_kwargs=form_kwargs)
        if formset.is_valid():
            with transaction.atomic():
                for form in formset:
                    (Answer.objects
                     .create(option_id=form.cleaned_data["option"],
                             submission_id=sub_pk,))

                sub.is_complete = True
                sub.save()
            return redirect("survey-thanks", pk=survey_pk)

    else:
        formset = AnswerFormSet(form_kwargs=form_kwargs)

    question_forms = zip(questions, formset)
    return render(
        request,
        "survey/submit.html",
        {"survey": survey, "question_forms": question_forms,
         "formset": formset},
    )


def thanks(request, pk):
    """Survey-taker receives a thank-you message."""
    survey = get_object_or_404(Survey, pk=pk, is_active=True)
    return render(request, "survey/thanks.html", {"survey": survey})
