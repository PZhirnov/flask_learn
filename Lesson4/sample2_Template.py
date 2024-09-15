from flask import Flask
from flask import render_template

from jinja2 import Template


app = Flask(__name__)


@app.route('/')
def index():
    # return render_template('index.html', name='Павел')
    t = Template("<b>Name: {{ name }}</b>")
    print(t.render(name="Pavel"))
    return render_template('index.html', datа_char_list=[i for i in range(100)])


if __name__ == '__main__':
    app.run(debug=True)
