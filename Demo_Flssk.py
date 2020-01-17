
from flask import Flask
from flask import render_template

app = Flask(__name__,template_folder='template')

@app.route('/')
def index():
    return ('<h1>hello World ....</h1>')


@app.route('/index')
def Hello():
    return ("return from Hello Method ...... :-)")

@app.route('/<name>')
def UserName(name):
    return ("Good Morning "+name)


@app.route('/Design')
def Design():
    return  render_template('design.html')

if __name__ == '__main__':
    app.run()
