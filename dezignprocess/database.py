python3 manage.py inspectdb
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AccountEmailaddress(models.Model):
    id = models.BigAutoField(primary_key=True)
    email = models.CharField(unique=True, max_length=254)
    verified = models.BooleanField()
    primary = models.BooleanField()
    user = models.ForeignKey('AuthUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_emailaddress'


class AccountEmailconfirmation(models.Model):
    id = models.BigAutoField(primary_key=True)
    created = models.DateTimeField()
    sent = models.DateTimeField(blank=True, null=True)
    key = models.CharField(unique=True, max_length=64)
    email_address = models.ForeignKey(AccountEmailaddress, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_emailconfirmation'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DezignprocessComment(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=80)
    email = models.CharField(max_length=254)
    body = models.TextField()
    created_on = models.DateTimeField()
    step = models.ForeignKey('DezignprocessStep', models.DO_NOTHING)
    username = models.ForeignKey(AuthUser, models.DO_NOTHING)
    progress_status = models.CharField(max_length=80)

    class Meta:
        managed = False
        db_table = 'dezignprocess_comment'


class DezignprocessProgress(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=80)
    email = models.CharField(max_length=254)
    updated_on = models.DateTimeField()
    progress = models.CharField(max_length=15)
    step = models.ForeignKey('DezignprocessStep', models.DO_NOTHING)
    username = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'dezignprocess_progress'


class DezignprocessStep(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(unique=True, max_length=80)
    slug = models.CharField(unique=True, max_length=80)
    featured_image = models.CharField(max_length=255)
    excerpt = models.TextField()
    order_number = models.IntegerField()
    list_number = models.IntegerField()
    step_image = models.CharField(max_length=255)
    body = models.TextField()
    video_two_url = models.CharField(max_length=200)
    video_name = models.CharField(max_length=80)
    video_url = models.CharField(max_length=200)
    video_three_name = models.CharField(max_length=80)
    resources = models.IntegerField()
    added = models.DateTimeField()
    video_three_url = models.CharField(max_length=200)
    video_two_name = models.CharField(max_length=80)
    tools = models.IntegerField()
    username_id = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'dezignprocess_step'


class DezignprocessTool(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(unique=True, max_length=80)
    slug = models.CharField(max_length=80)
    excerpt = models.TextField()
    body = models.TextField()
    template_image = models.CharField(max_length=255)
    order_number = models.IntegerField()
    step = models.ForeignKey(DezignprocessStep, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'dezignprocess_tool'


class DezignsurveyAnswer(models.Model):
    id = models.BigAutoField(primary_key=True)
    option = models.ForeignKey('DezignsurveyOption', models.DO_NOTHING)
    submit = models.ForeignKey('DezignsurveySubmission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'dezignsurvey_answer'


class DezignsurveyAnswers(models.Model):
    id = models.BigAutoField(primary_key=True)
    options = models.ForeignKey('DezignsurveyOptions', models.DO_NOTHING)
    submit = models.ForeignKey('DezignsurveySubmit', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'dezignsurvey_answers'


class DezignsurveyCustomquestion(models.Model):
    id = models.BigAutoField(primary_key=True)
    prompt = models.CharField(max_length=128)
    survey_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'dezignsurvey_customquestion'


class DezignsurveyOption(models.Model):
    id = models.BigAutoField(primary_key=True)
    text = models.CharField(max_length=128)
    question = models.ForeignKey('DezignsurveyQuestion', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'dezignsurvey_option'


class DezignsurveyOptions(models.Model):
    id = models.BigAutoField(primary_key=True)
    text = models.CharField(max_length=128)
    questions_id = models.BigIntegerField(blank=True, null=True)
    options_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dezignsurvey_options'


class DezignsurveyQuestion(models.Model):
    id = models.BigAutoField(primary_key=True)
    text = models.CharField(max_length=128)
    requires_options = models.BooleanField()
    survey_id = models.CharField(max_length=80)

    class Meta:
        managed = False
        db_table = 'dezignsurvey_question'


class DezignsurveyQuestions(models.Model):
    text = models.CharField(max_length=128)
    survey_id = models.BigIntegerField(blank=True, null=True)
    questions_id = models.IntegerField(primary_key=True)
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'dezignsurvey_questions'


class DezignsurveySubmission(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField()
    is_complete = models.BooleanField()
    survey_id = models.CharField(max_length=80)

    class Meta:
        managed = False
        db_table = 'dezignsurvey_submission'


class DezignsurveySubmit(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField()
    is_complete = models.BooleanField()
    survey_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'dezignsurvey_submit'


class DezigntoolsAgerange(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(unique=True, max_length=80)
    order_number = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'dezigntools_agerange'


class DezigntoolsAnswer(models.Model):
    id = models.BigAutoField(primary_key=True)
    option = models.ForeignKey('DezigntoolsOption', models.DO_NOTHING)
    submission = models.ForeignKey('DezigntoolsSubmission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'dezigntools_answer'


class DezigntoolsDefaultquestions(models.Model):
    id = models.BigAutoField(primary_key=True)
    survey = models.ForeignKey('DezigntoolsSurvey', models.DO_NOTHING)
    age_range = models.ForeignKey(DezigntoolsAgerange, models.DO_NOTHING, blank=True, null=True)
    gender = models.ForeignKey('DezigntoolsGender', models.DO_NOTHING, blank=True, null=True)
    industry = models.CharField(max_length=128, blank=True, null=True)
    job_title = models.CharField(max_length=128, blank=True, null=True)
    name = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'dezigntools_defaultquestions'


class DezigntoolsGender(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(unique=True, max_length=80)
    order_number = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'dezigntools_gender'


class DezigntoolsOption(models.Model):
    id = models.BigAutoField(primary_key=True)
    text = models.CharField(max_length=128)
    question = models.ForeignKey('DezigntoolsQuestion', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'dezigntools_option'


class DezigntoolsQuestion(models.Model):
    id = models.BigAutoField(primary_key=True)
    prompt = models.CharField(max_length=128)
    survey = models.ForeignKey('DezigntoolsSurvey', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'dezigntools_question'


class DezigntoolsSubmission(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField()
    is_complete = models.BooleanField()
    survey = models.ForeignKey('DezigntoolsSurvey', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'dezigntools_submission'


class DezigntoolsSurvey(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=64)
    is_active = models.BooleanField()
    created_at = models.DateTimeField()
    creator = models.ForeignKey(AuthUser, models.DO_NOTHING)
    survey_image = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'dezigntools_survey'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class DjangoSite(models.Model):
    domain = models.CharField(unique=True, max_length=100)
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'django_site'


class DjangoSummernoteAttachment(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    file = models.CharField(max_length=100)
    uploaded = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_summernote_attachment'


class HomeHome(models.Model):
    id = models.BigAutoField(primary_key=True)
    order_number = models.IntegerField()
    username = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'home_home'


class SocialaccountSocialaccount(models.Model):
    id = models.BigAutoField(primary_key=True)
    provider = models.CharField(max_length=30)
    uid = models.CharField(max_length=191)
    last_login = models.DateTimeField()
    date_joined = models.DateTimeField()
    extra_data = models.TextField()
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'socialaccount_socialaccount'
        unique_together = (('provider', 'uid'),)


class SocialaccountSocialapp(models.Model):
    id = models.BigAutoField(primary_key=True)
    provider = models.CharField(max_length=30)
    name = models.CharField(max_length=40)
    client_id = models.CharField(max_length=191)
    secret = models.CharField(max_length=191)
    key = models.CharField(max_length=191)

    class Meta:
        managed = False
        db_table = 'socialaccount_socialapp'


class SocialaccountSocialappSites(models.Model):
    id = models.BigAutoField(primary_key=True)
    socialapp_id = models.BigIntegerField()
    site = models.ForeignKey(DjangoSite, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'socialaccount_socialapp_sites'
        unique_together = (('socialapp_id', 'site'),)


class SocialaccountSocialtoken(models.Model):
    id = models.BigAutoField(primary_key=True)
    token = models.TextField()
    token_secret = models.TextField()
    expires_at = models.DateTimeField(blank=True, null=True)
    account = models.ForeignKey(SocialaccountSocialaccount, models.DO_NOTHING)
    app = models.ForeignKey(SocialaccountSocialapp, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'socialaccount_socialtoken'
        unique_together = (('app', 'account'),)


class SurveyAnswer(models.Model):
    id = models.BigAutoField(primary_key=True)
    created = models.DateTimeField()
    updated = models.DateTimeField()
    question = models.ForeignKey('SurveyQuestion', models.DO_NOTHING)
    response = models.ForeignKey('SurveyResponse', models.DO_NOTHING)
    body = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'survey_answer'


class SurveyCategory(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=400)
    order = models.IntegerField(blank=True, null=True)
    survey = models.ForeignKey('SurveySurvey', models.DO_NOTHING)
    description = models.CharField(max_length=2000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'survey_category'


class SurveyQuestion(models.Model):
    id = models.BigAutoField(primary_key=True)
    text = models.TextField()
    order = models.IntegerField()
    required = models.BooleanField()
    type = models.CharField(max_length=200)
    choices = models.TextField(blank=True, null=True)
    category = models.ForeignKey(SurveyCategory, models.DO_NOTHING, blank=True, null=True)
    survey = models.ForeignKey('SurveySurvey', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'survey_question'


class SurveyResponse(models.Model):
    id = models.BigAutoField(primary_key=True)
    created = models.DateTimeField()
    updated = models.DateTimeField()
    interview_uuid = models.CharField(max_length=36)
    survey = models.ForeignKey('SurveySurvey', models.DO_NOTHING)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'survey_response'


class SurveySurvey(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=400)
    description = models.TextField()
    is_published = models.BooleanField()
    need_logged_user = models.BooleanField()
    template = models.CharField(max_length=255, blank=True, null=True)
    editable_answers = models.BooleanField()
    expire_date = models.DateField()
    publish_date = models.DateField()
    display_method = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'survey_survey'