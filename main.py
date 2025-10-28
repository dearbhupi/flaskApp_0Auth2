from flask import Flask, render_template, request, redirect, session, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key="Bhupinder"

app.config["SQLALCHEMY_DATABASE_URI"]= "sqlite:///users.db" # type: ignore
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]= False

db = SQLAlchemy(app)

# Database Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username= db.Column(db.String(25), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

    def set_password(self, password):
        self.password_hash= generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash(password))


@app.route("/")
def index():
    if "username" in session:
        return redirect(url_for('dashboard'))

    return render_template("index.html")

#Login
@app.route("/login", methods=["POST"])
def login():
    #Collect info from the form
    username = request.form['username'] #will accpt form the index form html
    password = request.form['password']
    user= User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        session['username'] = username 
        return redirect(url_for('dashboard'))
    
    else:
        return render_template("index.html")



if __name__=="__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)