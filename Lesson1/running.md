Способы запуска
1. Gunicorn
а) Команда в терминале: gunicorn -w 4 'app:app'
Запустится по ссылке: http://127.0.0.1:8000/main

б) С использование конфигурационного файла
gunicorn --config gunicorn_config.py app:app


https://flask.palletsprojects.com/en/latest/deploying/gunicorn/
https://developers.redhat.com/articles/2023/08/17/how-deploy-flask-application-python-gunicorn#the_application


Работа с Docker:

sudo docker build -t flask_app .
sudo docker images
# - p [внешний порт]:[внутренний порт]
sudo docker run -i -t -p 8080:8080 flask_app:v.01