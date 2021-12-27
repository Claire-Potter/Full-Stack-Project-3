# Features

<!-- Start Document Outline -->

* [Navigation](#navigation)
	* [Desktop site:](#desktop-site)
	* [Mobile Site](#mobile-site)
	* [Desktop Site:](#desktop-site-1)
	* [Mobile Site:](#mobile-site-1)
	* [Links:](#links)
	* [Dropdown Menu](#dropdown-menu)
		* [Dropdown Desktop:](#dropdown-desktop)
		* [Dropdown Mobile:](#dropdown-mobile)
* [The Home Page](#the-home-page)
	* [Desktop Site](#desktop-site-2)
	* [Mobile Site](#mobile-site-2)
* [The Footer](#the-footer)
	* [Desktop Site](#desktop-site-3)
	* [Mobile Site](#mobile-site-3)
* [Steps One to Three and Steps Four to Seven](#steps-one-to-three-and-steps-four-to-seven)
	* [Desktop Site](#desktop-site-4)
	* [Mobile Site](#mobile-site-4)
	* [Steps Navigation](#steps-navigation)
		* [Steps Navigation](#steps-navigation-1)
		* [Steps Button](#steps-button)
		* [Steps Button](#steps-button-1)
* [Step Detail](#step-detail)
	* [Desktop Site](#desktop-site-5)
	* [Mobile Site](#mobile-site-5)
	* [Resources](#resources)
	* [Desktop Site](#desktop-site-6)
	* [Mobile Site](#mobile-site-6)
	* [Tools](#tools)
	* [Desktop Site](#desktop-site-7)
	* [Mobile Site](#mobile-site-7)
	* [Step Progress](#step-progress)
	* [Step Progress Status Desktop](#step-progress-status-desktop)
	* [Progress Form Mobile](#progress-form-mobile)
	* [Progress Status Updated](#progress-status-updated)
	* [Progress Status Section if not logged in](#progress-status-section-if-not-logged-in)
	* [Comments](#comments)
	* [Comments Form Mobile](#comments-form-mobile)
	* [Comments Updated](#comments-updated)
* [Step Tools](#step-tools)
	* [Desktop site](#desktop-site-8)
	* [Mobile Site](#mobile-site-8)
* [Survey - from Empathy Step](#survey---from-empathy-step)
	* [Survey from Empathy Step](#survey-from-empathy-step)
* [Survey - List](#survey---list)
	* [Desktop Site](#desktop-site-9)
	* [Mobile Site](#mobile-site-9)
	* [Survey List - No Surveys](#survey-list---no-surveys)
	* [Survey Create](#survey-create)
	* [Desktop Site](#desktop-site-10)
	* [Mobile Site](#mobile-site-10)
* [Survey Default Questions](#survey-default-questions)
	* [Desktop Site](#desktop-site-11)
	* [Mobile Site](#mobile-site-11)
* [Survey - Add Questions and Options](#survey---add-questions-and-options)
	* [Desktop Site](#desktop-site-12)
	* [Mobile Site](#mobile-site-12)
	* [Cancel Add Question](#cancel-add-question)
	* [Desktop Site](#desktop-site-13)
	* [Mobile Site](#mobile-site-13)
	* [Create Second Option](#create-second-option)
	* [Activate Survey](#activate-survey)
* [Send Survey](#send-survey)
	* [Desktop Site](#desktop-site-14)
	* [Mobile Site](#mobile-site-14)
	* [Email Sent message](#email-sent-message)
	* [Email Delivered](#email-delivered)
* [Start Survey](#start-survey)
	* [Desktop Site](#desktop-site-15)
	* [Mobile Site](#mobile-site-15)
* [Complete and Submit Survey](#complete-and-submit-survey)
	* [Desktop Site](#desktop-site-16)
	* [Mobile Site](#mobile-site-16)
	* [Answer Required](#answer-required)
	* [Thank you message](#thank-you-message)
* [Survey Details - Results](#survey-details---results)
	* [Desktop Site](#desktop-site-17)
	* [Mobile Site](#mobile-site-17)
	* [Delete Survey](#delete-survey)
* [Search for a Step](#search-for-a-step)
	* [Desktop Site](#desktop-site-18)
	* [Mobile Site](#mobile-site-18)
	* [Search - None](#search---none)
* [Contact Us](#contact-us)
	* [Desktop Site](#desktop-site-19)
	* [Mobile Site](#mobile-site-19)
* [Site Administration](#site-administration)
* [Account Management](#account-management)
* [Sign In via Social Media Sites](#sign-in-via-social-media-sites)
* [Alert Messages](#alert-messages)

<!-- End Document Outline -->

## Navigation

### Desktop site:
![navigation-menu-desktop](https://github.com/claire-potter/xperience-dezignwiz/blob/main/documentation/features/01.header-navigation-search-desktop.JPG)


### Mobile Site
![navigation-menu-mobile](https://github.com/claire-potter/xperience-dezignwiz/blob/main/documentation/features/01.header-navigation-search-mobile.JPG)

The Navigation Menu falls within the Header. This is created on the template base.html, which is the base template for all site templates. It contains the site logo - Xperience DezignWiz, with the 'X' created as a font awesome icon.

### Desktop Site:
The Navigation menu will display horizontally across the page as an unordered list

### Mobile Site:
The Navigation menu will compress into the navigation hamburger icon. When it is clicked the menu will display at the top of the site.

### Links:
* Home - the home page
* Steps - dropdown menu:
    * Steps 1 to 3
    * Steps 4 to 7
* Surveys - link to survey list
* Contact Us - contact form
* Account
    * Register - if logged out
    * Login - if logged out
    * Logout - if logged in
* Admin - if logged in as a staff member

### Dropdown Menu

The Steps dropdown menu is created in the template and the dropdown action is completed through the JavaScript script.js

#### Dropdown Desktop:

![Dropdown Menu Desktop](https://github.com/claire-potter/xperience-dezignwiz/blob/main/documentation/features/02.steps-dropdown-desktop.JPG)

#### Dropdown Mobile:

![Dropdown Menu Mobile](https://github.com/Claire-Potter/Xperience-DezignWiz/blob/main/documentation/features/02.steps-dropdown-mobile.JPG)

## The Home Page

### Desktop Site
![Home Page Desktop](https://github.com/claire-potter/xperience-dezignwiz/blob/main/documentation/features/03.welcome-purpose-desktop.JPG)

### Mobile Site
![Home Page Mobile](https://github.com/claire-potter/xperience-dezignwiz/blob/main/documentation/features/03.welcome-purpose-mobile.JPG)

* The Home Page displays a welcome message containing the site purpose
* This is created as a bootstrap accordion and can be minimized
* The home page renders well across screen sizes
* The Home Page provides clear direction as to next action required by providing a Get Started button

## The Footer

### Desktop Site
![Footer Desktop](https://github.com/claire-potter/xperience-dezignwiz/blob/main/documentation/features/04.footer-desktop.JPG)
### Mobile Site
![Footer Mobile](https://github.com/claire-potter/xperience-dezignwiz/blob/main/documentation/features/04.footer-mobile.JPG)

* The Footer contains the creation date and designer details
* It has been styled in a darker blue colour to create contrast with the white font
* The Social Media link icons are displayed in the footer
* Each of these icons will open the respective social media site on a new blank page ensuring the user has easy access to the Xperience DezignWiz social accounts (in theory as the accounts do not exist)

## Steps One to Three and Steps Four to Seven

### Desktop Site
![Steps One to Three Desktop](https://github.com/claire-potter/xperience-dezignwiz/blob/main/documentation/features/05.steps-1-to-3-desktop.JPG)

![Steps Four to Seven Desktop](https://github.com/claire-potter/xperience-dezignwiz/blob/main/documentation/features/05.steps-4-7-desktop.JPG)

### Mobile Site
![Steps One to Three Mobile](https://github.com/claire-potter/xperience-dezignwiz/blob/main/documentation/features/05.steps-1-to-3-mobile.JPG)

![Steps Four to Seven Mobile](https://github.com/claire-potter/xperience-dezignwiz/blob/main/documentation/features/05.steps-4-7-mobile.JPG)

* The Get Started button will open the first page of the Design Thinking steps containing steps one to three
* The steps can also be accessed from the navigation menu under the dropdown steps
* Each step is created as a bootstrap card and contains:
    * An appropriate image
    * The step number button
    * The step title 
    * A step excerpt
    * The step progress status
    * The number of step tools available
    * The number of step resources available
* The step progress status will reflect as a default status of 'Not Started' for users who are not logged in, or if a logged in user has not updated their status as yet. Once the user has updated their status, it will reflect here accordingly
* The step resources is a count of the number of linked resource videos added to the step model
* The step tools is a count of the number of linked tools added to the step model

### Steps Navigation

Navigation arrow icons are provided to allow the user to easily scroll back and fourth between the two steps pages. Javascript and bootstrap are used to add a tooltip to the navigation which displays as first and next

#### Steps Navigation

![Steps Navigation Arrows](https://github.com/claire-potter/xperience-dezignwiz/blob/main/documentation/features/06.prev-next-arrows.JPG)


#### Steps Button

The Image overlay was used to create the link styled as a button to access the individual step link page. Each button will open the correct step detail. The styling of the button is aligned to all styled buttons across the site so that the user can expect the action. The Tool-tip text displays the instruction to click here to access the specific step

#### Steps Button

![Step Button](https://github.com/claire-potter/xperience-dezignwiz/blob/main/documentation/features/07.step-buttons.JPG)

## Step Detail

### Desktop Site
![Step Detail Desktop](https://github.com/claire-potter/xperience-dezignwiz/blob/main/documentation/features/08.step-details-one-desktop.JPG)

### Mobile Site
![Step Detail Mobile](https://github.com/claire-potter/xperience-dezignwiz/blob/main/documentation/features/08.step-details-one-mobile.JPG)

* The Step Detail site, accessed from the steps page, renders for all seven steps. In the jumbotron each step will contain the unique Step title, number and progress status
* Below the step detail image specific for the step page will display followed by the step excerpt
* A summary of the Design Thinking process for the step will be provided below, styled as an accordion as per the home page, as this allows users with smaller screen to minimize the content to access the rest of the page
* Navigation arrows are available below the step summary which allows a user to perform a circular loop between all of the steps

### Resources
* The Resources section within the Step Detail page contains the relevant Code Institute videos embedded per step
* The user will have controls available to choose when to play the video and the associated options

### Desktop Site
![Resource Videos Desktop](https://github.com/claire-potter/xperience-dezignwiz/blob/main/documentation/features/08.step-details-two-resources-desktop.JPG)

### Mobile Site
![Resource Videos Mobile](https://github.com/claire-potter/xperience-dezignwiz/blob/main/documentation/features/08.step-details-two-resources-mobile.JPG)

### Tools
* Each tool added to the step can be accessed in this section
* The link will open the step tool page, it doesn't open a new page as there is a return button available at the end of each step tool page

### Desktop Site
![Step Tools Desktop](https://github.com/claire-potter/xperience-dezignwiz/blob/main/documentation/features/08.step-details-three-tools-desktop.JPG)

### Mobile Site
![Step Tools Mobile](https://github.com/Claire-Potter/Xperience-DezignWiz/blob/main/documentation/features/08.step-details-three-tools-mobile.JPG)

### Step Progress
* The Progress Status section contains the progress form, the comments form and the comments
* The progress form is used to select the current progress status from
    * Not Started
    * In Progress
    * Completed
    * Revisiting
* Only a logged in user will have access to this section
* Once a user has updated their status it will reflect at the top of the Step Detail page as the latest saved status

### Step Progress Status Desktop
![Step Progress Status Section Desktop](https://github.com/claire-potter/xperience-dezignwiz/blob/main/documentation/features/09.step-details-step-updates-desktop.JPG)

### Progress Form Mobile
![Step Progress Form](https://github.com/claire-potter/xperience-dezignwiz/blob/main/documentation/features/08.step-details-four-progress-mobile.JPG)

### Progress Status Updated
![Step Progress Updated](https://github.com/claire-potter/xperience-dezignwiz/blob/main/documentation/features/08.step-details-five-progress-updated-mobile.JPG)

### Progress Status Section if not logged in

![Progress Status if not logged in](https://github.com/claire-potter/xperience-dezignwiz/blob/main/documentation/features/09.step-details-seven-step-updates-not-logged-in.JPG)

### Comments
* The Comments section contains a comments form used to capture any relevant progress comments
* The comment once saved will only display to the logged in user
* The user can capture and save the form from this section
* When they navigate back to the specific step detail page, they can view their captured comment

### Comments Form Mobile
![Comments Form Mobile](https://github.com/claire-potter/xperience-dezignwiz/blob/main/documentation/features/09.step-details-six-comments-mobile.JPG)

### Comments Updated
![Comments Updated](https://github.com/claire-potter/xperience-dezignwiz/blob/main/documentation/features/09.step-details-six-comments-display-mobile.JPG)

## Step Tools
* When a step tool link is selected the step tool page will open
* The page is styled as per the step detail page with a unique image per tool and an accordion with the content
* A return button is found at the end of the step tool page so that the user can easily navigate back to the step detail page

### Desktop site
![Step Tool Page Desktop](https://github.com/claire-potter/xperience-dezignwiz/blob/main/documentation/features/10.step-tools-desktop.JPG)
### Mobile Site
![Step Tool Mobile Page](https://github.com/claire-potter/xperience-dezignwiz/blob/main/documentation/features/10.step-tools-mobile.JPG)

## Survey - from Empathy Step
* The Survey is a tool utilised within the empathy step
* A section is specifically created to display on the empathy page to provide a user the link to create surveys.

### Survey from Empathy Step
![Survey from Empathy Step](https://github.com/claire-potter/xperience-dezignwiz/blob/main/documentation/features/11.step-tools-survey-from-empathy.JPG)

## Survey - List
* When the Survey tool is selected from the Empathy Step or from the main menu link, the user will be directed tot the Survey List page
* If the user is not logged in, they will be redirected to the Login screen
* If a user has not created any surveys, a message saying so will display
* A button to the create survey page will display
* If they have created surveys, the Survey Title, creation data and time, edit/view link and delete link will display
* If the Survey is still in draft mode the edit link will display
* If the Survey is activated the view link will display

### Desktop Site
![Survey List Desktop](https://github.com/claire-potter/xperience-dezignwiz/blob/main/documentation/features/12.survey-list-desktop.JPG)
### Mobile Site
![Survey List Mobile](https://github.com/claire-potter/xperience-dezignwiz/blob/main/documentation/features/12.survey-list-mobile.JPG)
### Survey List - No Surveys
![Survey List -No Surveys](https://github.com/claire-potter/xperience-dezignwiz/blob/main/documentation/features/12.survey-list-desktop-no-surveys.JPG)

### Survey Create

* The button will open the page for the user to create a new survey
* The user will be able to save a new Survey Title
* A default Survey Title will display
* Once the user submits, the draft survey us created

### Desktop Site
![Survey Create Desktop](https://github.com/claire-potter/xperience-dezignwiz/blob/main/documentation/features/13.survey-create-desktop.JPG)

### Mobile Site
![Survey Create Mobile](https://github.com/claire-potter/xperience-dezignwiz/blob/main/documentation/features/13.survey-create-mobile.JPG)

## Survey Default Questions
* After the survey title is created the user is directed to the default questions page
* They are provided with a view of all of the default questions and answer options that will automatically be added to the survey
* They will only have the option to accept and proceed as all surveys are set up to include the generic questions

### Desktop Site
![Survey Default Questions Desktop](https://github.com/claire-potter/xperience-dezignwiz/blob/main/documentation/features/14.survey-default-questions-options-desktop.JPG)
### Mobile Site
![Survey Default Questions Mobile](https://github.com/claire-potter/xperience-dezignwiz/blob/main/documentation/features/14.survey-default-questions-options-mobile.JPG)

## Survey - Add Questions and Options
* The user will have the option to create their own custom questions for their survey
* They have to add at least one question
* If they choose to cancel and exit, they will be taken to the Survey Edit page, for the draft survey
* When a question is saved, the user is directed to add answer options for the question
* The User will need to add at least one option per question and save
* They are then taken back to add the next question
* Once they have added all their questions they can choose to Activate the survey

### Desktop Site
![Survey Create Question Desktop](https://github.com/claire-potter/xperience-dezignwiz/blob/main/documentation/features/15.survey-create-question-desktop.JPG)
### Mobile Site
![Survey Create Question Mobile](https://github.com/claire-potter/xperience-dezignwiz/blob/main/documentation/features/15.survey-create-question-mobile.JPG)
### Cancel Add Question
![Cancel Add Questions](https://github.com/claire-potter/xperience-dezignwiz/blob/main/documentation/features/15.survey-create-question-cancel-to-edit-desktop.JPG)

### Desktop Site
![Add Option Desktop](https://github.com/claire-potter/xperience-dezignwiz/blob/main/documentation/features/16.survey-create-option-desktop.JPG)

### Mobile Site
![Create Option Mobile](https://github.com/claire-potter/xperience-dezignwiz/blob/main/documentation/features/16.survey-create-option-mobile.JPG)

### Create Second Option
![Create second option](https://github.com/claire-potter/xperience-dezignwiz/blob/main/documentation/features/16.survey-create-option-second-mobile.JPG)

### Activate Survey
![Activate Survey](https://github.com/claire-potter/xperience-dezignwiz/blob/main/documentation/features/17.survey-create-add-second-question-or-activate.JPG)

## Send Survey

* The site has been integrated with the third party Sendgrid functionality to be able to send out emails
* Once the survey is activated the user will be taken to send out their email
* A default subject is provided
* The user is able to add multiple email addresses
* Default message content is added which the user can edit
* The URL for the survey will be added to the email for the user before it is sent out
* When the user submits the email form the email content will be validated and it will be sent out to all valid email addresses
* If the email is sent, a confirmation message will display
* The email content will be added to the email template created in Sendgrid and delivered to the valid email address/es

### Desktop Site
![Send Email Desktop](https://github.com/claire-potter/xperience-dezignwiz/blob/main/documentation/features/18.send-survey-desktop.JPG)
### Mobile Site
![Send Email Survey](https://github.com/claire-potter/xperience-dezignwiz/blob/main/documentation/features/18.send-survey-mobile.JPG)
### Email Sent message
![Survey Sent](https://github.com/claire-potter/xperience-dezignwiz/blob/main/documentation/features/18.email-sent-mobile.JPG)

### Email Delivered
![Email Delivered](https://github.com/claire-potter/xperience-dezignwiz/blob/main/documentation/features/19.email-template.JPG)

## Start Survey

* The surveyee can open the survey link received to start the survey
* A login button is also provided in the template to encourage existing users to login or new users to create an account
* The user will be taken to the start survey page which will display a default survey image and the survey title with a link to begin the survey
* When the button is clicked the surveyee will be taken to complete their answers

### Desktop Site
![Start Survey Desktop](https://github.com/claire-potter/xperience-dezignwiz/blob/main/documentation/features/20.start-survey-desktop.JPG)

### Mobile Site
![Start Survey Mobile](https://github.com/claire-potter/xperience-dezignwiz/blob/main/documentation/features/20.start-survey-mobile.JPG)

## Complete and Submit Survey
* The surveyee can proceed to answer the survey without having to login
* The surveyee will select an answer from the dropdown menus for all of the default questions
* The surveyee will select an answe from the custom question by using the radio buttons
* The surveyee is required to select an answer
* The surveyee submits their survey successfully
* A thank you message is displayed with a link to the home page to be taken back to check out the rest of the site

### Desktop Site
![Complete Questions Desktop](https://github.com/claire-potter/xperience-dezignwiz/blob/main/documentation/features/21.answer-default-questions-desktop.JPG)
### Mobile Site
![Complete Questions Mobile](https://github.com/claire-potter/xperience-dezignwiz/blob/main/documentation/features/21.answer-default-questions-mobile.JPG)
### Answer Required
![Required Answers](https://github.com/claire-potter/xperience-dezignwiz/blob/main/documentation/features/21.answer-default-questions-required.JPG)

### Thank you message
![Thank you message](https://github.com/claire-potter/xperience-dezignwiz/blob/main/documentation/features/22.survey-thank-you-desktop.JPG)

## Survey Details - Results

* The Survey Detail page, accessed through the view button on the Survey List page contains the following content"
    * Number of Submissions
    * Link to Start Survey
    * Age Question Doughnut chart
    * Age Question table of results - percentages
    * Gender Question Doughnut chart
    * Gender Question table of results - percentages
    * Industry Question Doughnut chart
    * Industry Question table of results - percentages
    * Custom Questions 
    * Custom Option selection - percentages
* The user will refer to the page to understand the generic information related to their client base
* The data will allow them to put together personas
* The return button takes the user back to their list of surveys
* The user has the option to delete a survey from the survey list page
* For the first release, the  survey is very simple, with basic functionality and results which can be expanded
* In the future, a link from the summary page can be added to resend the survey
* A validation to make sure users can only complete the survey once can be added, this would require that surveyees add an email address
* The charts can be refined and the custom questions can also be displayed as charts

### Desktop Site
![Survey Detail part one desktop](https://github.com/claire-potter/xperience-dezignwiz/blob/main/documentation/features/23.survey-detail-part-one-desktop.JPG)
![Survey Detail part two desktop](https://github.com/claire-potter/xperience-dezignwiz/blob/main/documentation/features/23.survey-detail-part-two-desktop.JPG)

### Mobile Site
![Survey Detail part one mobile](https://github.com/claire-potter/xperience-dezignwiz/blob/main/documentation/features/23.survey-detail-part-one-mobile.JPG)
![Survey Detail part two mobile](https://github.com/claire-potter/xperience-dezignwiz/blob/main/documentation/features/23.survey-detail-part-two-mobile.JPG)

### Delete Survey
![Survey-delete](https://github.com/claire-potter/xperience-dezignwiz/blob/main/documentation/features/23.survey-delete.JPG)

## Search for a Step

* The search feature allows the user to search by Step Title for a Step
* An autocomplete list has been set up in javascript file, to match what the user types in, and return the step title which matches
* As the search is built simply, this encourages the user to select the correct search term in the correct format
* When the user enters the searched term, the search page, specific per step is returned with a link to open the step
* If an incorrect term is search or if the search form is submitted with an empty search, the page returned  provides the user with the links to each step page, so that they are able to access whichever page they require

### Desktop Site
![Search desktop](https://github.com/claire-potter/xperience-dezignwiz/blob/main/documentation/features/24.search-step-desktop.JPG)



![Search-results-desktop](https://github.com/claire-potter/xperience-dezignwiz/blob/main/documentation/features/24.search-results-desktop.JPG)

### Mobile Site
![Search mobile](https://github.com/claire-potter/xperience-dezignwiz/blob/main/documentation/features/24.search-step-mobile.JPG)


![Search results mobile](https://github.com/claire-potter/xperience-dezignwiz/blob/main/documentation/features/24.search-results-mobile.JPG)

### Search - None
![Search None](https://github.com/claire-potter/xperience-dezignwiz/blob/main/documentation/features/24.search-none.JPG)


## Contact Us

* From the navigation menu a user can select Contact us
* They do not need to be logged in to use this feature
* A contact form will be provided on the page
* If the user is logged in, their name and email address will be automatically completed
* They are able to capture their request and send it
* An email will be sent to the admin email address
* The admin are also able to view and delete the contact request from the admin page

### Desktop Site
![Contact Desktop Site](https://github.com/Claire-Potter/Xperience-DezignWiz/blob/main/documentation/features/25.contact-desktop.JPG)

### Mobile Site
![Contact Mobile Site](https://github.com/Claire-Potter/Xperience-DezignWiz/blob/main/documentation/features/25.contact-mobile.JPG)


 Please <a href="" target="_blank">click here</a> to view the rest of the images.

 ## Site Administration

 * The Django Admin Site has been enabled and set up for two users
 * The AdminUser has a user group assigned
 * The SuperUser does not have a user group assigned
 * View and action restrictions have been enabled in admin.py for each model
 * This has been set up in order to protect data to ensure the administrators cannot 'break' the site
 * Various fields have had their create or edit ability removed as these should only be completed from the front end as a user
 * The Admin users are still able to create user fields from the front end

  Please <a href="" target="_blank">click here</a> to view the administration screenshots.

## Account Management

 * The Django Auth Account Management has been set up for the site
 * The default templates have been used to create the account pages
 * If a user is not logged in - they will have the option to login or register on their menu
 * When creating a new account, the email field will be validated
 * When creating a password validations are applied
 * When a user registers, an email is sent to validate their email address
 * If a user forgets their password they can send a forgot password email
 * A link will be sent to them, if they follow it they can successfully reset their password
 * A user has the option to add a new email address, add an additional email address, update their primary email address or resend their email validation message
 * The account base.html has been set up as a bootstrap side bar menu which displays across the account pages

 Please <a href="" target="_blank">click here</a> to view the account management screenshots.

 ## Sign In via Social Media Sites

 * It has been enabled for a user to sign in via Google and Facebook
 * From the login page the user can click on either Google or Facebook to register or login to the site
 * Their social media account will be picked up and aunthenticated
 * They will be able to successfully login
 * The single sign on makes it easy for the user to access the site

 Please <a href="" target="_blank">click here</a> to view the sign on via social accounts.

## Alert Messages

  * If a user completes an action a success or error message will be displayed
  * The message will automatically clear after two seconds
  * This provides the user with confirmation that their action was successful or failed

![Alert Message]()




