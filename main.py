from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/index') # 127.0.0.1:5000
def index():
    return render_template('index.html')


@app.route('/references')
def references():
    return render_template('references.html')


@app.route('/cells.html')
def cells():
    return render_template('cells.html')


@app.route('/mutations.html')
def mutations():
    return render_template('mutations.html')


if __name__ == '__main__':
    app.run(debug=True)
