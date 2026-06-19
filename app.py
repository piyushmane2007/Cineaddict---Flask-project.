from flask import Flask, render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
from send_mail import send_mail

app = Flask(__name__) 

ENV = "dev"

if ENV== 'dev':
    app.debug = True
    app.config["SQLALCHEMY_DATABASE_URI"] ="postgresql://postgres:YOUR_PASSWORD@localhost:5432/cineaddict"
else:
    app.debug = False 


app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app) 

class Review(db.Model):
    __tablename__ = 'review'
    id = db.Column(db.Integer, primary_key=True)
    reviewer = db.Column(db.String(200), unique=True)
    movie = db.Column(db.String(200))
    rating = db.Column(db.Integer)
    comments = db.Column(db.Text()) 

    def __init__(self,reviewer,movie,rating,comments):
        self.reviewer = reviewer
        self.movie = movie
        self.rating = rating
        self.comments = comments


@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/submit', methods=['POST'])
def submit(): 
    if request.method == 'POST':
        reviewer=request.form['Reviewer']
        movie=request.form['movie']
        rating=request.form['rating']
        comments=request.form['Comments']
        # print(reviewer,movie,rating,comments)
        if reviewer == "" or movie == "":
            return render_template("index.html",message="Please enter requird fields")
        if db.session.query(Review).filter(Review.reviewer == reviewer).count() == 0:
            data = Review(reviewer,movie,rating,comments)
            db.session.add(data)
            db.session.commit()
            send_mail(reviewer,movie,rating,comments)
        
            return render_template("thankyou.html")
        return render_template("index.html",message="You have already submitted review")
    

if __name__ == '__main__':
    app.run()