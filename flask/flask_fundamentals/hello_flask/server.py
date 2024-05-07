from flask import Flask
app = Flask(__name__)                     
    


@app.route('/')         
def hello_world():
    return "Hello World!"

@app.route('/dojo')         
def dojo():
    return "Dojo"

@app.route('/say/<name>')         
def say(name):
    return "Hi, " + name+  "!"


@app.route('/repeat/<name>/<num>')         
def repeat(name, num):
    return name*int(num)



if __name__=="__main__":
     app.run(debug=True)