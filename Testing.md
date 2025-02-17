## Testing

### Manual Testing

- Test of the Main top page menu = PASS
- Test of the displayed published posts = PASS
- Test of the navigation for posts = PASS
- Test for the opening of the choosen post = PASS
- Test for the Admin area = PASS
- Test for the CRUD action for the Post in the Admin area = PASS
- Test for the CRUD action for the User in the Admin area = PASS
- Test for the CRUD action for the Comment in the Admin area = PASS
- TEST for the Registration form for the new User
![Registering new User](readme_assets/image46.png)
- Test for the login and logout of the user = PASS
- Test for the message display related to action from the User = PASS
- Test for a login with wrong credentials = PASS
![alt text](readme_assets/image52.png)
- Test for the access to Admin area as a logged-in User = PASS
![Logged-in User access to Administration](readme_assets/image43.png)
- Test for the CRUD action for the Comment content by the User = PASS
![Delete button and modal for comment](readme_assets/image44.png)
- Test for display of the default post image over the post in post listing = PASS
- Test for upload of the Post custom-featured image from the Admin panel = PASS
- Test for edit/delete option in Admin/Newsletter area = PASS
![Admin can delete newsletter](readme_assets/image48.png)
- Test of the confirmation on the action = PASS
![Confirmation for Deletion](readme_assets/image49.png)

### Validator Testing

- HTML: **https://validator.w3.org/**
- about.html as a link to page
- post page for authenticated user with View Source -> Copy -> Paste code to Validate by direct input
- Error for comment-id -> post_detail.html -> data-comment_id -> comments.js -> data-comment_id
- CSS: **https://jigsaw.w3.org/css-validator**
- Lighthouse: **https://pagespeed.web.dev/**
- JavaScript: **https://www.jshint.com/**
- Python: **https://pep8ci.herokuapp.com/#**

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
- ModuleNotFoundError: No module named 'crispy_forms' on second computer, resolved with installation
![ModuleNotFindError](readme_assets/issue-image07.png)
- ImproperlyConfigured: The SECRET_KEY setting raise error and block the local server from running the site
![ImproperlyConfigured](readme_assets/issue-image08.png)
- [ Resolved with creating a new Secret Key from the Terminal and placed it in the env.py file ]
- Issue with import of the comment content for Edit, inside 'textarea' of the form. Didn't fill the form field.
- [ Resolved with the change of the field name configured in models.py ]
![Comment for edit issue](readme_assets/issue-image09.png)