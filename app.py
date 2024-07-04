from flask import Flask , request,render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("Home.html")

@app.route("/blog/<pk>")
def blog(pk):
    return render_template(f"blog{pk}.html")

@app.route("/user/<username>")
def hello(username):
    return f"<h3> Hello {username} </h3>"

@app.route("/add")
def add():
    a = request.args.get("a")
    b = request.args.get("b")
    a , b = int(a) , int(b)
    return f"<h3> Result {a+b} </h3>"

@app.route("/sub")
def sub():
    a = request.args.get("a")
    b = request.args.get("b")
    a , b = int(a) , int(b)
    return f"<h3> Result {a-b} </h3>"


@app.route("/div")
def div():
    a = request.args.get("a")
    b = request.args.get("b")
    a , b = int(a) , int(b)
    return f"<h3> Result {a*b} </h3>"


@app.route("/mul")
def mul():
    a = request.args.get("a")
    b = request.args.get("b")
    a , b = int(a) , int(b)
    return f"<h3> Result {a//b} </h3>"


@app.route("/calculate" , methods=["GET , POST"])
def calculate():
    if request.method == "GET":
        return render_template("calculate.html")
    else:
        a1 = request.form.get("a1")
        a2 = request.form.get("a2")
        action = request.form.get("action")
        a1, a2 = int(a1), int(a2)
        match action:
            case "add":
                result = a1 + a2
            case "sub":
                result = a1 - a2
        return render_template("calculate.html", result=result)




if __name__ == "__main__":
    app.run(host="127.0.0.1" , debug=True)

