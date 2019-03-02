from flask import Flask, render_template, session
from random import choice

app = Flask(__name__)

@app.route('/')
def index():
    if not 'gamer' in session:
        f = open('slova.txt', 'r')
        words = f.read().lower()
        f.close()
        words = words.split('\n')
        word = choice(words)
        xword = '■'*len(word)
    return render_template('otvet.html', x_word=xword, answer=word)


@app.route('/sendme', methods=['POST'])
def sendme():
    ...

app.secret_key = 'isduf*&&(*(*&@jhhje893w92803834e'
app.run()
