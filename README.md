# Project overview
This is a Selenium script that can read the Twitter home page (on your local
computer) and fetch the top 5 trending topics on twitter and store the
results in a MongoDB database (fields in db – unique ID, name of
top 5 trends date , time of end of Selenium script)

# Techstack used
### 1.Python
### 2.Selenium
### 3.MongoDB

# Project setup
1.use git clone to copy this project from this repository using command "git clone <project_url>"
<br>
2.install all the necessary libraries for this projects 
<br>
    &emsp;pip install selenium
    <br>
     &emsp;pip install pymongo
    <br>
     &emsp;pip install dotenv
<br>
3.create a .env file in the project same as .env-example file and fill in your credentials
