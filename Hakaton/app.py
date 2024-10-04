from flask import Flask, render_template

app = Flask(__name__)


def file_write(temp):
    with open('progress.txt', 'r+') as file:
        file.write(temp)


@app.route('/index')
@app.route('/')
def index():
    return render_template("index.html")


@app.route('/Progress')
def progress():
    return render_template('progress.html')


@app.route('/About')
def about():
    return render_template('about.html')


@app.route('/post_1')
def post_1():
    file_write(10)
    return render_template('post_1.html')


@app.route('/post_2')
def post_2():
    file_write(10)
    return render_template('post_2.html')


@app.route('/post_3')
def post_3():
    file_write(10)
    return render_template('post_3.html')


@app.route('/post_4')
def post_4():
    file_write(10)
    return render_template('post_4.html')


@app.route('/post_5')
def post_5():
    file_write(10)
    return render_template('post_5.html')


@app.route('/post_6')
def post_6():
    file_write(10)
    return render_template('post_6.html')


@app.route('/post_7')
def post_7():
    file_write(10)
    return render_template('post_7.html')


@app.route('/post_8')
def post_8():
    file_write(10)
    return render_template('post_8.html')


if __name__ == '__main__':
    app.run(debug=True)
