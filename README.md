# shitcoinsmarketcap
## Service to display scam coins and tokens
***
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


4. Open http://0.0.0.0:80 in your browser.
