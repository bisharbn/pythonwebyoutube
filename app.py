from flask import Flask,redirect,url_for

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World! Welcome to Bot"

@app.route("/home")
def home1():
    return "Hello, World! Home Page"

@app.route("/<name>")#passing value from url
def user(name):
    return f"Hello {name}!"

@app.route("/admin")
def admin():
    return redirect(url_for("user",name="Bishar!admin"))# give the function name here , if you need to redirect to new page

if __name__ == "__main__":
    app.run(debug=True)
