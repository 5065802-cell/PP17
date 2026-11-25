from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():
    user = request.form.get("username")
    pwd = request.form.get("password")
    if user == "admin" and pwd == "12345":
        return "<h3>Login Successful Welcome Admin</h3>"
    return "<h3>Invalid Username or Password</h3>"

if __name__ == "__main__":
    app.run(debug=True)
