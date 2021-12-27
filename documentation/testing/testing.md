# Testing

## Responsiveness and Compatibility

1. Lambda Test was used to check the site on different browsers and operating systems:
    * Safari
    * Chrome
    * Firefox
    * Edge
    * Opera
    * The site is compatible and accessible across all browsers.
    * Please click here to view browser testing screenshots.
    
2. Devices and Screen Sizes

    * The site was tested using the Responsively App as well as the Google Chrome device tool bar. The site has been set up to render effectively across multiple screen sizes and devices. I have tested using the following device displays:
    
    * Responsively App:
        * 5K Display 5120 * 2880
        * 4K Display 3840 * 2160
        * MacBook Pro 16 inch 3072 * 1920
        * MacBook Pro 15 inch 2880 * 1800
        * MacBook Pro 13 inch 2560 * 1600
        * Laptop with HiDPi Screen 1440 * 900
        * Laptop 1400 * 1000
        * MacBook Air 1440 * 900
        * Laptop with MDPi Screen 1280 * 800
        * Generic Laptop 1280 * 950
        * iPad Pro 1024 * 1366
        * Kindle Fire HDX 800 * 1280
        * iPad 768 * 1024
        * Microsoft Lumia 550 640 * 360
        * Blackberry Playbook 600 * 1024
        * Nokia N9 480 * 854
        * iPhone 6/7/8 Plus 414 * 736
        * iPhone 6/7/8 375 * 667
        * Galaxy S 5 360 * 640
        * iPhone 4 320 * 480
        * JioPhone 2 240 * 320
        * Responsive Mode - change the screen width to test various sizes
        
    * Google Chrome device tool bar:
        * Galaxy Note 3
        * Galaxy Note II
        * Galaxy S III
        * KindleFire HDX
        * LG Optimus L70
        * Laptop with HiDPI screen
        * Laptop with MDPI screen
        * Laptop with touch
        * Microsoft Lumia 550
        * Microsoft Lumia 950
        * Moto G4
        * Galaxy S5
        * Pixel 2
        * Pixel 2 XL
        * iPhone 5/SE
        * iPhone 6/7/8
        * iPhone 6/7/8 Plus
        * iPhone X
        * iPad
        * iPad Pro
        * Surface Duo
        * Galaxy Fold
        * Responsive Mode
        
        
## Code Validation

1. W3C HTML Code Validator
    * The code for all html pages was entered into the validator and all pages passed excluding the django templates tags.
          
2. W3C CSS Jigsaw Validator
    * The code for the stylesheet.css was entered into the validator and passed excluding the google fonts import.
3. JScript Code Validator
    * The code for the following JavaScript scripts pages was entered into the validator passed:
        * script.js
        
4. All .py files passed through pep-8 online successfully:

 Please click here to view the screenshots.

Pycodestyle ran within the console returned no errors:
 
 Please click here to view the screenshots.

## Testing Accessibility

The Wave Evaluation Tool was used to test the Accessibility of the site.

I had to make some changes to make sure I could pass the accessibility testing as best as possible.

Please click here to see the Wave screenshots.

**Home page:**

Two errors were received which were corrected:

1. A missing aria-label was added to the home page image.
2. A ‘floating’ aria-label was removed.

Warnings:

3. Replaced ‘p’ elements with heading (h1 – h6) elements for sections.
4. The one warning left was for the navigation home link, as it is seen as redundant, however as navigation is
standard across pages it is required.

**Steps 1-7:**

3 errors:

1. Step overlay did not contain an aria-label/ alt text. This was added.
2. Low contrast errors relating to muted text- this was changed.
3. Heading levels were added to reduce the warnings.


**Search page**

1. No errors. An image aria-label / alt text was updated to be more specific.

**Steps Details page:**

2 errors:
1. A ‘floating’ aria-label was removed.
2. Contrast issues were resolved.
Heading changes were made to improve accessibility.

**Step Tool page:**

There were no errors.

**Contact page:**

There were no errors.


**The Account Pages:**

There were no errors

**The Survey pages:**

Survey Create page – 2 errors:

Two missing form labels – added

No other errors

## Performance:

Google lighthouse utilised to test performance of site and mobile. Please see reports attached here.

I used the tool ImageOptimizer to resize all images to improve performance.
I also moved the home image
from the static media folder, and created a CloudinaryField in which I saved the image. 

Whilst reading through the cloudinary documentation on cloudinary.com, I came across the following passage:

