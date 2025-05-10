from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80), nullable = False)
    author = db.Column(db.String(80), nullable = False)
    publisher = db.Column(db.String, nullable = False)

    def __repr__(self):
        return f"{self.id} - {self.name} - {self.author} - {self.publisher}"

@app.route("/")
def index():
    return "Hello"

@app.route("/id")
def GetID():
    return "id"

@app.route("/book_name")
def GetBookName():
    return "name"

@app.route("/author")
def GetAuthor():
    return "author"

@app.route("/publisher")
def GetPublisher():
    return "publisher"

# $env:FLASK_APP="application.py"
# $env:FLASK_ENV="development"
# flask run
