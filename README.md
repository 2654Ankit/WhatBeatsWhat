# What Beats What 
# Requirements:
## 1. Docker shold be installed on your machine. To install docker go to https://docs.docker.com/engine/install/

# How to run:-

## 1. Pull the code on your machine
## 2. set .env file containig :-  GEMNI_API_KEY= your_api_key, REDIS_HOST=redis ,REDIS_PORT=6379  
## 3. Now run "docker-compose --env-file .env up --build". This will create the image of project in docker
## 5. go to  http://0.0.0.0:8000  on your browser the UI will appear and you are ready to play.
## 6. To run project after docker image is build you can only run "docker-compose --env-file .env up".


# Rule of game:
## 1. If you guess more than one time a single word then you will loose.
## 2. Here is sample :  water bets rock, heat beat water, ice beats heat and so on