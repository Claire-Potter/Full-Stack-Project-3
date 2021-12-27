# Xperience DezignWiz
## About this project:

The Design Thinking Process is used by multiple industries to assist project teams to solve business needs by coming up with user-centric solutions, including prototyping the solution and testing it followed by revisiting and reworking the solution concept. The focus is on the user and the user's needs. It consists of five steps: Empathy, Define, Ideate, Prototype and Test.

The purpose of Xperience DezignWiz is to create a step by step approach for those who are new to the Design Thinking Process, to be able to understand each Design Thinking Step, provide tools relevant to the step to assist the user to complete the step and to be able to track their progress within each step. The key tool provided is a Survey tool, which allows the user to create and send their own surveys. A survey submissions summary is provided with charts, allowing the user to analyse their data to understand their user-base. This is very helpful to assist the user to move on to completing personas. The user can go back and fourth between the various steps and the process does not have to be completed sequentially.

As the user comes to the conclusion of the Design Thinking Process, they should have received the necessary information and support tools to be able to successfully implement the process.

This site has been completed as  a minimum viable
product and hopefully in time, the functionality can be extended.

The project is developed using Django, Python, JavaScript, HTML, CSS, and the Bootstrap framework.

This is currently a test project.

Table of Contents

# Ux Design

## User Stories

**Project Goals:**

**Users**
1. Contact the site owner directly through a form
2. Register to create  an account to have access to utilise the Step Updates section, the Survey tool or to answer a Survey.
3. Complete functionality / access all features as created within the User Stories for the role: User.

**Survey Takers**
1. Receive a Survey via email
2. Open the Survey link
3. Successfully complete the Survey
4. View XperienceDezignWiz Site


**Site Administrator**
1. Receive contact forms through Django admin and direct email message.

2. Edit:

    * Home Page Image
    * Step fields: 
        * feature image
        * steps image
        * excerpt
        * body
        * resources
        * tools
        * view all other fields
    * Tool fields:
        * excerpt
        * body
        * image
        * view all other fields
    
 3. View only
    * Default Questions
        * Age 
        * Gender
        * Industry
    * Default Options
        * Age
        * Gender
        * Industry
        
4. View/Edit/Delete:
    * All Steps Pages Images (Images)
    * Resources
    * Surveys
        
5. Maintain user data:

    * View/Delete:
        * Progress Status - users
        * Comments
        * Surveys
        * Questions
        * Options
        * Submissions
        * Default Question Answers
        * Answers
        * Contact Requests

6. Add:

    * Tool


**User Stories:**

You can view an organised board with all user stories here:

<a href="https://github.com/Claire-Potter/Xperience-DezignWiz#workspaces/xperience-dezignwiz-project-61c62eda01f3f500100e5fdc/board" target="_blank">User Stories</a>

## Strategy

### High-level Business Goals

 - Create a well thought-out and user friendly website.
 - All content to be concise and easy to understand.
 - The purpose of the website is to help new users of the Design Thinking Process
 - To be utilised by students, educational institutions and work places to assist new design thinkers to successfully work through the design thinking process and implement the steps

### Value

The value lies in providing the content in an easy to use way to allow the new design thinker to understand the concept of design thinking, the purpose of each step and how to implement each step as quickly as possible. The tools should provide some guidance and ideas.
The survey tool will allow them to interact with their customer/client base or potential user to receive their input and feedback.
As users of the site successfully work through the Design Thking process and use the site to track their progress, interact through and learn from, the greater the use of the site will be.

### Why is this site so special?

There are multiple sites and tools available with Design Thinking process content and tools. 

What makes this site special:

 - The site works through and presents each step in a logical fashion
 - The ability to update your personal progress against each step
 - Many sites only contain written content, or there is a video on You Tube or the site is a set up as a tool to assist with one stage within the process.
 - The way the site is packaged is to look at the process as a whole whilst still providing detailed content as well as implementation tools for each individual step.
   
### Trade-offs

