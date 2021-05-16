from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("htmlpractice.html")


@app.route('/cat')
def index2():
    return render_template("cat.html")


if __name__ == "__main__":
    app.run(debug=True)
