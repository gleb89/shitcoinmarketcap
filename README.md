# shitcoinsmarketcap

## touch .env
## enviroment
   - POSTGRES_USER
   - POSTGRES_PASSWORD
   - POSTGRES_DB
   - LOGIN_EMAIL
   - PASSWORD_EMAIL
   - SECRET_KEY
   - API_KEY_COIN
   - URL_PRICE


#### - Docker start
### docker-compose up --build
### docker-compose up -d
### docker-compose -f docker-compose.yml logs -f


#### - localhost start
### virtualenv env
### sourse/env/bin/activate
### pip install -r requirements.txt
### python manage.py makemigrations
### python manage.py migrate
### python manage.py createsuperuser
### python manage.py runserver
