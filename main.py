from flask import Flask, render_template, request, redirect, session, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key="Bhupinder"

app.config["SQLALCHEMY_DATABASE_URI"]= "sqlite:///users.db" # type: ignore
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]= False

db = SQLAlchemy(app)

@app.route("/")
def index():
    if "username" in session:
        return redirect(url_for('dashboard'))

    return render_template("index.html")

if __name__=="__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)