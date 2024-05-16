from flask import Flask, render_template, request, redirect,  url_for, flash

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/test')
def test():
    return render_template('test.html')

@app.route('/test2')
def test2():
    return render_template('test2.html')

@app.route('/test3')
def test3():
    return render_template('test3.html')
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=10000)