# Read & Review API
This is the Read & reviews API build with django REST. the read & review API contains different functions for registration if visitor want to be able to post and comment. sign in for access to all the features. the read & review is made for sharing content for interaction with users who enjoy reading books.

## Validation

* CI python Linter
* tested in all serializers and views.

![alt text](images/dawdawdawd.PNG)

# Testing in Django REST

## Testing in Django REST

### views

| Status | **Posting - Post is valid** |
|:------:|:-----------------------------------
| &check; | test for sending post (status code 201). created post.

| Status | **Comments - Valid comment created** |
|:------:|:----------------------------
| &check; | tested for creating comment (status code 201) comment created.


| Status | **sign in - Valid Data** |
|:------:|:-------------------------------
| &check; | When the user try to sign in (status code 200) user sign in.


## Deployment

### Create project repository

 Log in to GitHub then use the Code institute for making the project
 click to "use this template" 
 create a repository with name in the Repository name
 then create Repository 

### Create heroku app
 Login to the heroku platform
go to the dropdown in homepage and create app
give the app a project name, and choose the location you are in.

### deploy heroku application
press the settings tab when clicked into your new application project.
go to config vars section.
and installed ALLOWED_HOST, CLIENT_ORIGIN, CLIENT_ORIGIN_DEV,CLOUDINARY_URL,DATABASE_URL,SECRET_KEY.for backend.
add key of DISABLE_COLLECTSTATIC and  the value of 1
install gunicorn in the command in the terminal 
update the requirements.txt.
Create a Procfile.
in settings put the '.herokuapp.com' to ALLOWED_HOSTS.
go to deploy in heroku go down to "Manual deploy" and press to Deploy Branch.

## Credits
### Help from
* Code institute project for Django REST framework.
* lucid.app for making my models.