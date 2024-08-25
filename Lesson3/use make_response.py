from flask import Flask, make_response

app = Flask(__name__)


@app.route('/books/<genre>')
def books(genre):
    res = make_response(f'All Books in {genre} category', 200)
    res.headers['Content-Type'] = 'text/plain'
    res.headers['Server'] = 'Foobar'
    # res.status_code = 200
    return res


@app.route('/404/')
def http_404_handler():
    return make_response("<h2>404 Error</h2>", 400)


@app.route('/set-cookie')
def set_cookie():
    """Пример установки куки
    Это простой пример и при необходимости взять из документации расширенный вариант
    """
    res = make_response("Cookie setter")
    res.set_cookie("favorite-color", "skyblue")
    res.set_cookie("favorite-font", "sans-serif")
    return res




if __name__ == '__main__':
    app.run()
