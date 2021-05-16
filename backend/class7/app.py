from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/submitpage')
def index2():
    return render_template("submit.html")


if __name__ == "__main__":
    app.run(debug=True)
