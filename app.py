from flask import Flask, render_template, request
from requestform import RequestForm

app = Flask(__name__)


@app.route("/")
def main():
    return render_template('index.html')


@app.route("/search",  methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        rq = RequestForm(request.form['address'])
        distance = rq.call_func()

        return render_template('index.html', result=distance)


if __name__ == '__main__':
    app.run(debug=True)
