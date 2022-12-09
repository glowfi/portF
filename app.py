from flask import Flask, redirect, render_template, url_for, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
db = SQLAlchemy(app)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), nullable=False)
    message = db.Column(db.String(200), nullable=False)

    def __repr__(self) -> str:
        return self.id


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"].lstrip(" ").strip(" ")
        print(name, email, message)
        newTask = Todo(name=name, email=email, message=message)
        try:
            if name != "" and email != "" and message != "":
                db.session.add(newTask)
                db.session.commit()
            return redirect("/")
        except Exception as e:
            print(e)
            return "There was an issue!"
    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