| Opportunity                                                                                                                                   | Importance | Difficulty |
|-----------------------------------------------------------------------------------------------------------------------------------------------|------------|------------|
| Navigation across the site                                                                                                                    | 5          | 1          |
| Home Page with site purpose                                                                                                                   | 4          | 1          |
| Steps Overview including progress status, resource and tool count                                                                             | 5          | 2          |
| Step Detail page with content, linked resources, linked tools and progress status section                                                     | 5          | 3          |
| Linked videos as resources                                                                                                                    | 4          | 2          |
| Linked tools with information                                                                                                                 | 4          | 1          |
| Ability to search for a step                                                                                                                  | 3          | 2          |
| Ability to create a survey                                                                                                                    | 4          | 3          |
| Ability to send out a survey                                                                                                                  | 4          | 3          |
| For Survey Users to access and complete the survey                                                                                            | 4          | 1          |
| Ability to review the survey results and track submissions                                                                                    | 4          | 4          |
| Limit what logged in users can see and do vs. what site visitors can see and do                                                               | 4          | 2          |
| Provide access to the Admin page for a Site Administrator to perform certain functions                                                        | 4          | 2          |
| Contact form for all site users and visitors to contact administration via, to be sent out via email and to be received within the admin page | 4          | 3          |
| Create a persona with the data from the survey                                                                                                | 3          | 4          |
| Integrate with a third party tool to use as a project board for ideation, provide documentation and guidance on the tool                      | 2          | 4          |
| Provide prompts to the user within the step to assist the user to move forward. Provide certain progress milestones for the user to meet      | 2          | 4          |
| Provide PDF functionality to allow the user to download and save all their documentation                                                      | 3          | 4          |


Using the trade-off process to rank the importance and feasibility of the opportunities I have decided:

1. To go ahead with 14/18 of the opportunities.
2. Given the timeframe and my current skill as a developer, I have to narrow down the scope of the deliverable and focus on the core functionality.
3. Including one functional tool - the survey will assist me to ensure the project is completed.

## Scope

For this project, the main aim is to create a simple platform to guide a user through the design thinking process without overwhelming them. Secondary to that is to provide the user with the necessary information required to be able to implement each design thinking step. The website will be designed to render successfully across all screen sizes and platforms. Accessibility requirements will be considered and addressed. Apart from the default Django Admin centre, which is best utilised from a laptop/computer, the design has been completed for mobile first.

In order to create a flowing design, two additional steps have been added to the five design thinking steps. Number one - Getting Started, provides an overview of the design thinking process and Finishing Off provides a round up of the process as well as an explanation of storytelling. The steps will be put together based on the Code Institute Design Thinking resource videos and utilising content from Design Thinking sites.

To provide an overview of the design thinking steps, two pages containing step summary cards will be created. A user can easily scroll between the two pages and view the step name, a relatable image, access the detailed step page from the step link and view their progress status (users who are not logged in or those who have not updated their status) will see a default status of Not Started and number of resources and tools available per step.

Users who have registered for an account will have the additional option of creating their own update statuses and adding and saving comments to the step detail page. This way they can track the progress they make as they work through each design thinking step. They will also have the ability to be able to create and send out their own surveys. They will also be able to track and view the feedback they receive from their clients/customers, which will be really useful to assist them to understand their users' needs.

Site Administrators will have access to the Admin section which allows them to view and monitor site content and assist where required.

The Super User will have additional access to the Admin section. Certain models will be limited in terms of being able to create, delete or edit content.

## Structure

### Skeleton

Below is an image of the site structure, excluding the survey, as login is required to access.


<a href="https://github.com/Claire-Potter/Xperience-DezignWiz/blob/main/documentation/design/site-map/site-map.pdf" target="_blank">Site Map</a>

The survey basic structure is as follows:

<a href="https://github.com/Claire-Potter/Xperience-DezignWiz/blob/main/documentation/design/site-map/survey-journey.JPG" target="_blank">Survey Journey</a>


### Access

This website will allow users to access different parts of the site depending on whether they're logged in/have an account. 


#### Site visitors: 

Can access the home, steps summary, step search, and step details pages. They will not be able to update their progress status or add comments on the step detail page. The progress status on the step page will reflect as 'Not Started'. They will not have access to the survey functionality, apart from being able to answer a survey. They will be able to use the contact form to contact the site admin. They will have access to register an account.

