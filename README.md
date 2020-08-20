# Awwwards

##### By [Sarah Sindet](https://github.com/sarahsindet)

Github link: https://github.com/sarahsindet/Awwwards.git 


# Description  
This project allows users to post their projects for other users to rate according to design, usability, creativity and content.

 
## User Story  
  
* A user can view posted projects and their details.  
* A user can post a project to be rated/reviewed. 
* A user can rate/ review other users' projects.  
* Search for projects.  
* View projects overall score.
* A user can view their profile page.  
  

  
## Setup and Installation  
To get the project : 
  
##### Clone the repository:  
 ```bash 
 https://github.com/sarahsindet/awwwards.git 
```

##### Install and activate Virtual  
 ```bash 
- python3 -m venv virtual - source virtual/bin/activate  
```  


##### Navigate into the folder and install requirements with te command:
 ```bash 
pip install -r requirements.txt 
```

##### Install Dependencies  
 ```bash 
 pip install -r requirements.txt 
```  
 ##### Setup Database  
  SetUp your database User,Password, Host then make migrations:
 ```bash 
python manage.py makemigrations projects
 ``` 
 Then Migrate: 
 ```bash 
 python manage.py migrate 
```
##### Run the application  
 ```bash 
 python manage.py runserver 
``` 
##### Testing the application  
 ```bash 
 python manage.py test 
```
Open the application on your browser `127.0.0.1:8000`.  
  
 
 
 
## Technology used  
  
* [Python3.6](https://www.python.org/)  
* [Django 1.11](https://docs.djangoproject.com/en/1.1/)  
* [Heroku](https://heroku.com)  
  
  
 
  
## Contact Information   
If you have any question or contributions, please email me at sarahsindet@gmail.com 
  

