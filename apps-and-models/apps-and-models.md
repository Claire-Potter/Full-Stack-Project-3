# Django Apps and Models

All Apps and Models for XperienceDezignWiz project.

The XperienceDezignWiz project is created utilising three separate Apps.

<!-- Start Document Outline -->

* [Home App](#home-app)
	* [1. The Home Model](#1-the-home-model)
	* [2. The Contact Model](#2-the-contact-model)
	* [3. The Verification Model](#3-the-verification-model)
* [DezignProcess App](#dezignprocess-app)
	* [1. The Step Model](#1-the-step-model)
	* [2. The Images Model](#2-the-images-model)
	* [3. The Resource Model](#3-the-resource-model)
	* [4. The Tool Model](#4-the-tool-model)
	* [5. The Progress Model](#5-the-progress-model)
	* [6. The Comment Model](#6-the-comment-model)
* [DezignTools App](#dezigntools-app)
	* [1. The Survey Model](#1-the-survey-model)
	* [2. The Gender Model](#2-the-gender-model)
	* [3. The AgeRange Model](#3-the-agerange-model)
	* [4. The Industry Model](#4-the-industry-model)
	* [5. The Age Question Model](#5-the-age-question-model)
	* [6. The Gender Question Model](#6-the-gender-question-model)
	* [7. The Industry Question Model](#7-the-industry-question-model)
	* [8. The DefaultOptions Model](#8-the-defaultoptions-model)
	* [9. The Question Model](#9-the-question-model)
	* [10. The Option Model](#10-the-option-model)
	* [11. The Submission Model](#11-the-submission-model)
	* [12. The Answer Model](#12-the-answer-model)
	* [13. The Default Answer Model](#13-the-default-answer-model)

<!-- End Document Outline -->

## Home App
The Home App is utilised to house:

### 1. The Home Model
Utilised to store the home image and create the Home page view using the template index.html.

| Key | Name       | Type                    | Explanation                                                                                                               |
|-----|------------|-------------------------|---------------------------------------------------------------------------------------------------------------------------|
|     | id<br>     | BigAutoField            | It is a 64-bit integer, much like an AutoField except that it is guaranteed to fit numbers from 1 to 9223372036854775807. |
|     | created_on | DateTimeField           | A date, represented in Python by a datetime.date instance                                                                 |
|     | home_image | CloudinaryField(image)  |  A field to select the image file to be uploaded to Cloudinary storage.
|            | deletable | BooleanField(default=False)                  | A true/false field. <br>The default form widget for this field is a CheckboxInput.                                               |


### 2. The Contact Model
Utilised to store the contact request data and create the Contact us page view using the template contact.html.

| Key        | Name       | Type                                                                | Explanation                                                                                                                       |
|------------|------------|---------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
|            | id<br>     | BigAutoField                                                        | It is a 64-bit integer, much like an AutoField except that it is guaranteed to fit numbers from 1 to 9223372036854775807.         |
| ForeignKey | username   | ForeignKey(User, on_delete=models.CASCADE,  related_name='contact') |  A many-to-one relationship. Requires two positional arguments: the class to which the model is related and the on_delete option. |
|            | body       | TextField                                                           | 	A large text field. The default form widget for this field is a Textarea.                                                        |
|            | created_on | DateTimeField                                                       | A date, represented in Python by a datetime.date instance                                                                         |
|            | email      | EmailField                                                          | It is a CharField that checks that the value is a valid email address.                                                            |
|            | name       | CharField(max_length80)                                             | A field to store text based values.                                                                                               |
|            | deletable | BooleanField(default=False)                  | A true/false field. <br>The default form widget for this field is a CheckboxInput.                                               |

### 3. The Verification Model
Utilised to store the verification code for google cloud. Google cloud is utilised to create the Sendgrid Email account. The verification code is read by google to verify the site domain.

| Key | Name         | Type                     | Explanation                                                                                                               |
|-----|--------------|--------------------------|---------------------------------------------------------------------------------------------------------------------------|
|     | id<br>       | BigAutoField             | It is a 64-bit integer, much like an AutoField except that it is guaranteed to fit numbers from 1 to 9223372036854775807. |
|     | updated_on   | DateTimeField            | A date, represented in Python by a datetime.date instance                                                                 |
|     | verification | CharField(max_length250) | A field to store text based values.                                                                                       |
|            | deletable | BooleanField(default=False)                  | A true/false field. <br>The default form widget for this field is a CheckboxInput.                                               |

## DezignProcess App
The DezignProcess App is utilised to house the data for the Design Thinking steps and views for the relevant templates:

### 1. The Step Model
Utilised to store the Design Thinking Steps data, and create the various views required.

| Key             | Name          | Type                                                                        | Explanation                                                                                                                                                                                               |
|-----------------|---------------|-----------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                 | id<br>        | BigAutoField                                                                | It is a 64-bit integer, much like an AutoField except that it is guaranteed to fit numbers from 1 to 9223372036854775807.                                                                                 |
| ForeignKey      | feature_image | ForeignKey(Images, on_delete=models.CASCADE, related_name='featured_image',<br>        default='1') | A many-to-one relationship. Requires two positional arguments: the class to which the model is related and the on_delete option.                                                                          |
| ForeignKey      | steps_image   | ForeignKey(Images, on_delete=models.CASCADE, related_name='step_image',<br>        default='1') | A many-to-one relationship. Requires two positional arguments: the class to which the model is related and the on_delete option.                                                                          |
| ManyToManyField | resources     | ManyToManyField(<br>        Resource, related_name='resource', blank=True)  | A many-to-many relationship. Requires a positional argument: the class to which the model is related, which works exactly the same as it does for ForeignKey, including recursive and lazy relationships. |
| ManyToManyField | tools         | ManyToManyField(<br>        Tool, related_name='tool', blank=True)          | A many-to-many relationship. Requires a positional argument: the class to which the model is related, which works exactly the same as it does for ForeignKey, including recursive and lazy relationships. |
|                 | added         | DateTimeField                                                               | A date, represented in Python by a datetime.date instance                                                                                                                                                 |
|                 | body          | TextField                                                                   | A large text field. The default form widget for this field is a Textarea.                                                                                                                                 |
|                 | excerpt       | TextField                                                                   | A large text field. The default form widget for this field is a Textarea.                                                                                                                                 |
|                 | list_number   | IntegerField                                                                | It is an integer field. Values from -2147483648 to 2147483647 are safe in all databases supported by Django.                                                                                              |
|                 | order_number  | IntegerField                                                                | It is an integer field. Values from -2147483648 to 2147483647 are safe in all databases supported by Django.                                                                                              |
|                 | slug          | SlugField                                                                   | Slug is a newspaper term. A slug is a short label for something, containing only letters, numbers, underscores or hyphens. They’re generally used in URLs.                                                |
|                 | title         | CharField(max_length80)                                                     | A field to store text based values.                                                                                                                                                                       |
|            | deletable | BooleanField(default=False)                  | A true/false field. <br>The default form widget for this field is a CheckboxInput.                                               |



### 2. The Images Model
Utilised to store the images utilised throughout the Steps templates.

| Key | Name         | Type                                                    | Explanation                                                                                                                      |
|-----|--------------|---------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
|     | id<br>       | BigAutoField                                            | It is a 64-bit integer, much like an AutoField except that it is guaranteed to fit numbers from 1 to 9223372036854775807.        |
|     | added        | DateTimeField                                           | A date, represented in Python by a datetime.date instance                                                                        |
|     | category     | CharField(max_length=15, choices=ImageCategory.choices,<br>                                default=ImageCategory.OTHER,) | A many-to-one relationship. Requires two positional arguments: the class to which the model is related and the on_delete option. |
|     | image        | CloudinaryField(image)                                  | A field to select the image file to be uploaded to Cloudinary storage.                                                           |
|     | name         | CharField(max_length100)                                | A field to store text based values.                                                                                              |
|     | order_number | IntegerField                                            | It is an integer field. Values from -2147483648 to 2147483647 are safe in all databases supported by Django.                     |
|     | title        | CharField(max_length100)                                | A field to store text based values.                                                                                              |
|            | deletable | BooleanField(default=False)                  | A true/false field. <br>The default form widget for this field is a CheckboxInput.                                               |

### 3. The Resource Model
Utilised to store the videos displayed within the resources section on the step detail page.

| Key | Name         | Type                     | Explanation                                                                                                               |
|-----|--------------|--------------------------|---------------------------------------------------------------------------------------------------------------------------|
|     | id<br>       | BigAutoField             | It is a 64-bit integer, much like an AutoField except that it is guaranteed to fit numbers from 1 to 9223372036854775807. |
|     | added        | DateTimeField            | A date, represented in Python by a datetime.date instance                                                                 |
|     | order_number | IntegerField             | It is an integer field. Values from -2147483648 to 2147483647 are safe in all databases supported by Django.              |
|     | video_name   | CharField(max_length100) | A field to store text based values.                                                                                       |
|     | video_url    | EmbedVideoField          | A field to store the video url utilising the django library django-embed-video                                            |
|            | deletable | BooleanField(default=False)                  | A true/false field. <br>The default form widget for this field is a CheckboxInput.                                               |

### 4. The Tool Model
Utilised to store the data and create the view using the step_tool.html template.

| Key        | Name         | Type                                                                    | Explanation                                                                                                                                                |
|------------|--------------|-------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
|            | id<br>       | BigAutoField                                                            | It is a 64-bit integer, much like an AutoField except that it is guaranteed to fit numbers from 1 to 9223372036854775807.                                  |
| ForeignKey | image        | ForeignKey(Images, on_delete=models.CASCADE, related_name='tool_image',<br>        default='1') | A many-to-one relationship. Requires two positional arguments: the class to which the model is related and the on_delete option.                           |
|            | body         | TextField                                                               | A large text field. The default form widget for this field is a Textarea.                                                                                  |
|            | excerpt      | TextField                                                               | A large text field. The default form widget for this field is a Textarea.                                                                                  |
|            | order_number | IntegerField                                                            | It is an integer field. Values from -2147483648 to 2147483647 are safe in all databases supported by Django.                                               |
|            | slug         | SlugField                                                               | Slug is a newspaper term. A slug is a short label for something, containing only letters, numbers, underscores or hyphens. They’re generally used in URLs. |
|            | title        | CharField(max_length80)                                                 | A field to store text based values.                                                                                                                        |
|            | deletable | BooleanField(default=False)                  | A true/false field. <br>The default form widget for this field is a CheckboxInput.                                               |

### 5. The Progress Model
Utilised to store the progress updated status created by the user on the step detail page.

| Key        | Name       | Type                                                                | Explanation                                                                                                                      |
|------------|------------|---------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
|            | id<br>     | BigAutoField                                                        | It is a 64-bit integer, much like an AutoField except that it is guaranteed to fit numbers from 1 to 9223372036854775807.        |
| ForeignKey | step       | ForeignKey(Step, on_delete=models.CASCADE, related_name='progress',<br>        default='1') | A many-to-one relationship. Requires two positional arguments: the class to which the model is related and the on_delete option. |
| ForeignKey | username   | ForeignKey(User, on_delete=models.CASCADE, related_name='progress',<br>        default='1') | A many-to-one relationship. Requires two positional arguments: the class to which the model is related and the on_delete option. |
|            | email      | EmailField                                                          | It is a CharField that checks that the value is a valid email address.                                                           |
|            | name       | CharField(max_length80)                                             | A field to store text based values.                                                                                              |
|            | progress   | CharField(max_length=15, choices=ProgressStatus.choices,<br>                                default=ProgressStatus.NOT_STARTED,) | A field to store text based values.                                                                                              |
|            | updated_on | DateTimeField                                                       | 	A date, represented in Python by a datetime.date instance                                                                       |
|            | deletable | BooleanField(default=False)                  | A true/false field. <br>The default form widget for this field is a CheckboxInput.                                               |
### 6. The Comment Model
Utilised to store the updated comments created by the user on the step detail page.

| Key        | Name       | Type                                                                | Explanation                                                                                                                      |
|------------|------------|---------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
|            | id<br>     | BigAutoField                                                        | It is a 64-bit integer, much like an AutoField except that it is guaranteed to fit numbers from 1 to 9223372036854775807.        |
| ForeignKey | step       | ForeignKey(Step, on_delete=models.CASCADE, related_name='comments',<br>        default='1') | A many-to-one relationship. Requires two positional arguments: the class to which the model is related and the on_delete option. |
| ForeignKey | username   | ForeignKey(User, on_delete=models.CASCADE, related_name='comments',<br>        default='1') | A many-to-one relationship. Requires two positional arguments: the class to which the model is related and the on_delete option. |
|            | email      | EmailField                                                          | It is a CharField that checks that the value is a valid email address.                                                           |
|            | name       | CharField(max_length80)                                             | A field to store text based values.                                                                                              |
|            | body       | TextField                                                           | A large text field. The default form widget for this field is a Textarea.                                                        |
|            | created_on | DateTimeField                                                       | A date, represented in Python by a datetime.date instance                                                                        |
|            | deletable | BooleanField(default=False)                  | A true/false field. <br>The default form widget for this field is a CheckboxInput.                                               |

## DezignTools App
The DezignTools App is utilised to house the data for the Survey functionality and views for the relevant templates:

### 1. The Survey Model
Utilised to store the Survey data and create the required views.

| Key        | Name         | Type                                                               | Explanation                                                                                                                                                |
|------------|--------------|--------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
|            | id<br>       | BigAutoField                                                       | It is a 64-bit integer, much like an AutoField except that it is guaranteed to fit numbers from 1 to 9223372036854775807.                                  |
| ForeignKey | creator      | ForeignKey(User, on_delete=models.CASCADE, related_name='creator',<br>        default='1') | A many-to-one relationship. Requires two positional arguments: the class to which the model is related and the on_delete option.                           |
|            | created_at   | DateTimeField                                                      | A date, represented in Python by a datetime.date instance                                                                                                  |
|            | excerpt      | TextField                                                          | A large text field. The default form widget for this field is a Textarea.                                                                                  |
|            | is_active    | BooleanField                                                       | 	A true/false field. <br>The default form widget for this field is a CheckboxInput.                                                                        |
|            | survey_image | CloudinaryField(image)                                             | A field to select the image file to be uploaded to Cloudinary storage. |
|            | title        | CharField(max_length80)                                            | A field to store text based values.                                                                                                                        |
|            | deletable | BooleanField(default=False)                  | A true/false field. <br>The default form widget for this field is a CheckboxInput.                                               |

### 2. The Gender Model
Utilised to store the gender data which populates the option selection for the gender default question added to all surveys.

| Key | Name         | Type                    | Explanation                                                                                                               |
|-----|--------------|-------------------------|---------------------------------------------------------------------------------------------------------------------------|
|     | id<br>       | BigAutoField            | It is a 64-bit integer, much like an AutoField except that it is guaranteed to fit numbers from 1 to 9223372036854775807. |
|     | name         | CharField(max_length80) | A field to store text based values.                                                                                       |
|     | order_number | IntegerField            | 	It is an integer field. Values from -2147483648 to 2147483647 are safe in all databases supported by Django.             |
|            | deletable | BooleanField(default=False)                  | A true/false field. <br>The default form widget for this field is a CheckboxInput.                                               |


### 3. The AgeRange Model
Utilised to store the age range data which populates the option selection for the age range default question added to all surveys.

| Key | Name         | Type                    | Explanation                                                                                                               |
|-----|--------------|-------------------------|---------------------------------------------------------------------------------------------------------------------------|
|     | id<br>       | BigAutoField            | It is a 64-bit integer, much like an AutoField except that it is guaranteed to fit numbers from 1 to 9223372036854775807. |
|     | name         | CharField(max_length80) | A field to store text based values.                                                                                       |
|     | order_number | IntegerField            | It is an integer field. Values from -2147483648 to 2147483647 are safe in all databases supported by Django.              |
|            | deletable | BooleanField(default=False)                  | A true/false field. <br>The default form widget for this field is a CheckboxInput.                                               |


### 4. The Industry Model
Utilised to store the industry data which populates the option selection for the industry default question added to all surveys.

| Key | Name  | Type                    | Explanation                                                                                                               |
|-----|-------|-------------------------|---------------------------------------------------------------------------------------------------------------------------|
|     | id<br> | BigAutoField            | It is a 64-bit integer, much like an AutoField except that it is guaranteed to fit numbers from 1 to 9223372036854775807. |
|     | title | CharField(max_length80) | A field to store text based values.                                                                                       |
|            | deletable | BooleanField(default=False)                  | A true/false field. <br>The default form widget for this field is a CheckboxInput.                                               |

### 5. The Age Question Model
Utilised to store the age question which
is the default question about age range. 

| Key | Name         | Type                        | Explanation                                                                                                               |
|-----|--------------|-----------------------------|---------------------------------------------------------------------------------------------------------------------------|
|     | id<br>       | BigAutoField                | It is a 64-bit integer, much like an AutoField except that it is guaranteed to fit numbers from 1 to 9223372036854775807. |
|     | age_question | CharField(max_length80)     | A field to store text based values.                                                                                       |
|     | deletable    | BooleanField(default=False) |   A true/false field. <br>The default form widget for this field is a CheckboxInput.                                                                                                                        |

### 6. The Gender Question Model
Utilised to store the gender question which
is the default question about gender. 

| Key | Name            | Type                        | Explanation                                                                                                               |
|-----|-----------------|-----------------------------|---------------------------------------------------------------------------------------------------------------------------|
|     | id<br>          | BigAutoField                | It is a 64-bit integer, much like an AutoField except that it is guaranteed to fit numbers from 1 to 9223372036854775807. |
|     | gender_question | CharField(max_length80)     | A field to store text based values.                                                                                       |
|     | deletable       | BooleanField(default=False) | A true/false field. <br>The default form widget for this field is a CheckboxInput.                                        |


### 7. The Industry Question Model
Utilised to store the industry question which
is the default question about industry.

| Key | Name              | Type                        | Explanation                                                                                                               |
|-----|-------------------|-----------------------------|---------------------------------------------------------------------------------------------------------------------------|
|     | id<br>            | BigAutoField                | It is a 64-bit integer, much like an AutoField except that it is guaranteed to fit numbers from 1 to 9223372036854775807. |
|     | industry_question | CharField(max_length80)     | A field to store text based values.                                                                                       |
|     | deletable         | BooleanField(default=False) | A true/false field. <br>The default form widget for this field is a CheckboxInput.                                        |


### 8. The DefaultOptions Model
Utilised to store the Default Question and Options selections users make when answering a survey.

| Key        | Name              | Type                                                                                     | Explanation                                                                                                                                                                                              |
|------------|-------------------|------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|            | id<br>            | BigAutoField                                                                             | It is a 64-bit integer, much like an AutoField except that it is guaranteed to fit numbers from 1 to 9223372036854775807.                                                                                |
| ForeignKey | survey            | ForeignKey(Survey, on_delete=models.CASCADE, related_name='defaultquestions_set',<br>        default='1') | A many-to-one relationship. Requires two positional arguments: the class to which the model is related and the on_delete option.                                                                         |
| ForeignKey | age_question      | ForeignKey(Survey, on_delete=models.CASCADE, related_name='defaultquestions_set',<br>        default='1') | A many-to-one relationship. Requires two positional arguments: the class to which the model is related and the on_delete option.                                                                         |
| ForeignKey | gender_question   | ForeignKey(Survey, on_delete=models.CASCADE, related_name='defaultquestions_set',<br>        default='1') | A many-to-one relationship. Requires two positional arguments: the class to which the model is related and the on_delete option.                                                                         |
| ForeignKey | industry_question | ForeignKey(Survey, on_delete=models.CASCADE, related_name='defaultquestions_set',<br>        default='1') | A many-to-one relationship. Requires two positional arguments: the class to which the model is related and the on_delete option.                                                                         |
| ManytoMany | age_range         | ManytoManyRelationship(AgeRange, on_delete=models.CASCADE, related_name='age_range_set',<br>        default='1') | A many-to-many relationship. Requires a positional argument: the class to which the model is related, which works exactly the same as it does for ForeignKey, including recursive and lazy relationships |
| ManytoMany | gender            | ManytoManyRelationship(Gender, on_delete=models.CASCADE, related_name='gender_set',<br>        default='1') | A many-to-many relationship. Requires a positional argument: the class to which the model is related, which works exactly the same as it does for ForeignKey, including recursive and lazy relationships |
| ManytoMany | industry          | ManytoManyRelationship(Industry, on_delete=models.CASCADE, related_name='industry_set',<br>        default='1') | A many-to-many relationship. Requires a positional argument: the class to which the model is related, which works exactly the same as it does for ForeignKey, including recursive and lazy relationships |
|            | deletable         | BooleanField(default=True)                                                               | 	A true/false field. <br>The default form widget for this field is a CheckboxInput.                                                                                                                      |
|            | active            | BooleanField(default=False)                                                              | 	A true/false field. <br>The default form widget for this field is a CheckboxInput.                                                                                                                      |


### 9. The Question Model
Utilised to store the Question data which users create and add to their individual surveys.

| Key        | Name      | Type                                         | Explanation                                                                                                                      |
|------------|-----------|----------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
|            | id<br>    | BigAutoField                                 | It is a 64-bit integer, much like an AutoField except that it is guaranteed to fit numbers from 1 to 9223372036854775807.        |
| ForeignKey | survey    | ForeignKey(Survey, on_delete=models.CASCADE) | A many-to-one relationship. Requires two positional arguments: the class to which the model is related and the on_delete option. |
|            | question  | CharField(max_length128)                     | A field to store text based values.                                                                                              |
|            | deletable | BooleanField(default=False)                  | A true/false field. <br>The default form widget for this field is a CheckboxInput.                                               |


### 10. The Option Model
Utilised to store the Option data which users create and add to their individual questions created within their surveys.

| Key        | Name     | Type                                           | Explanation                                                                                                                      |
|------------|----------|------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
|            | id<br>   | BigAutoField                                   | It is a 64-bit integer, much like an AutoField except that it is guaranteed to fit numbers from 1 to 9223372036854775807.        |
| ForeignKey | question | ForeignKey(Question, on_delete=models.CASCADE) | A many-to-one relationship. Requires two positional arguments: the class to which the model is related and the on_delete option. |
|            | option   | CharField(max_length128)                       | A field to store text based values.                                                                                              |
|            | deletable | BooleanField(default=False)                  | A true/false field. <br>The default form widget for this field is a CheckboxInput.                                               |

### 11. The Submission Model
Utilised to store the survey submission created by users.

| Key        | Name        | Type                                         | Explanation                                                                                                                      |
|------------|-------------|----------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
|            | id<br>      | BigAutoField                                 | It is a 64-bit integer, much like an AutoField except that it is guaranteed to fit numbers from 1 to 9223372036854775807.        |
| ForeignKey | survey      | ForeignKey(Survey, on_delete=models.CASCADE) | A many-to-one relationship. Requires two positional arguments: the class to which the model is related and the on_delete option. |
|            | created_at  | DateTimeField                                | A date, represented in Python by a datetime.date instance                                                                        |
|            | is_complete | BooleanField                                 | A true/false field. <br>The default form widget for this field is a CheckboxInput.                                               |
|            | deletable | BooleanField(default=False)                  | A true/false field. <br>The default form widget for this field is a CheckboxInput.                                               |
### 12. The Answer Model
Utilised to store the survey submission and options selected by the user.

| Key        | Name       | Type                                             | Explanation                                                                                                                      |
|------------|------------|--------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
|            | id<br>     | BigAutoField                                     | It is a 64-bit integer, much like an AutoField except that it is guaranteed to fit numbers from 1 to 9223372036854775807.        |
| ForeignKey | submission | ForeignKey(Submission, on_delete=models.CASCADE) | A many-to-one relationship. Requires two positional arguments: the class to which the model is related and the on_delete option. |
| ForeignKey | option     | ForeignKey(Option, on_delete=models.CASCADE)     | A many-to-one relationship. Requires two positional arguments: the class to which the model is related and the on_delete option. |
|            | deletable | BooleanField(default=False)                  | A true/false field. <br>The default form widget for this field is a CheckboxInput.                                               |

### 13. The Default Answer Model
Utilised to store the default answers selected by the user.

| Key        | Name       | Type                                             | Explanation                                                                                                                      |
|------------|------------|--------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
|            | id<br>     | BigAutoField                                     | It is a 64-bit integer, much like an AutoField except that it is guaranteed to fit numbers from 1 to 9223372036854775807.        |
| ForeignKey | submission | ForeignKey(Submission, on_delete=models.CASCADE) | A many-to-one relationship. Requires two positional arguments: the class to which the model is related and the on_delete option. |
| ForeignKey | survey     | ForeignKey(Option, on_delete=models.CASCADE)     | A many-to-one relationship. Requires two positional arguments: the class to which the model is related and the on_delete option. |
| ForeignKey | age_range  | ForeignKey(AgeRange, on_delete=models.CASCADE)   | A many-to-one relationship. Requires two positional arguments: the class to which the model is related and the on_delete option. |
| ForeignKey | gender     | ForeignKey(Gender, on_delete=models.CASCADE)     | A many-to-one relationship. Requires two positional arguments: the class to which the model is related and the on_delete option. |
| ForeignKey | industry   | ForeignKey(Industry, on_delete=models.CASCADE)   | A many-to-one relationship. Requires two positional arguments: the class to which the model is related and the on_delete option. |
|            | deletable  | BooleanField(default=True)                       | A true/false field. <br>The default form widget for this field is a CheckboxInput.                                               |

















