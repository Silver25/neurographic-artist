
# Neurographic Art

![Am I responsive](readme_assets/image00.png)  
- In a lack of Responsive view generator [https://ui.dev/amiresponsive] above image cover some minimum preview  

## Purpose

The objective of this project is to create a responsive website utilizing Python/Django, JavaScript, HTML, and CSS (Bootstrap), 
representing a full stack development approach.  

At present, the project serves solely educational purposes and bears no connection to any existing real-life counterparts. 
The content of the website is tailored for individuals seeking tranquility and relaxation. 
Users will have the ability to explore the website through an operational navigation bar that directs them to various sections of the site.  

Furthermore, the website provides an engaging experience of contemporary web dynamics by facilitating visitor interaction with forms and content modification.

## Description [Interactive Responsive Website]

Discover the World of Neurographic Art: Transform Your Mind, Emotions, and Creativity  

Welcome to your ultimate resource for understanding and exploring Neurographic Art.  
A transformative and meditative art form that melds psychology, neuroscience, and creativity.  
On this site, you'll delve into the fascinating world of this unique technique, where simple lines and shapes evolve into intricate, meaningful compositions.  

Live site reachable at https://neurographical-915fed1a7d6c.herokuapp.com/

## UX Design

### User Stories
- Kanban board created as a GitHub Issues: https://github.com/users/Silver25/projects/3  
![user-stories-template-setup](readme_assets/image18.png)  
![user-stories-template-setup](readme_assets/image19.png)  
![user-stories-template-setup](readme_assets/image20.png)  
![user-stories-template-setup](readme_assets/image21.png)  
![user-stories-template-setup](readme_assets/image22.png)  
![user-stories-template-setup](readme_assets/image23.png)  
![user-story-create](readme_assets/image24.png)  
![user-story-create](readme_assets/image25.png)  
![user-story-create](readme_assets/image26.png)  


### Wireframes

- Wireframe for desktop visual  
![Home page wireframe](readme_assets/image91.png)  

### ERD (Entity Relationship Diagram) visualisation

An Entity Relationship Diagram (ERD) is a type of diagram that lets you see how different entities 
(e.g. people, customers, or other objects) relate to each other in an application or a database.  

![Entity Relationship Diagram](readme_assets\ERD_visual.webp)

### Colour Scheme

- Basic colour for the font and background is WHITE
- other colours as follows:  
![Colour Scheme](readme_assets/image92.png)

### Typography

- Font family: Lato, sans-serif

## Features

- Top/main Menu  
![Main menu on the top](readme_assets/image36.png)  
- Hero image with Readme more link  
![Hero image and button](readme_assets/image50.png)  
- Newsletter subscribtion Form  
![Newsletter Form](readme_assets/image51.png)  
- Footer  
![Footer with copyright and links](readme_assets/image38.png)  
- Journal page - post listing  
![List of published posts](readme_assets/image39.png)  
- Journal page - post listing with post images  
![Post image above the title](readme_assets/image45.png)  
- Navigation through all published posts  
![Navigation through post listings](readme_assets/image40.png)  
- Comment form -  allow registered users to create a new comment  
![Comment form for related post](readme_assets/image35.png)  
- Published comments preview with total number of comments for the related post  
![Display of the comments](readme_assets/image34.png)  
- Comment Edit button - for the registered users with the option to edit a existed comment  
- Comment Update button - for the registered users with the option to update a existed comment  
![Edit and Delete buttons for User](readme_assets/image54.png)  
- About page  
- Successful login, logout, submit, update and subscription messages for the user on the top  
![Top page msg for login](readme_assets/image33.png)  
![Top page msg for logout](readme_assets/image42.png)  
![Top page msg for submited form](readme_assets/image37.png)  
![Top page msg for subscription](readme_assets/image47.png)  
- Login form  
![Sign In page with form](readme_assets/image32.png)  
- Logout choice  
- Sign out page with second level action to confirm choice  
![Sign/Log out page](readme_assets/image41.png)  
- Signup form  
![Signup form](readme_assets/image56.png)  
- Social Media links  

### Future Features

- On mobile devices, the featured image is displayed below the title
- Registered User can modified and delete post with assigned Role
- Unsubscribe from newsletter list link/button
- Cookie Consent Popup
- Freebies page


## Testing
- Results of testing available on another file [Testing.md file](Testing.md)  

## Deployment

### Local deployment on workstation
- from installation of Python on Windows OS to runing project in the browser
- setup of the environment on computer with installation of VS Code, Python and Git
- installation of needed extensions for VS Code
- saving global credentials for Git [for connection from VS Code to GitHub]
- test of installed components
- Organize a *folder structure* - main folder for all Projects ...
- .. and with copy of the repository/clone, subfolder for each project creates VS Code
- clone of remote/GitHub repository download last version of the code, files and attachments
- for fully functional project to run locally on a computer it's important to install all dependencies
- with command in terminal: pip install -r requirements.txt VS Code will install everything from the list

### Setup and startup of the Project in Cloud
- Create new GitHub repository from template
![New repo creating](readme_assets/image01.png)  
- Apply settings for new repo
![New repo apply](readme_assets/image02.png)  
- Start Gitpod Dashboard to create new Workspace
![Gitpod new Workspace](readme_assets/image03.png)  
- Chosen project starting preparation
![Preparing Workspace](readme_assets/image04.png)  
- Building Workspace with all necessary elements
![Building image for the Workspace](readme_assets/image05.png)  
- Installed Django using the following command in the Terminal: pip3 install Django~=5.1.4
- Added the package to the requirements.txt file with the command: pip3 freeze local > requirements.txt
- Creating the Django Project in Terminal:
  - Created the new project, "Neurographic", using the Django built-in function: django-admin startproject neurographic .
- Creating the new app in Terminal:
  - Created the new app: about, using the Django built-in function: python3 manage.py startapp about
![Creating the new app](readme_assets/image06.png)  
  - Added the app to the list of installed apps in neurographic/settings.py
  - Imported HttpResponse from django.http and view function in about/views.py
  - Imported the about view and added the new path to the urlpatterns in neurographic/urls.py
  - Created new class 'Post' as a model of the app Journal and register for the Django and database
  ![New Post model created](readme_assets/image29.png)  
  - Post model displayed in Django administration area
  ![Post model in Django](readme_assets/image30.png)  

### Heroku deployment
- Dashboard -> Button 'New' -> Create new app
![Create New App](readme_assets/image08.png)  
- New App details -> name + Region -> Button 'Create app'
![New App details](readme_assets/image09.png)  
- Heroku App -> Settings tab -> Config Vars Reveal
![Reveal Config vars for App](readme_assets/image10.png)  
- Config Vars new key 'DISABLE_COLLECTSTATIC' set to '1'
![Config Vars key](readme_assets/image11.png)  
- Gitpod IDE Terminal -> Gunicorn server preparation setup
![Gunicorn server preparation](readme_assets/image12.png)  
- Terminal -> Procfile created -> Heroku as ALLOWED_HOSTS
![Heroku settings for server](readme_assets/image13.png)  
- Heroku connecting to GitHub project
![Heroku connects GitHub](readme_assets/image14.png)  
- Heroku App -> Deploy tab -> Deployment method -> GitHub -> Connect to GitHub -> Authorize Heroku
  -> Popup window -> Sign in to GitHub -> Search for gitHub project
- Manual deploy -> Deploy a GitHub branch -> Deploy Branch button
![Heroku deploys app from GitHub](readme_assets/image15.png)  
- Receive code from GitHub -> Build main ...
- Your app was successfully deployed. -> View button
![Deployed App access with the View button](readme_assets/image16.png)  
![App successfully started](readme_assets/image17.png)  
- Connection with Database, creating the tables and Admin credentials in IDE
![Connected with db](readme_assets/image27.png)  
- Connection with the Database on Heroku  
![Heroku creds for db](readme_assets/image28.png)  
- Remove Config Vars key 'DISABLE_COLLECTSTATIC' so Heroku can use static files
![Enable static files on Heroku](readme_assets/image31.png)  

## Technologies
- HTML language
- Bootstrap [CSS] framework
- Python language
- Django framework
- Postgres database
- JavaScript

## Tools
- Visual Studio Code code editor [https://code.visualstudio.com/]
- Git version control system [https://git-scm.com/]
- Gitpod online code editor [https://www.gitpod.io/]
- GitHub developer platform [https://github.com/]
- Agile technique - GitHub Issues tables [Kanban board]

## Credits [Acknowledgments]

- Images and photographs created by Me, Myself and I  
- Font style created by Google Fonts [https://fonts.google.com/]  
- Footer icons provided by Font Awesome [https://fontawesome.com/icons]  
- FotoJet - creating photo collages [https://www.fotojet.com/]  
- Photovisi photo collage maker [https://www.photovisi.com/]  
- Pixlr's online collage maker [https://pixlr.com/photo-collage/]  
---

- Online simple Kanban style task process board [https://notepad.js.org/kanban/]  
- Google Translate [https://translate.google.com/]  
- Control Vi to edit and download image from clipboard [https://ctrl.vi/]  
- Folge - paste image from clipboard to download [https://folge.me/tools/]  
- Lorem Ipsum - generator of dummy text [https://www.lipsum.com/]  
- Quillbot Fix grammar, spelling, and punctuation errors [https://quillbot.com/paraphrasing-tool]  
- Humanize AI-generated content into natural, human-like text [https://www.humanizeai.pro/]  
- Wireframe accomplished with online tool [https://wireframe.cc/]  
- Colour palette generator [https://coolors.co/]  
- DbSchema universal database tool for ERD visualisation on Windows  
---

- Complete Basic Django Series [https://djangotherightway.com/]  
- Content made for the Django Community [https://django.wtf/]  
- Answers and suggestions [https://stackoverflow.com/tags]  
- Creating Readme [https://github.com/kera-cudmore/readme-examples]  
- Code Institute Solutions [https://github.com/Code-Institute-Solutions/blog/tree/main]  
- Git documentation [https://git-scm.com/doc]  
- DevTools documentation [https://learn.microsoft.com/en-gb/microsoft-edge/devtools-guide-chromium/landing/]  
- Google Dev Sources [https://developers.google.com]  
- Art & Object [https://www.artandobject.com/]  
- Irish Journal of Psychological Medicine [https://www.cambridge.org/core/journals/irish-journal-of-psychological-medicine]  
- American Psychological Association [https://psycnet.apa.org/home]  
---
I would like to express gratitude to **[Code Institute](https://codeinstitute.net/ie/)** and **walk through** project for offering a valuable step-by-step guide that was instrumental in creating the basis for this website.  
Last but not least is big THANKS to my mentor **Rory** for guidance and sugestions through project.
