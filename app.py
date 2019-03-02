from flask import Flask, render_template, session, request, redirect
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
        session['word'] = word
        session['xword'] = xword
        session['gamer'] = True
    else:
        xword = session['xword']
        word = session['word']
    if not '■' in xword:
        session.pop('gamer')
    return render_template('otvet.html', x_word=xword, answer=word)


@app.route('/send', methods=['POST'])
def sendme():
    char = request.form['char']
    xword = session['xword']
    word = session['word']
    new_xword = ''
    for i in range(len(word)):
        if word[i] == char:
            new_xword += char
        else:
            new_xword += xword[i]
    session['xword'] = new_xword
    return redirect('/')

app.secret_key = 'isduf*&&(*(*&@jhhje893w92803834e'
app.run()
