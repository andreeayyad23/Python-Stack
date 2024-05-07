from flask import Flask, render_template, request, redirect, session
app =Flask(__name__)

app.secret_key='Secret'


@app.route('/')
def count():
    if "counter" in session:
        session["counter"] += 1
    else:
        session["counter"] = 1
    return render_template('index.html', count=session["counter"])

@app.route('/addtwo')
def addtwo():
    session["counter"] += 1
    return redirect('/')

@app.route('/destroy_session')
def destroy():
    session.clear()
    return redirect('/')

@app.route('/reset')
def reset():
    session["counter"] = 0
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)