#### Registered users:

Can login to the site. Once logged in, they will have access to update their progress per step as well as to add comments. They will have access to the tools material. They will have access to create surveys, add their own questions and answer options, send out the survey and view the survey results. They are able to save the survey as a draft, and come back at a later stage to edit. If they no longer need the survey, they are able to delete it. They are able to perform the following account maintenance: reset a password by sending a link to their email, update their email address, add an additional email address, change the primary email address and resend the verification email. 

#### Site administrators and Superusers: 

Can add, edit, delete site content. Site admin have a limited view and functionality within the admin section. Superusers will have additional access except for certain models and fields for which the ability to create, delete or edit has been restricted to maintain data integrity.

If the user tries to access a page with the incorrect permissions, they will be redirected to the login screen.

## Wireframes

The original wireframes created are saved as wireframes-desktop and wireframes-mobile.
### Differences:
1. The original survey was designed to be completed as a single page, with surveys access through cards at the end of the page. As I ended up using a blueprint and templates, the wireframes for the survey can be seen in the survey folder. All of the templates were adjusted to meet the site requirements and to be styled as per site design. This includes adding the templates for selecting the default options, answering the default questions, sending the email and displaying the default answer results as charts.
2. The auths account default templates for login, logout, register etc were utilised and fully styled to match the site design.
3. The Contact page was added later, and the Code Institute Resume Project -Contact template provided the template. It was fully customised to meet site design and requirements.

Please <a href="https://github.com/Claire-Potter/Xperience-DezignWiz/tree/main/documentation/design/wireframes" target="_blank">click here</a> to view all wireframes


## Design
### Colours

The colours for this site are based on the below image:

