from flask import Flask, render_template, redirect, request, session
import model

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/create_account", methods = ["POST"])
def create_account():
    if session.get("email"):
        return
    else:
        new_email = request.form.get("email")
        new_pw = request.form.get("password")
        new_age = request.form.get("age")
        new_zip = request.form.get("zipcode")
        model.create_new_user(model.session, new_email, new_pw, new_age, new_zip)
        return render_template("new_user.html", new_email=new_email, new_pw=new_pw, new_age=new_age, new_zip=new_zip)

@app.route("/login", methods=["POST"])
def process_login():
    # form.get("___") --> blank corresponds to name in HTML form
    email = request.form.get("email")
    password = request.form.get("password")
    if model.authenticate(email, password):
        return render_template("login.html", email=email, password=password)
    else:
        return render_template("login_fail.html")

@app.route("/user_list")
def user_list():
    user_list = model.session.query(model.User).limit(5).all()
    return render_template("user_list.html", users=user_list)

@app.route("/user_list/<user_id>")
def user_id(user_id):
    user = model.session.query(model.User).get(user_id)
    return render_template("user_id.html", user=user)

if __name__ == "__main__":
    app.run(debug = True)