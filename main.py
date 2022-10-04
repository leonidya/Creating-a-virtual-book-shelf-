from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
# app.app_context().push()
app.config['SQLALCHEMY_DATABASE_URI']= "sqlite:///new-books-collection24.db"
# HINT 2: Don't if you get a deprecation warning in the console that's related to SQL_ALCHEMY_TRACK_MODIFICATIONS
 # You can silence it with
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.app_context().push()
# CREATE TABLE
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    # Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f'<Book {self.title}>'

db.create_all()

@app.route('/')
def home():
    all_books = db.session.query(Book).all()
    return render_template("index.html", all_books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        new_book = Book(title=(request.form["title"]), author=(request.form["author"]), rating=(request.form["rating"]))
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("add.html")

print(Book.query.all())

if __name__ == "__main__":
    app.run(debug=True)












#
# # print(Book.query.all())
# # all_books = session.query(Book).all()
# # book = Book.query.filter_by(title="Harry Potter").first()
# # db.session.commit()
# # book_to_update = Book.query.filter_by(title="Harry Potter and the Chamber of Secret").first()
# # book_to_update.title = "Harry Potter and the Chamber of Secretsgfdgdf"
# # db.session.commit()
#
# print(Book.query.all())