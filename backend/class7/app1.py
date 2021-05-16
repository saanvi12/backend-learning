from flask import Flask
app = Flask(__name__)


@app.route('/sdfg')
def index():
    return "Hello World!"


@app.route('/')
def index2():
    return "This is the second page."


if __name__ == "__main__":
    # app.run(debug=True)
    print(__name__)
