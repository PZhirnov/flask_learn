"""
Изменение страниц ошибок
Декоратор errorhandler используется для
создания пользовательских страниц с ошибками.
Он принимает один аргумент — ошибку HTTP, — для которой создается страница.
"""

from flask import Flask, request, g, abort

app = Flask(__name__)


@app.after_request
def after_request(response):
    print("after_request() called")
    return response


@app.errorhandler(404)
def http_404_handler(error):
    """
    При отмене запроса через abort(404)
    отработает данные метод.
    Оба обработчика ошибок принимают
    один аргумент error, который содержит дополнительную информацию о типе ошибки.
    :param error:
    :return:
    """
    return "<p>HTTP 404 Error Encountered</p>", 404


@app.errorhandler(500)
def http_500_handler(error):
    return "<p>HTTP 500 Error Encountered</p>", 500


@app.route("/")
def index():
    # print("index() called")
    # return '<p>Testings Request Hooks</p>'
    abort(404)  # в данном случае вызовется метод http_404_handler


if __name__ == "__main__":
    app.run()
