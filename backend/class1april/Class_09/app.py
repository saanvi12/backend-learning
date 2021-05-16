from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['GET', 'POST'])
def submitFucntion():
    if request.method == 'POST':
        data = {
            'Name': request.form['name'],
            'Age': request.form['age'],
            'Gender': request.form.get('gender'),
            'Email': request.form['email'],
            'Resaddr': request.form['raddr'],
            'City': request.form['city'],
            'Prov': request.form.get('prov'),
            'Zip': request.form['zip'],
            'Country': request.form['country'],
            'Nation': request.form['nation']
        }
        print(data)
    return render_template('submit.html', datas=data)


if __name__ == '__main__':
    app.run(debug=True)
