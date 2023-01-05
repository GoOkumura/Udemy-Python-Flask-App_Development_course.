from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/signup")
def sign_up():
    return render_template("signup.html")

@app.route("/home")
def home():
    pass

if __name__ == "__main__":
    app.run(debug=True)