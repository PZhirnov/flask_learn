from flask import Flask
from flask import render_template

app = Flask(__name__, template_folder='templates')


@app.route('/')
def index():
    """
    Если render_template() нужно передать много аргументов, можно не разделять их запятыми (,),
    а создать словарь и использовать оператор **, чтобы передать аргументы-ключевые слова функции. Например:
    :return:
    """
    return render_template('index.html', name='Jerry')


@app.route('/dict/')
def index_dict():
    name, age, profession = "Jerry", 24, 'Programmer'
    template_context = dict(name=name, age=age, profession=profession)
    return render_template('index.html', **template_context)


if __name__ == '__main__':
    app.run(debug=True)
