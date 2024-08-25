from flask import Flask, request
from werkzeug.exceptions import BadRequestKeyError

"""
Контекст приложения предлагает такие объекты как current_app или g. current_app ссылается на экземпляр, 
который обрабатывает запрос, а g используется, чтобы временно хранить данные во время обработки запроса
"""
from flask import current_app, g

"""
Контекст запроса также предоставляет объекты: request и session. request содержит информацию о текущем запросе, 
а session — это словарь (dict). В нем хранятся значения, которые сохраняются между запросами.
"""
from flask import request, session


app = Flask(__name__)

"""
Чтобы получить доступ к объектам, предоставляемым контекстами 
приложения и запроса вне функции представления, нужно сперва создать соответствующий контекст.
Создать контекст приложения можно с помощью метода app_context() для экземпляра Flask.
"""

"""Вриант 1"""
# app_context = app.app_context()
# app_context.push()
# print(current_app.name)

with app.app_context():
    print(current_app.name)

# Демо процесса создания контекста запроса
with app.test_request_context('/index'):
    print(request.path)  # получим полный путь к запрашиваемой странице(без домена).
    print(request.method)
    print(current_app.name)


@app.route('/')
@app.route('/index/')
def index():
    print(current_app.name)
    # так можно получить аргументы из запроса /index/?x=12&f=15
    try:
        print(request.args, "или показать нужный аргумент:", request.args['x'])
    except BadRequestKeyError as err:
        print(err)
    return f'Привет! {request.remote_addr} {request.method} {request.args}'


@app.route('/users/<user_id>/')
def get_user(user_id: int):
    print(type(user_id))
    return f'Привет {user_id}'


@app.route('/users/<user_id>/posts/<post_id>')
def get_post(user_id: str, post_id: str):
    print(type(user_id))
    return f'Привет {user_id} - {post_id}'


if __name__ == '__main__':
    print(app.url_map)  # карта маршрутов
    app.run(debug=True)
