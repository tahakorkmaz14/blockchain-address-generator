# Blockchain Address Generator
Welcome to this blockchain address generator project. 
Here you can generate and store multiple blockchain addresses and use them. Addresses can be created at both mainnet and testnets although it can change in the future
***
***

## Prerequisites
- Python=>3.10

## Considerations
I have added optional docker containers to simplify the build. If you want to use the docker build you should install Docker and Docker Compose on your local machine.

We will be calling our API throughout the next 8 modules. I have written the requests in (Curl)[https://curl.se/] and (Httpie)[https://httpie.io/]. 

(Httpie)[https://httpie.io/] provides a clean terminal output which is handy for this type of project. You will need to install it locally if you want to use the commands.
>Note: (Httpie)[https://httpie.io/] is pre-installed in the docker container.
***
***

## Getting started
First you will need to clone down the project.

1) Root of the main project is core folder.

2) Open a terminal and cd into the core directory.

3) Then run the following commands...

```
venv activate

pip3 install -r requirements.txt

python manage.py makemigrations

python manage.py migrate

python manage.py runserver

```

***
***

## APIs
There's 3 APIs that are running functionally right now, 4 if you count the contact storage.

GET http://127.0.0.1:8000/list-address/        get all the stored addresses

GET http://127.0.0.1:8000/retreive-address/    get specific address and information using the id given after the creation

POST http://127.0.0.1:8000/generate-address/   {currrency="BTC", network="mainnet"} create a new address at the specified network

post command with httpie
```
http http://127.0.0.1:8000/generate-address/ currency="BTC" network="mainnet"           
```



***
***


## Following along
I added a docker for testing with httpie, curl with Flask to run tests as well. Also there's another postgresql database connection string for railway app as well. You can change it to use an online postgre sql database instead of sqllite as well. There's also some unittests at the tests.py file but i didnt finish them all.
***
***