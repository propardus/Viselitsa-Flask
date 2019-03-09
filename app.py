from flask import Flask, render_template, session, request, redirect
from random import choice

app = Flask(__name__)


@app.before_first_request
def before_request():
    session['gamer']=False
    session['nepravda'] = 0
    session['pravda'] = 0

@app.route('/')
def index():
    global lif
    lif = 10
    if session['gamer']==False:
        f = open('slova.txt', 'r')
        words = f.read().lower()
        f.close()
        words = words.split('\n')
        word = choice(words)
        xword = '■'*len(word)
        session['word'] = word
        session['xword'] = xword
        session['lif']=lif
        session['gamer'] = True
        session['bukvi']=['']

    else:
        xword = session['xword']
        word = session['word']
        lif = session['lif']
    if not '■' in xword:
        session['gamer'] = False
        session['pravda'] = session['pravda'] + 1
        return render_template('pobandproi.html', ot='победили')
    else:
        return render_template('otvet.html', x_word=xword, answer=word,live=lif)


@app.route('/send', methods=['POST'])
def sendme():
    global lif
    char = request.form['char']
    xword = session['xword']
    word = session['word']
    new_xword = ''
    print(session['bukvi'])
    if char not in session['bukvi'] :
        session['bukvi'].append(char)
        for i in range(len(word)):
            if word[i] == char:
                new_xword += char
            else:
                new_xword += xword[i]
        if new_xword==xword:
            lif = lif-1
        # return '{}, {}, {}'.format(session['word'], session['xword'], request.form['char'])
        if lif <= 0:
            session['nepravda'] = session['nepravda'] + 1
            session['gamer']=False
            return render_template('pobandproi.html',ot='проиграли')
        else:
            session['xword'] = new_xword
            session['lif'] = lif
    return redirect('/')



@app.route('/results')
def res():
    return render_template('otvetee.html',x_res=session['pravda'],p_res=session['nepravda'])


@app.route('/logout')
def zanovo():
    session['nepravda']+=1
    session['gamer']=False
    return redirect('/')


app.secret_key = 'isduf*&&(*(*&@jhhje893w92803834e'
app.run()

