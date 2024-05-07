from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    firstname = request.form["first_name"]
    lastname = request.form["last_name"]
    studentid = request.form ["student_id"]
    apple = request.form["apple"]
    strawberry = request.form["strawberry"]
    raspberry = request.form["raspberry"]
    total = int(apple)+int(strawberry)+int(raspberry)
    print (request.form)
    print (f"Charging,{firstname} {lastname} for {total} fruits")
    return render_template("checkout.html",firstname = firstname ,lastname=lastname, studentid=studentid, 
                           apple=int(apple),strawberry=int(strawberry),raspberry=int(raspberry), total=int(total))



@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)   