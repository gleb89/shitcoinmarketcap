# shitcoinsmarketcap
![Test Image 3](/api.png)
### Service to display scam coins and tokens 
***
    
### Application structure   
    ├── apps
    |   ├── coins
    |   ├── comments
    |   ├── core
    |   └── users
    ├── config
    |   ├── settings.py
    |   ├── urls.py
    |   ├── wsgi.py
        ├── celery.py
        ├── tasks.py
    |   ├── asgi.py
    |   └── keysetting.py
    ├── data
    |   ├── nginx
    |       └──app.conf
    ├── static
    ├── Dockerfile
    ├── docker-compose.yml
    └─ requirements.txt
    
    
    



## Build and run the container

1. Install Docker.

2. Create a `.env` file 

    ```
    # Environment settings for local development.
   POSTGRES_USER=postgres
   POSTGRES_PASSWORD=postgres
   POSTGRES_DB=241281
    ```


3. On the command line, within this directory, do this to build the image and
   start the container:

        docker-compose run djapi python manage.py migrate --noinput
        docker-compose run djapi python manage.py createsuperuser
        docker-compose up --build
        docker-compose up -d
        docker-compose -f docker-compose.yml logs -f


4. Open http://0.0.0.0:80/api/v1 in your browser.

## If deploy  - 
 - rename file  <strike>docker-compose.prod.yml</strike> docker-compose.yml and <strike>docker-compose.yml </strike> docker-compose.dev.yml 

        
        chmod +x init-letsencrypt.sh
        ./init-letsencrypt.sh
        docker-compose run djapi python manage.py migrate --noinput
        docker-compose run djapi python manage.py createsuperuser
        docker-compose up --build
        docker-compose up -d

5 . Requests api JWT

   -      Authorization :Bearer 'token' 
    
    