*“Selecting the optimal image format - f_auto
Some formats such as WebP and JPEG-XR are more efficient than the standard JPEG format for delivering web images, but they are not supported by all browsers: JPEG-XR is supported only in Internet Explorer/Edge browsers, while WebP is currently supported only in Chrome/Opera browsers and Android devices. The result is that the best image to deliver to your visitor depends on which browser they are using.
Cloudinary has the ability to automatically detect which browser is requesting the image and then select the most efficient image format to deliver. Just add the fetch_format parameter and set its value to auto (f_auto in URLs).”*

I added this to the cloudinary tags for all pages with images.

## Automated Tests

### Tox Environment test

The following steps were followed to run a tox test:

1. First, install tox:
    * $ pip install tox

2. After that, edit tox.ini file and input your Cloudinary credentials in setenv.

3. Then, just run:
    * $ tox

I had to create the following two files:


image one


And:

image two

Results were as follows:

image three

Which means:

Only if all environments ran successfully tox will return exit code 0 (success). In this case you’ll also see the message congratulations :). 

Please follow this link to description of tox system overview:

<a href="https://tox.wiki/en/latest/index.html?highlight=congratulations%20result#system-overview" target="_blank">Tox wiki</a>

## Django Extensions

Django extensions was installed and the automated check through python manage.py was run successfully.

Results were as follows:

## Validate-template

The validate-template test was created in home - tests.py and run for all templates.

Before:

After corrections:


## HTML-Validator 

The html-validator test was run for all templates.

It was installed as follows:

1. Install django-extensions
2. Add to apps list
3. Install html-validator
4. Set up html-validator middleware
5. Add the html-validator settings to settings.py
6. Enable and open each site page for validation file to be generated.
7. Only if a template contains an error will the text file be created and displayed in the console, therefore there are no screenshots for templates once errors were corrected.

Please click here to view the results.

## Spell Checker

internetmarketingninjas.com was utilised to check spelling across the entire site.

Each page received a summary with any errors per page as follows:

Most of the spelling errors were due to American vs. British spelling as the site is American.

Spelling Before:

Spelling After:

## Bugs and Issues

### Model Creation

I decided to go back to the embed-video you tube video I watched to learn about the embed-video library.

I wanted to include a video preview within my admin page. 
I created a new Resource model to add the video fields to. When I previously tried to do this, I tried to add the Step model as a foreign field to the Resource model. I then wasn’t able to get the code right to pull the videos through to the Step detail page, which referenced the Step model. I had the exact same issue with the Tool model.

Out of frustration, I manually created the relationship to the videos by adding three different embed video fields to the Step model. I then created three separate fields in my Step Detail template to load each video. For the video count I created an integer field in the step model and set it to the number of videos added per step. This was a rather inefficient work around and meant that maintenance would also be completed separately.

For the tools per step I completed a similar process. I created three separate tool names in views and wrote out if, elif and else statements again to manually reference the different tools per step. This resulted in a very long view, and separate sections to maintain. 

I simply went to the end of the embed-video you tube and watched the creation of the admin.py. Suddenly something clicked, I realised that if I created the Resource model as a Many to Many field in the Step model, I could easily reach the Resource model and return the relevant videos per step. 

I feel as if through the weeks spent working on my project set up, I developed a real understanding of how the database relationships work. I went back and re-coded my Resources and Tool model, so that now the code within the view and templates is minimal and the page relies on the database relationship to get the relevant data. This was a big victory for me.

I also went back and added all of my Images for my DesignSteps app to one model. I added the model as a foreign key to the Step model, firstly for the featured image and then for the individual step image.
I also added it as a foreign key to the Tool model. This way I am now able to maintain all of the images from the same model. I could also add a field called name, which I could then pull through to generate the alt text for each image, instead of having a generic alt description, the actual image is now described.

### Chart-js

I ran into an issue when creating the chart-js functionality within the survey detail page. I was able to set up and generate the doughnut charts for the default survey questions.

However, when it came to the questions, which a user can set up themselves, a for loop is set up to generate the question, the options for the question and the percentage each option was selected. 

The issue was that, I could only get the chart-js jquery code to reference one chart element. Even if I created multiple elements and tried to reach one after the other by referencing the class, it would only generate the chart once. The data was then corrupted as it would try to add one question and option set over the other.

Due to time restraint, I wasn’t able to spend further time trying to complete this task. I made the decision to keep the question section set up the same as the set up completed in the survey tutorial for the first release of this project.

## Feature and User Story Testing

### Feature: Navigation

* The site has a navigation menu, which displays on the desktop and resizes appropriately for smaller screens
    * Pass
* All menu options are readable and all links direct the user to the correct pages
    * Pass
* The Navigation menu is created within the header and is styled according to the site design
    * Pass

