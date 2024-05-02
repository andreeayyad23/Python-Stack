from flask import Flask, render_template
app = Flask(__name__)
@app.route('/play')
def index():

    return render_template("index.html", num = 3, color = "blue")

@app.route('/play/<x>')
def play(x):
    return render_template("index.html", num = int(x), color = "blue")

@app.route('/play/<x>/<color>')
def color(x, color):
    return render_template("index.html", num = int(x), color = color)

if __name__=="__main__":
    app.run(debug=True)