import smtplib
from flask import Flask, render_template, request,flash,redirect,url_for
import os
from dotenv import load_dotenv

app = Flask(__name__)
app.secret_key = 'madkwmdsadmaad'

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/contact', methods =['GET','POST'])
def contact():
    load_dotenv()
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]
        try:
            with smtplib.SMTP(os.environ["SMTP_ADDRESS"], port=587) as connection:
                connection.starttls()
                connection.login(os.environ["EMAIL_ADDRESS"], os.environ["EMAIL_PASSWORD"])

                connection.sendmail(
                    from_addr=os.environ["EMAIL_ADDRESS"],
                    to_addrs=os.environ["EMAIL_ADDRESS"],
                    msg=f"Subject: Portfolio Direct Message!!\n\nName: {name}\nEmail: {email}\nMessage: {message}".encode(
                        "utf-8")
                )
                flash("Message sent successfully!","success")
        except Exception:
            flash("Message failed to send!", "error")
        return redirect(url_for('contact'))
    return render_template("contact.html")

@app.route("/my_strength")
def strength():
    return render_template("strength.html")

@app.route("/hobby")
def hobby():
    return render_template("hobby.html")

@app.route('/achievements')
def achievements():
    return render_template("achievements.html")

@app.route('/dream')
def dream():
    return render_template("dream.html")

if __name__ == "__main__":
    app.run(debug = True,port = 5001)