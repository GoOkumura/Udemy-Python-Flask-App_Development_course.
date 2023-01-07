from flask import Flask, render_template, request
from wtforms import StringField, SubmitField, IntegerField
from wtforms.form import Form


app = Flask(__name__)

app.config["SECRET_KEY"] = b"\x87\x84\x8b.iD\x9d\x9cj\xf7\n\x15\x9c3-\x19"

class UserForm(Form):
    name = StringField("名前")
    age = IntegerField("年齢")
    submit = SubmitField("Submit")

@app.route("/", methods=["GET", "POST"])
def index():
    name = age = ""
    form = UserForm(request.form)
    if request.method == "POST":
        if form.validate():
            name = form.name.data
            age = form.age.data
            form = UserForm()
        else:
            print("入力内容に間違いがあります。")
    return render_template("index.html", form = form, name = name, age = age)

if __name__ == "__main___":
    app.run(debug=True)