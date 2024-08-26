"""Используется для отмены запроса с конкретным
типом ошибки: 404, 500 и так далее
"""

from flask import Flask, abort

app = Flask(__name__)


@app.route('/')
def index():
    abort(500)


if __name__ == "__main__":
    app.run()
