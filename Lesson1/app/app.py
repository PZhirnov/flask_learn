from flask import Flask
from flask import render_template

from datetime import datetime
from os import path

app = Flask(__name__)


@app.route('/')
def index():
    return 'My app'


@app.route('/main')
def main():
    data: dict = {
        "id": 150,
        "username": "p.zhirnov",
        "datetime": datetime.utcnow(),
    }
    print(type(path.join(path.abspath('results'), f'new_file{datetime.utcnow()}.txt')))
    print(path.abspath('results'))
    with open(path.join(path.abspath('results'), f'new_file{datetime.now()}.txt'.replace(':', '-')), 'w', encoding='utf-8') as file:
        file.write(f'{datetime.utcnow()}')
    return render_template('main.html', **data)


if __name__ == '__main__':
    app.run(debug=True)
