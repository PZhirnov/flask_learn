"""
Создание ответов с помощью кортежей
Можно использовать кортежи в одном из следующих форматов:
(response, status, headers)
(response, headers)
(response, status)
response — строка, представляющая собой тело ответа, status — код состояния HTTP,
который может быть указан в виде целого числа или строки, а headers — словарь со значениями заголовков.
"""

from flask import Flask, make_response

app = Flask(__name__)


@app.route('/books/<genre>')
def books(genre):
    res = make_response(f'All Books in {genre} category', 200)
    res.headers['Content-Type'] = 'text/plain'
    res.headers['Server'] = 'Foobar'
    # res.status_code = 200
    return res


@app.route('/')
def http_500_handler():
    return "<h2>500 Error</h2>", 500


@app.route('/md')
def render_markdown():
    return "## Heading", 200, {'Content-Type': 'text/markdown'}


@app.route('/transfer', methods=['get', 'post'])
def transfer():
    """
    Реализация редиректа скодом 302
    :return:
    """
    # Редирект может быт сделан двумя способами
    # return redirect("https://localhost:5000/login")
    return "", 302, {'location': 'https://localhost:5000/login'}


if __name__ == '__main__':
    app.run()
