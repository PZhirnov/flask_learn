"""Flask может генерировать URL с помощью функции url_for() из пакета flask. URL можно
задавать вручную в шаблонах и функциях представления,
но это не очень хорошая практика. Предположим, возникла необходимость поменять структуру ссылок
для блога с /<id>/<post-title>/ на /<id>/post/<post-title>/ . Если URL были заданы вручную в шаблонах и функциях,
тогда придется вручную редактировать их во всех местах. Функция url_for() позволяет произвести то же изменение одним щелчком.
Функция url_for() принимает конечную точку и возвращает URL в виде строки.
"""

from flask import Flask, make_response
from flask import url_for


app = Flask(__name__)


@app.route('/')
def index():
    response = make_response("Ответ", 200)
    # response.charset = "utf-8"
    # response.headers['Content-Type'] = 'text/plain'
    response.headers['Server'] = 'Foobar'
    print(url_for('index'))
    print(url_for('main', name=10))
    return response


@app.route('/main/')
def main():
    response = make_response("Ответ", 200)
    # response.charset = "utf-8"
    # response.headers['Content-Type'] = 'text/plain'
    response.headers['Server'] = 'Foobar'
    print(url_for('index'))
    return response


if __name__ == '__main__':
    app.run(debug=True)
