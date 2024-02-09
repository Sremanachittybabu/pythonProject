from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from send_email import send_email
from sqlalchemy.sql import func

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:am107ec068@localhost/height_collector'
db = SQLAlchemy(app)


class data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    height = db.Column(db.Integer, nullable=False)

    def __init__(self, email, height):
        self.email = email
        self.height = height


@app.route("/")
def index():
    return render_template('index.html')


@app.route('/success', methods=['POST'])
def success():
    if request.method == 'POST':
        email = request.form["email_name"]
        height = request.form["height_name"]
        if db.session.query(data).filter(data.email == email).count() == 0:
            data1 = data(email, height)
            db.session.add(data1)
            db.session.commit()
            average_height = db.session.query(func.avg(data.height)).scalar()
            average_height = round(average_height)
            count = db.session.query(data.height).count()
            send_email(email, height, average_height, count)
            return render_template('success.html')
        else:
            return render_template('index.html',
                                   text="We have this email already. Please use another email to enter")


if __name__ == '__main__':
    app.run(debug=True)
