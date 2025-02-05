![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

# Neurographic Art

## Purpose

## Description [Interactive Responsive Website]

Discover the World of Neurographic Art: Transform Your Mind, Emotions, and Creativity  

Welcome to your ultimate resource for understanding and exploring Neurographic Art.  
A transformative and meditative art form that melds psychology, neuroscience, and creativity.  
On our site, you'll delve into the fascinating world of this unique technique, where simple lines and shapes evolve into intricate, meaningful compositions.  
Learn about the term “Neurographic Art,” its origins, and its profound impact on personal growth and emotional well-being. Through engaging tutorials and  
insightful articles, we’ll guide you step-by-step, helping you master the techniques that allow your subconscious to speak through art.  
Join our vibrant community of artists and enthusiasts discovering the therapeutic power and boundless possibilities of Neurographic Art.  

Live site reachable at https://neurographical-915fed1a7d6c.herokuapp.com/

## UX Design
Proposed by Jesse James Garrett, this process is represented as five levels of activity called planes.  
These planes and their concerns are as follows.

### Target audience

### First Time Visitor Goals

### Returning Visitor Goals

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
- MoSCow prioritization [for PBIs - Product Backlog Items]:
- Must Have / Should Have / Could Have / Won’t Have (GitHub Issues)
- create user story template file [user-story.md]
- git pull to update preview on Gitpod VS GUI
- write these lines as reminder

### The strategy plane: 
What are you aiming to achieve in the first place and for whom?

### The scope plane: 
Which features, based on information from the strategy plane, do you want to include in your design?
What's on the table for a production release and what's not, at least for now?

### The structure plane: 
How is the information structured and how is it logically grouped?

### The skeleton plane: 
How will our information be represented, and how will the user navigate to the information and the features?

### The surface plane: 
What will the finished product look like?
What colors, typography, and design elements will we use?

### Wireframes

### Colour Scheme

### Typography

## Features

### Future Features

## Testing

### Manual Testing

### Validator Testing

### Bugs and Issues

- Running the Project for the first time in the browser and Django doesn't recognise the hostname
![Issue with running in the browser](readme_assets/issue-image01.png)
[ Resolved with adding the hostname to ALLOWED_HOSTS, inside project/settings.py file ]
![Resolved issue and Django running in the browser](readme_assets/issue-image02.png)
- Django App first run in the browser issue [ resolved with manually adding /about on the end ]
![Django App first run issue](readme_assets/image07.png)
- The issue with the 'Push' command in IDE Terminal after some changes/commits were done directly on GitHub space
![Push command refuse because of GitHub commits](readme_assets/issue-image04.png)
- Resolved
![Resolved git push error](readme_assets/issue-image05.png)
- Error with About app, run server command stop all, on localhost, after migration
![About app admin.py error](readme_assets/issue-image06.png)

## Deployment

### Local deployment on workstation
- from installation of Python on Windows OS to runing project in the browser

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
- Git version control

## Credits [Acknowledgments]

Images and photographs created by Me, Myself and I
Font style created by Google Fonts [https://fonts.google.com/]
Footer icons provided by Font Awesome [https://fontawesome.com/icons]
---
Online simple Kanban style task process board [https://notepad.js.org/kanban/]
Google Translate [https://translate.google.com/]
Control Vi to edit and download image from clipboard [https://ctrl.vi/]
Folge - paste image from clipboard to download [https://folge.me/tools/]
Lorem Ipsum - generator of dummy text [https://www.lipsum.com/]
---
- Complete Basic Django Series [https://djangotherightway.com/]
- Content made for the Django Community [https://django.wtf/]
---


## Gitpod Reminders

For a frontend (HTML, CSS, JS only) apps in Gitpod, Terminal: **python3 -m http.server**

For a backend Python file, Terminal: **python3 run.py**  [ if name of the file is 'run.py' ]

To run the Django server in the Terminal: **python manage.py runserver**  
Dev server opens: 127.0.0.1:8000  
Heroku live server: https://neurographical-915fed1a7d6c.herokuapp.com/
GitHub status: https://www.githubstatus.com/history



<details>
<summary>Image explanation <b style="color: yellow;">(open here)</b></summary>
<!-- Comment related to link and image -->
<img src="work-readme/image.webp">
</details>