![Colour Image](https://github.com/Claire-Potter/Xperience-DezignWiz/blob/main/documentation/design/colour-scheme/inspiring-website-color-schemes.png raw=true)

The pink-blue combo is among the most preferred colour mixes that please the eye. For this website design, the designer has chosen several nuances of pastel blue jazzed up with energizing pink. I found the image on the following site:

https://graphicmama.com/blog/website-color-schemes/

I find the colour scheme to be young and fun whilst still simple and sophisticated. It creates a calming atmosphere perfect for taking in information. I used the colour scheme across the site to keep the consistency and flow.


### Fonts
The logo font for the site is 'Mochiy Pop P One' with the default font set as sans-serif.

The main font used across the body is 'Dongle' with the default font set as sans-serif.

These fonts were chose to be easy to read and have a young and casual look.

# Database

For development, I used the sqlite3 database that comes with Django. A PostgreSQL database through Heroku is in use 
for the deployed live site.

Please access the app and database file <a href="https://github.com/Claire-Potter/Xperience-DezignWiz/blob/main/documentation/apps-and-models/apps-and-models.md" target="_blank">here</a> 


 <a href="https://github.com/Claire-Potter/Xperience-DezignWiz/blob/main/documentation/apps-and-models/apps-and-models.png" target="_blank">Database diagram</a>

 <a href="https://github.com/Claire-Potter/Xperience-DezignWiz/blob/main/documentation/apps-and-models/full-database.png" target="_blank">Database diagram full site</a>

 <a href="https://github.com/Claire-Potter/Xperience-DezignWiz/blob/main/documentation/apps-and-models/survey-data-model.JPG" target="_blank">Survey data model</a>

# Features
 
Please access the features file <a href="https://github.com/Claire-Potter/Xperience-DezignWiz/blob/main/documentation/features/features.md" target="_blank">here</a>

# Technologies used 

## Languages
* HTML5
* CSS3
* JavaScript
* Python
* Dockerfile - Readme

## Agile Planning

* GitHub and ZenHub were used to plan user stories including acceptance criteria and tasks.
* Create and plan Project Backlogs as Milestones.
* Create and plan Integrations as Milestones.
* Create relative estimates and priority ratings. 

## Images
Cloudinary used to crop and style the images
ImageOptimizer used to minify image file sizes.


## Libraries and Frameworks
* Django was used to create templates and manage the project.
* Bootstrap 4 was used to format the site design with their built-in CSS, Popper and JS.
* FontAwesome 5.15.3 is used for social links and the rating stars.
* Google Fonts is used for fonts on the site.
* jQuery to easily manipulate the DOM and update Bootstrap tools that require initialization.
* Chart-js 2.8.0 utilised to render the doughnut charts on the survey detail page including additional scripts for Bootstrap JS, jQuery CDN and Popper.js

## Development tools
* Git is used to track changes made to the repository and for version control.
* GitHub is used to store the project and to share the project.

## Deployment/Hosting
* Heroku is used to deploy and host the live site content.

## Static and media file storage
* Cloudinary is used to store static files and media files so that they work correctly on the deployed site

## Email
* Google cloud is used to verify the name and enable Sendgrid
* Sendgrid is used to integrate, create an email template and send emails

# Testing

Please access the testing pack <a href="https://github.com/Claire-Potter/Xperience-DezignWiz/blob/main/documentation/testing/testing.md" target="_blank">here</a>

# Deployment

## Required technology

This website was developed on Gitpod using the Code Institute  student template with changes frequently committed to git then pushed onto GitHub from the Gitpod terminal. The deployed site utilises the new version of the python template.

The deployed version of the website is the master.

* Django: to create multiple apps in the project and manage templates
* Python3: write the code and run the project through Django
* PIP: install packages
* Git: version control
* Postgre: as the database to create content, add new content, and manage data
* Cloudinary to store all static files
* Sendgrid to send emails
* Heroku: to deploy the project and manage the app

## Maintaining Code

To maintain the code the following actions are taken:

1. Log into GitHub
2. Go to the repositories tab at the top of the screen
3. Click on the repository named XperienceDezignWiz
4. Once in the repository select the green icon GitPod to open the code on GitPod
5. Gitpod will load
6. The XperienceDezignWiz Main branch will open
7. The XperienceDezignWiz folders and files will be visible on the left hand side
8. The credentials file env.py has been added to gitignore as it contains sensitive information. This file will need to be created saved again to the repository
9. You will need to run the following command to install requirements:
    * Pip3 install -r requirements.txt
10. In settings.py ensure Debug is saved as Debug=True, remember to change back to Debug=False before pushing your changes back to GitHub
11. Run the dev site as follows:
    * Python3 Manage.py runserver
12. Create , test and save the change required to the relevant file
13. To save the changes back to github the following process needs to be followed:

    * clear the terminal by typing in "clear" and pressing enter

    * Add the code to gitpod by typing in "git add ." in terminal and press enter
    
    * Commit the code to gitpod by typing in "git commit -m "Add a short message here" and press enter
    
    * Push the code back down to github by typing in "git push" select enter
    
    * From the github side, refresh the repository page and the commit will reflect
    
    * Open the item to view the commit changes


## Deployment to Heroku
The website was deployed from GitHub to Heroku using the following steps:

1. Create a new application in Heroku:

    * Navigate to Heroku.com and login.
    * Click on the new button.
    * Select Create New App.
    * Enter a unique app name.
    * Select your current region.
    
2. Set up connection to Github Repository

    * Click the deploy tab and select GitHub - Connect to GitHub.
    * A prompt to find a github repository to connect to will then be displayed.
    * Enter the repository name for the project and click search to find your repository.
    * Click the connect button.
    
3. Add PostgreSQL Database:

    * Click the Resources tab.
    * Under Add-ons seach for Heroku Postgres and then click on it when it appears.

4. Add Dynos:
    * From Git create a procfile with the content: web: gunicorn xperiencedezignwiz.wsgi 
    * Save the changes and push through to GitHub
    * Each dyno in your app belongs to one of the declared process types, and it executes the startup command associated with that process type.
    * Click the Resources tab.
    * Select to create Dynos
    * Select to add free Dynos

5. Set environment variables:
    * Click on the Settings tab and then click reveal Config Vars.
    * Variables added:


        CLOUDINARY_URL

        DATABASE_URL

        DISABLE_COLLECTSTATIC

        SECRET_KEY

        SENDGRID_API_KEY



6. Enable automatic deployment:

    * Click the Deploy tab
    * In the Automatic deploys section, choose the branch you want to deploy from then click Enable Automation Deploys.

## How to Fork the Repository

1. To be able to fork the repository, you will need your own github and gitpod accounts with linked permissions
2. From your github home page in the search bar search for Claire-Potter
3. Under Users select the user Claire-Potter
4. On the repository page choose to open the XperienceDezignWiz repository
5. At the top of the page on the right-hand side select to Fork the repository
6. Your own version of the repository will create
7. Select the green GitPod icon to open the work space on GitPod
8. Follow the steps in the Maintaining Code section above to make and save changes to your own repository
9. Remember you will need to create your own version of the env.py file for the credentials
10. Emails will not work unless you set up your own account with Sendgrid and integrate. Any third party provider can be utilised.


# References

## Code

### General Queries

The following were used for any general queries or guidance required:

1. Code Institute LMS
2. Stack Overflow - https://stackoverflow.com/
3. Django 3.2 Documentation - 
https://docs.djangoproject.com/en/3.2/releases/3.2/

### Code Adaptations

1. The base code for this project is from the Code Institute 'I Think Therefore I Blog' project

2. Contact form is based on the Contact Form from the Code Institute Resume Project

3. Survey app was built by following this tutorial from Matt Segal and the associated github page mentioned within the site https://mattsegal.dev/django-survey-project.html
4. The following tutorial was referenced to build the search functionality and fully customised https://www.youtube.com/watch?v=AGtae4L5BbI
5. Complex lookups with Q objects was referenced here:
 https://docs.djangoproject.com/en/3.2/topics/db/queries/

6. The instruction to create the apps-models.png image were found here:
https://medium.com/@yathomasi1/1-using-django-extensions-to-visualize-the-database-diagram-in-django-application-c5fa7e710e16

7. additional support sourced from stackoverflow:
https://stackoverflow.com/questions/6778439/enable-to-use-django-extensions-with-pygraphviz/48912793

8. The bootstrap sidebar was set up according to: 
https://bootstrapious.com/p/bootstrap-sidebar

9. The following article was referenced to customise crispyforms:
https://simpleisbetterthancomplex.com/tutorial/2018/11/28/advanced-form-rendering-with-django-crispy-forms.html#custom-fields-placement-with-crispy-forms

10. The following tutorial video was followed to embed the videos in Django
https://www.youtube.com/watch?v=dGF1x14QNGA

11. The following site was referenced to complete the html-validator testing - 
https://pypi.org/project/django-html-validator/

12. The following site was referenced to update cloudinary storage - https://pypi.org/project/django-cloudinary-storage/

13. The following site was referenced to remove the has no objects pep8 error - 
https://stackoverflow.com/questions/45135263/class-has-no-objects-member

## Content
2. All videos displayed as Resources are the property of Code Institute and were sourced from the Code Institute You Tube channel. They have been used from project purposes only 
1. The favicon was created on Free Favicon Maker
2. Images sourced through Unsplash and Shutterstock
3. The Design Thinking material was sourced from the following sites and used for project purposes only:

    * https://www.interaction-design.org/literature/article/5-stages-in-the-design-thinking-process

    * https://www.interaction-design.org/literature/article/prototyping-learn-eight-common-methods-and-best-practices

    * https://www.workshopper.com/post/design-thinking-phase-5-how-to-test-effectively

    * https://think.design/user-design-research/surveys/

    * https://uxdesign.cc/how-to-nail-a-user-interviews-in-a-ux-hcd-or-design-thinking-process-full-guide-17d4eeee8dc3

    * https://www.interaction-design.org/literature/topics/personas

    * https://enterprisersproject.com/article/2020/2/design-thinking-how-to

    * https://www.interaction-design.org/literature/topics/storytelling
    
4. The decriptions used for the models were sourced from the following site:
https://www.geeksforgeeks.org/django-model-data-types-and-fields-list/

## Acknowledgements
A huge thank you to my mentor Brian Macharia. The guidance and advice that you have provided has been invaluable.

Thank you to Code Institute for providing such well-thought out and put together course material and for the constant guidance and advice provided through Slack.

Finally, to my wonderful husband and children, thank you for your understanding and support through this process.