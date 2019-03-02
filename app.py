from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('otvet.html')


@app.route('/sendme', methods=['POST'])
def sendme():
    ...

app.run()
