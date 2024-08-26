"""
Перехват запросов

В веб-приложениях часто нужно исполнить определенный код до или после запроса. Например, нужно вывести весь список IP-адресов пользователей, которые используют приложение или авторизовать пользователя до того как показывать ему скрытые страницы. Вместе того чтобы копировать один и тот же код внутри каждой функции представления, Flask предлагает следующие декораторы:

before_first_request: этот декоратор выполняет функцию еще до обработки первого запроса
before_request: выполняет функцию до обработки запроса
after_request: выполняет функцию после обработки запроса. Такая функция не будет вызвана при возникновении исключений в обработчике запросов. Она должна принять объект ответа и вернуть тот же или новый ответ.
teardown_request: этот декоратор похож на after_request. Но вызванная функция всегда будет выполняться вне зависимости от того, возвращает ли обработчик исключение или нет.
ВАЖНО! если функция в before_request возвращает ответ, тогда обработчик запросов не вызывается.
"""

from flask import Flask, request, g

app = Flask(__name__)


@app.before_request
def before_request():
    print(request.args)
    if not len(request.args):
        """Если аргументы не были переданы, то функция не сработает
        """
        return """
        <h2>Не переданы аргументы!</h2>
        <p>Функция не сработает!</p>
        """
    print("before_first_request() called")


@app.after_request
def after_request(response):
    # Тут response можно обработать перед тем, как отдать на фронт
    print("after_request() called")
    return response


@app.route("/")
def index():
    print("index() called")
    return '<p>Testings Request Hooks</p>'


if __name__ == "__main__":
    app.run(debug=True)
