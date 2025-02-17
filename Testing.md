## Testing

### Manual Testing

The manual testing of a website can be a simple procedure, involving the access of a web page or application within a controlled setting, 
systematically navigating through a set of predefined test scenarios, and documenting the results of each test in a spreadsheet. 
This fundamental method is often utilized by software teams as they first emphasize quality assurance.  

Primarily, a foundational understanding of the Python environment and Django templating, along with knowledge of HTML elements and CSS properties, is advantageous for recognizing and resolving potential issues.

**Testing Process:**  
- *Tested Code*:  
- Project was started as a Python code with Django framework to be used for templating and administration of applications  
- After every new function, variable or template tag, testing was provided through checking result with running server
- *Tested Content*: 
- Before adding actual content, inserted some test content into HTML file and run it in web browser to ensure that the code is working as expected.
- *User Interface (UI)*: 
- Verified the layout, visual design, and overall user experience. Checked for consistent formatting, proper image loading, and readability across different screen sizes.
- *Readability*: 
- Examined displayed text (font family, font size, color contrast).
- *Navigation*: 
- Tested all navigation elements like menus, buttons, and links. Ensured they lead to the correct destination pages and function smoothly.
- *Forms & Functionality*: 
- Tested form (contact) to be sure it submit data correctly, provide clear error messages for invalid inputs, and follow expected functionalities, sending data.
- *Content Accuracy*: 
- Reviewed all website content for accuracy, grammar, and spelling mistakes. Verified that descriptions and other information are up-to-date and consistent.
- *Responsiveness*: 
- Validated responsiveness of the website loading Dev Tools option of split screen and resized the browser window across different browsers.
---
- Test of the Main top page menu = PASS  
- Test for all links on the site = PASS  
- Test of the displayed published posts = PASS  
- Test of the navigation for posts = PASS  
- Test for the opening of the choosen post = PASS  
- Test for the Admin area = PASS  
- Test for the CRUD action for the Post in the Admin area = PASS  
- Test for the CRUD action for the User in the Admin area = PASS  
- Test for the CRUD action for the Comment in the Admin area = PASS  
- TEST for the Registration form for the new User = PASS  
![Registering new User](readme_assets/image46.png)  
- Test for the login and logout of the user = PASS  
- Top navigation link change to 'Logout' = PASS  
![Login or logout msg](readme_assets/image53.png)  
- Test for the message display related to action from the User = PASS  
- Test for a login with wrong credentials = PASS  
![alt text](readme_assets/image52.png)  
- Test for the access to Admin area as a logged-in User = PASS  
![Logged-in User access to Administration](readme_assets/image43.png)  
- Test for the CRUD action for the Comment content by the User = PASS  
![Edit button fill form area for editing](readme_assets/image55.png)  
- Test of the confirmation on the action by User = PASS  
![Delete button and modal for comment](readme_assets/image44.png)  
- Test for display of the default post image over the post in post listing = PASS  
- Test for upload of the Post custom-featured image from the Admin panel = PASS  
- Test for edit/delete option in Admin/Newsletter area = PASS  
![Admin can delete newsletter](readme_assets/image48.png)  
- Test of the confirmation on the action by Admin = PASS  
![Confirmation for Deletion](readme_assets/image49.png)  

### Validator Testing

- HTML: **https://validator.w3.org/**  
- As this Project is build with Django templates, for every specific page View Source command is used to be able to Copy and Paste code to validator  
- Home page  
![Home page](readme_assets/image57.png)  
- About page  
![About page](readme_assets/image58.png)  
- Journal page listing  
![Journal page listing](readme_assets/image59.png)  
- Journal page - single post  
![Journal page - single post](readme_assets/image62.png)  
- Sign up page  
![Sign up page](readme_assets/image60.png)  
- Login page  
![Sign in page](readme_assets/image61.png)  
- Error page - 404  
![Error page - 404](readme_assets/image63.png)  
- CSS: **https://jigsaw.w3.org/css-validator**  
![Styling with custom CSS](readme_assets/image64.png)  
- Lighthouse: **https://pagespeed.web.dev/**  
- Lighthouse is an open-source, automated Audit tool for improving the quality of web pages. You can run it against any web page, public or requiring authentication. It has audits for performance, accessibility, progressive web apps, SEO, and more. Lighthouse is integrated directly into the Chrome DevTools, under the "Lighthouse" panel.  
- Lighthouse metrics:  
- Home page - desktop  
![Home page - desktop](readme_assets/image67.png)  
- Home page - mobile  
![Home page - mobile](readme_assets/image68.png)  
- About page - desktop  
![About page - desktop](readme_assets/image65.png)  
- About page - mobile  
![About page - mobile](readme_assets/image66.png)  
- Journal page, listing - desktop  
![Journal page, listing - desktop](readme_assets/image70.png)  
- Journal page, listing - mobile  
![Journal page, listing - mobile](readme_assets/image69.png)  
- Journal page, single - desktop  
![Journal page, single - desktop](readme_assets/image71.png)  
- Journal page, single - mobile  
![Journal page, single - mobile](readme_assets/image72.png)  
- Sign up page - desktop  
![Sign up page - desktop](readme_assets/image73.png)  
- Sign up page - mobile  
![Sign up page - mobile](readme_assets/image74.png)  
- Sign in page - desktop  
![Sign in page - desktop](readme_assets/image75.png)  
- Sign in page - mobile  
![Sign in page - mobile](readme_assets/image76.png)  
- Error 404 page - desktop  
![Error 404 page - desktop](readme_assets/image77.png)  
- Error 404 page - mobile  
![Error 404 page - mobile](readme_assets/image78.png)  
- JavaScript: **https://www.jshint.com/**  
- Only one custom JS file  
![Custom JS file](readme_assets/image79.png)  
- Python: **https://pep8ci.herokuapp.com/**  
- for all tested code Results: All clear, no errors found  
![Home/admin.py](readme_assets/image85.png)  
![Home/apps.py](readme_assets/image86.png)  
![Home/forms.py](readme_assets/image87.png)  
![Home/models.py](readme_assets/image88.png)  
![Home/urls.py](readme_assets/image89.png)  
![Home/views.py](readme_assets/image90.png)  
![About/admin.py](readme_assets/image80.png)  
![About/apps.py](readme_assets/image81.png)  
![About/models.py](readme_assets/image82.png)  
![About/urls.py](readme_assets/image83.png)  
![About/views.py](readme_assets/image84.png)  

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