#### User Story
As **a User** I can **easily Navigate across all site pages** so that **I can view all content logically and without hassle**

#### Acceptance Criteria
* The Navigation menu is located in a visible page section
    * Pass
* The menu items are logical and all links open the correct pages
    * Pass
* The Navigation menu items will display according to the user's logged in status
    * Pass
* If the user is a staff member, they will also have access to the Admin site
    * Pass
* The Navigation menu will re-size for smaller screens and will display as a the navigation 'hamburger'
    * Pass

#### Desktop Site 
![Navigation Menu Desktop](https://raw.githubusercontent.com/claire-potter/xperience-dezignwiz/main/documentation/features/01.header-navigation-search-desktop.JPG)


#### Mobile Site
![Navigation Menu Mobile](https://github.com/claire-potter/xperience-dezignwiz/blob/main/documentation/features/01.header-navigation-search-mobile.JPG)

### Feature: Home Page

* The Home Page displays a welcome message containing the site purpose
    * Pass
* This is created as a bootstrap accordion and can be minimized
    * Pass
* The home page renders well across screen sizes
    * Pass
* The Home Page provides clear direction as to next action required by providing a Get Started button
    * Pass

#### User Story

As a **Site User** I can **understand the site purpose** so that **my expectations of the site are set**

#### Acceptance Criteria
  
* As soon as a user enters the site they should be presented with the site purpose
    * Pass
* This should be easily understood and provide the necessary directions required
    * Pass
* The user should have an understanding about what to expect
    * Pass
    
#### Desktop Site

![Home Page Desktop](https://github.com/claire-potter/xperience-dezignwiz/blob/main/documentation/features/03.welcome-purpose-desktop.JPG)

#### Mobile Site
![Home Page Mobile](https://github.com/claire-potter/xperience-dezignwiz/blob/main/documentation/features/03.welcome-purpose-mobile.JPG)

### Feature: The Footer

* The Footer contains the creation date and designer details
    * Pass
* It has been styled in a darker blue colour to create contrast with the white font
    * Pass
* The Social Media link icons are displayed in the footer
    * Pass
* Each of these icons will open the respective social media site on a new blank page ensuring the user has easy access to the Xperience DezignWiz social accounts (in theory as the accounts do not exist)
    * Pass
    
#### User Story

As **a User** I can **access XperienceDezignWiz Social Media Accounts** so that **I don't have to search for them individually**

#### Acceptance Criteria
  
* Social Media Icons appear within the page footer
    * Pass
* The icon contains a link to the various social media sites
    * Pass
* Clicking the icon will open the social media site on a new blank tab
    * Pass
  


#### Desktop Site
![Footer Desktop](https://github.com/claire-potter/xperience-dezignwiz/blob/main/documentation/features/04.footer-desktop.JPG)
#### Mobile Site
![Footer Mobile](https://github.com/claire-potter/xperience-dezignwiz/blob/main/documentation/features/04.footer-mobile.JPG)

### Feature: Steps One to Three and Steps Four to Seven


* The Get Started button will open the first page of the Design Thinking steps containing steps one to three
    * Pass
* The steps can also be accessed from the navigation menu under the dropdown steps
    * Pass
* Each step is created as a bootstrap card and contains:
    * An appropriate image
        * Pass
    * The step number button
    * The step title 
        * Pass
    * A step excerpt
        * Pass
    * The step progress status
        * Pass
    * The number of step tools available
        * Pass
    * The number of step resources available
         * Pass
* The step progress status will reflect as a default status of 'Not Started' for users who are not logged in, or if a logged in user has not updated their status as yet. Once the user has updated their status, it will reflect here accordingly
    * Pass
* The step resources is a count of the number of linked resource videos added to the step model
    * Pass
* The step tools is a count of the number of linked tools added to the step model
    * Pass

#### User Stories

As **a Site User** I can **view a step by step design thinking process** so that **I can easily follow the process**

As **a User** I can **view the summarised sub-sections of a step from the step process summary page** so that **I can easily overview 1. My progress within each step, 2. How many resources are available per step 3. How many tools are available per step**



#### Acceptance Criteria
  
* A Site User can view a summary of each design thinking step
    * Pass
* A Site User can view steps 1 to 3 and steps 4 to 7 in two sequenced pages which they can easily move between
    * Pass
  
* Each step on the Step Lists includes the progress status with an updated status if applicable
    * Pass
* Each step on the Step Lists includes a resources summary with the number of resources matching the number of linked resources per step
    * Pass
* Each step on the Step Lists includes a tools summary with the number of tools matching the number of linked tools per step
    * Pass
    
### Desktop Site
![Steps One to Three Desktop](https://github.com/claire-potter/xperience-dezignwiz/blob/main/documentation/features/05.steps-1-to-3-desktop.JPG)

![Steps Four to Seven Desktop](https://github.com/claire-potter/xperience-dezignwiz/blob/main/documentation/features/05.steps-4-7-desktop.JPG)

### Mobile Site
![Steps One to Three Mobile](https://github.com/claire-potter/xperience-dezignwiz/blob/main/documentation/features/05.steps-1-to-3-mobile.JPG)

![Steps Four to Seven Mobile](https://github.com/claire-potter/xperience-dezignwiz/blob/main/documentation/features/05.steps-4-7-mobile.JPG)

### Steps Navigation

* Navigation arrow icons are provided to allow the user to easily scroll back and fourth between the two steps pages.
    * Pass
* JavaScript and bootstrap are used to add a tool-tip to the navigation which displays as first and next
    * Pass
    

#### Steps Navigation

![Steps Navigation Arrows](https://github.com/claire-potter/xperience-dezignwiz/blob/main/documentation/features/06.prev-next-arrows.JPG)


#### Steps Button

* Each button will open the correct step detail. 
    * Pass
The styling of the button is aligned to all styled buttons across the site so that the user can expect the action. 
    * Pass
* The Tool-tip text displays the instruction to click here to access the specific step
    * Pass
    
#### User Story

As **a Site User** I can **click on a step and open it** so that **I can access the content of the step**

#### Acceptance Criteria
  
* Each step displays individually on a page
    * Pass
* Each step has a unique URL link to open the Step page
    * Pass
* When the URL is clicked, the Step detail page will open
    * Pass
    
#### Steps Button

![Step Button](https://github.com/claire-potter/xperience-dezignwiz/blob/main/documentation/features/07.step-buttons.JPG)

### Feature: Step Detail

* The Step Detail site, accessed from the steps page, renders for all seven steps. In the jumbotron each step will contain the unique Step title, number and progress status
    * Pass
* Below the step detail image specific for the step page will display followed by the step excerpt
    * Pass
* A summary of the Design Thinking process for the step will be provided below, styled as an accordion as per the home page, as this allows users with smaller screen to minimize the content to access the rest of the page
    * Pass
* Navigation arrows are available below the step summary which allows a user to perform a circular loop between all of the steps
    * Pass
    
#### User Story

As **a User** I can **easily move back and fourth between steps** so that **I can updated my progress status for each step and access the step content as and when required.**

#### Acceptance Criteria
  
* Navigation within the step details page directs the user between steps
    * Pass
* The previous page arrow will open the previous step
    * Pass
* The next page arrow will open the next step
    * Pass
* For the step Getting Started, the previous page arrow will go to the last step Finishing off
    * Pass
* For the step Finishing Off, the next page arrow will go to the first step Getting Started
    * Pass
* The user is able to circle back and fourth between all seven steps as required
    * Pass

#### Desktop Site
![Step Detail Desktop](https://github.com/claire-potter/xperience-dezignwiz/blob/main/documentation/features/08.step-details-one-desktop.JPG)

#### Mobile Site
![Step Detail Mobile](https://github.com/claire-potter/xperience-dezignwiz/blob/main/documentation/features/08.step-details-one-mobile.JPG)

#### Resources
* The Resources section within the Step Detail page contains the relevant Code Institute videos embedded per step
    * Pass
* The user will have controls available to choose when to play the video and the associated options
    * Pass

#### User Story

As **a Site User** I can **access and play the resource video/s within the step** so that **I can re-view the learning material to understand the step within the process**

#### Acceptance Criteria
  
* The video links are saved to the database
    * Pass
* The videos display within the Step Detail page
    * Pass
* The user can select to play the video and has control options
    * Pass
    
#### Desktop Site
![Resource Videos Desktop](https://github.com/claire-potter/xperience-dezignwiz/blob/main/documentation/features/08.step-details-two-resources-desktop.JPG)

#### Mobile Site
![Resource Videos Mobile](https://github.com/claire-potter/xperience-dezignwiz/blob/main/documentation/features/08.step-details-two-resources-mobile.JPG)

#### Tools
* Each tool added to the step can be accessed in this section
    * Pass
* The link will open the step tool page, it doesn't open a new page as there is a return button available at the end of each step tool page
    * Pass
    
#### User Story

As **a Site User** I can **access any step tools available ** so that **I can complete any documentation required for the step and understand how to implement the step**

#### Acceptance Criteria
  
* The step tools data is saved to the database
    * Pass
* Each Step has the relevant step tools linked to the step
    * Pass
* The step tool is displayed in the step detail page and links to the relevant step tool page
    * Pass
*  The user can open the link to display the step tool content
    * Pass
* The user can return to the step detail page
    * Pass

#### Desktop Site
![Step Tools Desktop](https://github.com/claire-potter/xperience-dezignwiz/blob/main/documentation/features/08.step-details-three-tools-desktop.JPG)

#### Mobile Site
![Step Tools Mobile](https://github.com/Claire-Potter/Xperience-DezignWiz/blob/main/documentation/features/08.step-details-three-tools-mobile.JPG)

#### Step Progress
* The Progress Status section contains the progress form, the comments form and the comments
    * Pass
* The progress form is used to select the current progress status from
    * Not Started
        * Pass
    * In Progress
        * Pass
    * Completed
        * Pass
    * Revisiting
        * Pass
* Only a logged in user will have access to this section
    * Pass
* Once a user has updated their status it will reflect at the top of the Step Detail page as the latest saved status
    * Pass
    
#### User Stories
As **a User** I can **update my step status and add comments** so that **I can track my progress through the Design Thinking journey.**

As a **User** I can **update my step progress status and it will reflect correctly across all site pages** so that **I can compare my progress across the steps**.

#### Acceptance Criteria
  
* A Progress Status section is available to a logged in user within the Step Detail page
    * Pass
* A site visitor will see a default message within the section
    * Pass
* The user will be able to select and save a new progress status
    * Pass
* The status will reflect at the top of the Step Detail page as well as on the Step List page
    * Pass
* The user can create and save progress comments
    * Pass
* The comments will display in the Progress Status section on the Step Detail page
    * Pass
* Visitors have the status 'Not Started' per step across all pages
    * Pass
* If a logged in user has not updated all statuses or a status, all statuses or each individual status not updated will reflect as 'Not Started'
    * Pass
* A logged in user's status per step will reflect as selected status once updated
    * Pass    
#### Step Progress Status Desktop
![Step Progress Status Section Desktop](https://github.com/claire-potter/xperience-dezignwiz/blob/main/documentation/features/09.step-details-step-updates-desktop.JPG)

#### Progress Form Mobile
![Step Progress Form](https://github.com/claire-potter/xperience-dezignwiz/blob/main/documentation/features/08.step-details-four-progress-mobile.JPG)

#### Progress Status Updated
![Step Progress Updated](https://github.com/claire-potter/xperience-dezignwiz/blob/main/documentation/features/08.step-details-five-progress-updated-mobile.JPG)

#### Progress Status Section if not logged in

![Progress Status if not logged in](https://github.com/claire-potter/xperience-dezignwiz/blob/main/documentation/features/09.step-details-seven-step-updates-not-logged-in.JPG)

#### Comments
* The Comments section contains a comments form used to capture any relevant progress comments
    * Pass
* The comment once saved will only display to the logged in user
    * Pass
* The user can capture and save the form from this section
    * Pass
* When they navigate back to the specific step detail page, they can view their captured comment
    * Pass

#### Comments Form Mobile
![Comments Form Mobile](https://github.com/claire-potter/xperience-dezignwiz/blob/main/documentation/features/09.step-details-six-comments-mobile.JPG)

#### Comments Updated
![Comments Updated](https://github.com/claire-potter/xperience-dezignwiz/blob/main/documentation/features/09.step-details-six-comments-display-mobile.JPG)


### Feature: Step Tools
* When a step tool link is selected the step tool page will open
    * Pass
* The page is styled as per the step detail page with a unique image per tool and an accordion with the content
    * Pass
* A return button is found at the end of the step tool page so that the user can easily navigate back to the step detail page
    * Pass
    
As **a User** I can **Return to the previous page** so that **When I follow an internal link, I can easily return to where I was within the design process**

#### Acceptance Criteria
  
* Return links open the previous page that the user had open
    * Pass
* This is unless the link will create a loop, then it will return to the most logical page
    * Pass
* A user is always able to navigate back to where they were previously unless it is not possible to do so
    * Pass
    
#### Desktop site
![Step Tool Page Desktop](https://github.com/claire-potter/xperience-dezignwiz/blob/main/documentation/features/10.step-tools-desktop.JPG)

#### Mobile Site
![Step Tool Mobile Page](https://github.com/claire-potter/xperience-dezignwiz/blob/main/documentation/features/10.step-tools-mobile.JPG)

### Feature: Survey - from Empathy Step
* The Survey is a tool utilised within the empathy step
    * Pass
* A section is specifically created to display on the empathy page to provide a user the link to create surveys.
    * Pass

#### Survey from Empathy Step
![Survey from Empathy Step](https://github.com/claire-potter/xperience-dezignwiz/blob/main/documentation/features/11.step-tools-survey-from-empathy.JPG)

### Feature: Survey - List
* When the Survey tool is selected from the Empathy Step or from the main menu link, the user will be directed tot the Survey List page
    * Pass
* If the user is not logged in, they will be redirected to the Login screen
    * Pass
* If a user has not created any surveys, a message saying so will display
    * Pass
* A button to the create survey page will display
    * Pass
* If they have created surveys, the Survey Title, creation data and time, edit/view link and delete link will display
    * Pass
* If the Survey is still in draft mode the edit link will display
* If the Survey is activated the view link will display
    * Pass
    
#### User Story

As **a User** I can **create a new survey** so that **I can interact with customers/clients/users of my product to gather data and receive user input/feedback**

#### Acceptance Criteria
  
* When a user is logged in they have access to the survey tool from the Empathy page
    * Pass
* They also can access the survey tool from the Survey menu link. A non-logged in user will be directed to the login page.
    * Pass
* When the user opens the Survey page, they will see a list of their created surveys, if already created.
    * Pass
* The user will have the option to create a new survey
    * Pass
* When the user selects the option to create a new survey, the Customise your own Design Thinking Survey page opens
    * Pass
* The user will enter and save a Survey Title to the Survey form and select create to save the form
    * Pass
    
#### Desktop Site
![Survey List Desktop](https://github.com/claire-potter/xperience-dezignwiz/blob/main/documentation/features/12.survey-list-desktop.JPG)
#### Mobile Site
![Survey List Mobile](https://github.com/claire-potter/xperience-dezignwiz/blob/main/documentation/features/12.survey-list-mobile.JPG)
#### Survey List - No Surveys
![Survey List -No Surveys](https://github.com/claire-potter/xperience-dezignwiz/blob/main/documentation/features/12.survey-list-desktop-no-surveys.JPG)

#### Survey Create

* The button will open the page for the user to create a new survey
    * Pass
* The user will be able to save a new Survey Title
    * Pass
* A default Survey Title will display
    * Pass
* Once the user submits, the draft survey us created
    * Pass

#### Desktop Site
![Survey Create Desktop](https://github.com/claire-potter/xperience-dezignwiz/blob/main/documentation/features/13.survey-create-desktop.JPG)

#### Mobile Site
![Survey Create Mobile](https://github.com/claire-potter/xperience-dezignwiz/blob/main/documentation/features/13.survey-create-mobile.JPG)

### Feature: Survey Default Questions
* After the survey title is created the user is directed to the default questions page
    * Pass
* They are provided with a view of all of the default questions and answer options that will automatically be added to the survey
    * Pass
* They will only have the option to accept and proceed as all surveys are set up to include the generic questions
    * Pass
#### User Story

As **a User** I can **include predefined questions and answers** so that **it simplifies the survey creation process by providing generic questions and options**

#### Acceptance Criteria
  
* The user will be presented with the predefined questions and associated answer options
    * Pass
* The user will be able to read through th content
    * Pass
* The user will choose to accept the default questions and options
    * Pass
* The default questions and options will now be included in their survey
    * Pass

#### Desktop Site
![Survey Default Questions Desktop](https://github.com/claire-potter/xperience-dezignwiz/blob/main/documentation/features/14.survey-default-questions-options-desktop.JPG)
#### Mobile Site
![Survey Default Questions Mobile](https://github.com/claire-potter/xperience-dezignwiz/blob/main/documentation/features/14.survey-default-questions-options-mobile.JPG)


### Feature: Survey - Add Questions and Options
* The user will have the option to create their own custom questions for their survey
    * Pass
* They have to add at least one question
    * Pass
* If they choose to cancel and exit, they will be taken to the Survey Edit page, for the draft survey
    * Pass
* When a question is saved, the user is directed to add answer options for the question
    * Pass
* The User will need to add at least one option per question and save
    * Pass
* They are then taken back to add the next question
    * Pass
    
#### User Story

As **a User** I can **add my own questions and answer options** so that **I can customise the survey according to my project requirements whilst still being able to analyse the feedback once received**

#### Acceptance Criteria
  
* A user can add their own question content and save their content
    * Pass
* A user can add answer options per question and save their content
    * Pass
* A user can continue adding questions and options until their requirements have been met
    * Pass
* The questions and correct options will be included in the survey for the surveyee to answer as radio buttons to ensure that the feedback can still be analysed
    * Pass
* Once they have added all their questions they can choose to Activate the survey
    * Pass

#### Desktop Site
![Survey Create Question Desktop](https://github.com/claire-potter/xperience-dezignwiz/blob/main/documentation/features/15.survey-create-question-desktop.JPG)
#### Mobile Site
![Survey Create Question Mobile](https://github.com/claire-potter/xperience-dezignwiz/blob/main/documentation/features/15.survey-create-question-mobile.JPG)
#### Cancel Add Question
![Cancel Add Questions](https://github.com/claire-potter/xperience-dezignwiz/blob/main/documentation/features/15.survey-create-question-cancel-to-edit-desktop.JPG)

### Desktop Site
![Add Option Desktop](https://github.com/claire-potter/xperience-dezignwiz/blob/main/documentation/features/16.survey-create-option-desktop.JPG)

### Mobile Site
![Create Option Mobile](https://github.com/claire-potter/xperience-dezignwiz/blob/main/documentation/features/16.survey-create-option-mobile.JPG)

### Create Second Option
![Create second option](https://github.com/claire-potter/xperience-dezignwiz/blob/main/documentation/features/16.survey-create-option-second-mobile.JPG)

### Activate Survey
![Activate Survey](https://github.com/claire-potter/xperience-dezignwiz/blob/main/documentation/features/17.survey-create-add-second-question-or-activate.JPG)

### Feature: Send Survey

* The site has been integrated with the third party Sendgrid functionality to be able to send out emails
    * Pass
* Once the survey is activated the user will be taken to send out their email
    * Pass
* A default subject is provided
* The user is able to add multiple email addresses
    * Pass
* Default message content is added which the user can edit
    * Pass
* The URL for the survey will be added to the email for the user before it is sent out
    * Pass
* When the user submits the email form the email content will be validated and it will be sent out to all valid email addresses
    * Pass
* If the email is sent, a confirmation message will display
    * Pass
* The email content will be added to the email template created in Sendgrid and delivered to the valid email address/es
    * Pass

#### User Story

As **a User** I can **send out the Survey directly from within the site to multiple email addresses** so that **I can manage sending the survey and receiving feedback from one platform with ease**

#### Acceptance Criteria
  
* Once the user has activated the survey they are directed to a page to send out the survey via email
    * Pass
* A default subject will be suggested as 'XperienceDezignWiz Survey', however, the user can still update the subject
    * Pass
* The user is able to capture multiple email addresses to send the survey out to.
    * Pass
* The user is able to add content to the default message: You have been sent a survey to complete.
    * Pass
* The survey url will be added to the email for the user
    * Pass
* The user can send out their message and receive a confirmation
    * Pass
* The email will be delivered to viable email addresses
    * Pass
    
#### Desktop Site
![Send Email Desktop](https://github.com/claire-potter/xperience-dezignwiz/blob/main/documentation/features/18.send-survey-desktop.JPG)
#### Mobile Site
![Send Email Survey](https://github.com/claire-potter/xperience-dezignwiz/blob/main/documentation/features/18.send-survey-mobile.JPG)
#### Email Sent message
![Survey Sent](https://github.com/claire-potter/xperience-dezignwiz/blob/main/documentation/features/18.email-sent-mobile.JPG)

#### Email Delivered
![Email Delivered](https://github.com/claire-potter/xperience-dezignwiz/blob/main/documentation/features/19.email-template.JPG)

### Feature: Start Survey

* The surveyee can open the survey link received to start the survey
    * Pass
* A login button is also provided in the template to encourage existing users to login or new users to create an account
    * Pass
* The user will be taken to the start survey page which will display a default survey image and the survey title with a link to begin the survey
    * Pass
* When the button is clicked the surveyee will be taken to complete their answers
    * Pass

#### Desktop Site
![Start Survey Desktop](https://github.com/claire-potter/xperience-dezignwiz/blob/main/documentation/features/20.start-survey-desktop.JPG)

#### Mobile Site
![Start Survey Mobile](https://github.com/claire-potter/xperience-dezignwiz/blob/main/documentation/features/20.start-survey-mobile.JPG)

### Feature: Complete and Submit Survey

* The surveyee can proceed to answer the survey without having to login
    * Pass
* The surveyee will select an answer from the dropdown menus for all of the default questions
    * Pass
* The surveyee will select an answer from the custom question by using the radio buttons
    * Pass
* The surveyee is required to select an answer
    * Pass
* The surveyee submits their survey successfully
    * Pass
* A thank you message is displayed with a link to the home page to be taken back to check out the rest of the site
    * Pass

#### Desktop Site
![Complete Questions Desktop](https://github.com/claire-potter/xperience-dezignwiz/blob/main/documentation/features/21.answer-default-questions-desktop.JPG)
#### Mobile Site
![Complete Questions Mobile](https://github.com/claire-potter/xperience-dezignwiz/blob/main/documentation/features/21.answer-default-questions-mobile.JPG)
#### Answer Required
![Required Answers](https://github.com/claire-potter/xperience-dezignwiz/blob/main/documentation/features/21.answer-default-questions-required.JPG)

#### Thank you message
![Thank you message](https://github.com/claire-potter/xperience-dezignwiz/blob/main/documentation/features/22.survey-thank-you-desktop.JPG)

### Feature: Survey Details - Results
* The Survey Detail page, accessed through the view button on the Survey List page contains the following content"
    * Number of Submissions
        * Pass
    * Link to Start Survey
        * Pass
    * Age Question Doughnut chart
        * Pass
    * Age Question table of results - percentages
         * Pass
    * Gender Question Doughnut chart
         * Pass   
    * Gender Question table of results - percentages
         * Pass   
    * Industry Question Doughnut chart
        * Pass
    * Industry Question table of results - percentages
         * Pass   
    * Custom Questions 
         * Pass   
    * Custom Option selection - percentages
        * Pass
* The return button takes the user back to their list of surveys
        * Pass


#### User Stories

As **a User** I can **review Survey feedback** so that **I can understand my customer/client/users**

As **a User** I can **delete a survey** so that **I have the option available if the survey is no longer required**

#### Acceptance Criteria
  
* A user can view how many surveys have been submitted
    * Pass
* A user can view doughnut charts and tables containing the default question and answer data
    * Pass
* A user can view a summary of the questions they created and the options that users have chosen as a percentage
    * Pass
* A user can access the survey start page from the survey detail page
    * Pass
* The user has the option to delete a survey from the survey list page
    * Pass
* The user can select to delete the survey
    * Pass
* The user deletes the survey and a success message is displayed
    * Pass

#### Desktop Site
![Survey Detail part one desktop](https://github.com/claire-potter/xperience-dezignwiz/blob/main/documentation/features/23.survey-detail-part-one-desktop.JPG)
![Survey Detail part two desktop](https://github.com/claire-potter/xperience-dezignwiz/blob/main/documentation/features/23.survey-detail-part-two-desktop.JPG)

#### Mobile Site
![Survey Detail part one mobile](https://github.com/claire-potter/xperience-dezignwiz/blob/main/documentation/features/23.survey-detail-part-one-mobile.JPG)
![Survey Detail part two mobile](https://github.com/claire-potter/xperience-dezignwiz/blob/main/documentation/features/23.survey-detail-part-two-mobile.JPG)

#### Delete Survey
![Survey-delete](https://github.com/claire-potter/xperience-dezignwiz/blob/main/documentation/features/23.survey-delete.JPG)

### Feature: Search for a Step

* The search feature allows the user to search by Step Title for a Step
    * Pass
* An autocomplete list has been set up in javascript file, to match what the user types in, and return the step title which matches
    * Pass
* When the user enters the searched term, the search page, specific per step is returned with a link to open the step
    * Pass
* If an incorrect term is search or if the search form is submitted with an empty search, the page returned  provides the user with the links to each step page, so that they are able to access whichever page they require
    * Pass
    
#### User Story 

As **a User** I can **search for a Step** so that **I can access each step as and when required**

#### Acceptance Criteria
  
* A step search input field is available to the user across all pages
    * Pass
* When the user starts to type, they are prompted to select the correct step name
    * Pass
* The search displays the correct step searched for
    * Pass
* If a blank search or incorrect search term are run, all step pages links are returned for the user to choose between
    * Pass
  
#### Desktop Site
![Search desktop](https://github.com/claire-potter/xperience-dezignwiz/blob/main/documentation/features/24.search-step-desktop.JPG)
![Search-results-desktop](https://github.com/claire-potter/xperience-dezignwiz/blob/main/documentation/features/24.search-results-desktop.JPG)

#### Mobile Site
![Search mobile](https://github.com/claire-potter/xperience-dezignwiz/blob/main/documentation/features/24.search-step-mobile.JPG)
![Search results mobile](https://github.com/claire-potter/xperience-dezignwiz/blob/main/documentation/features/24.search-results-mobile.JPG)

#### Search - None
![Search None](https://github.com/claire-potter/xperience-dezignwiz/blob/main/documentation/features/24.search-none.JPG)

