from flask import Flask,jsonify
from flask_sqlalchemy import SQLAlchemy
import os

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'student.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db = SQLAlchemy(app)



class Student(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), nullable=False)
  email = db.Column(db.String,nullable=False, unique=True)
  

  review = db.relationship('Review',backref='student',cascade='all,delete,delete-orphan',lazy=True) 

  def __repr__(self):
    return f'<Student(id={self.id}, name={self.name}, gpa={self.email})>'

  def to_dict(self):
    d={}
    #d['id']=self.id
    d['name']=self.name
    d['email']=self.email
    #d['avg_rating'] = self.review.returnAverage() 
    #reviews_dict = [r.to_dict() for r in self.review]
    #d['reviews'] = reviews_dict

    averageRatingsList = [r.returnAverage() for r in self.review]


    totalRating = 0
    for item in averageRatingsList:
        totalRating = totalRating +  item

    if len(averageRatingsList) != 0:
        average = totalRating/len(averageRatingsList)
    else:
        average = 0
    d['avg_rating'] = average

    return d

class Review(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    course=db.Column(db.String(100),nullable=False)
    author=db.Column(db.String(100),default='Anonymous')
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    review=db.Column(db.String(1000), default='This student is the worst student I have seen in all my life.')
    intelligence = db.Column(db.Integer, db.CheckConstraint('intelligence>=0 and intelligence <=5'),default=3)
    attendance = db.Column(db.Integer, db.CheckConstraint('attendance>=0 and attendance <=5'),default=3)
    participation = db.Column(db.Integer, db.CheckConstraint('participation>=0 and participation <=5'),default=3)
    sarcasm = db.Column(db.Integer, db.CheckConstraint('sarcasm>=0 and sarcasm <=5'),default=3)

    def __repr__(self):
        return f'<Blog(id={self.id}, title={self.content}, content={self.content},author={self.author})>'

    def to_dict(self):
        d={}
        d['id']=self.id
        d['course']=self.course
        d['author']=self.author
        d['student_id']=self.student_id
        d['review']=self.review
        d['intelligence']=self.intelligence
        d['attendance']=self.attendance
        d['participation']=self.participation
        d['sarcasm']=self.sarcasm
        return d
    
    def returnAverage(self):
        return (self.intelligence + self.attendance + self.participation + self.sarcasm) / 4


def init_db():

    db.create_all()
    db.session.add(Student(name="David",email='david@svsu.edu'))
    db.session.add(Student(name="Josh",email='josh@svsu.edu', intelligence = 5))
    db.session.add(Student(name="Jane",email='jane@svsu.edu'))
    db.session.add(Student(name="Peter",email='peter@svsu.edu'))
    db.session.add(Student(name="Jack",email='jack@svsu.edu'))
    
    db.session.add(Review(course="CS101",author='Avishek', student_id = 1 ))
    db.session.add(Review(course="CS101",author='George', student_id = 1 ))
    db.session.add(Review(course="CS102",author='Sahil', student_id = 2 ))
    # db.session.add(Blog(title="Blog 2",author=1))
    # db.session.add(Blog(title="Blog 3",author=1))
    # db.session.add(Blog(title="Blog 4",author=2))
    db.session.commit()

#init_db()
@app.route('/')
def index():
    return "Hello World"

@app.route('/students')
def viewAllStudents():
    res = Student.query.all()
    dlist=[r.to_dict() for r in res]
    print(dlist)
    return jsonify(dlist)

@app.route('/students',methods=['POST'])
def updateStudent(studentJSON):
    if request.method == 'POST':
        s1 = Student(email = studentJSON.studentEmail)
        res = Student.query.filter_by(email = studentEmail ).first_or_404()
        dlist=[r.to_dict() for r in res]
        print(dlist)
        return jsonify(dlist)
   
        


@app.route('/student/<studentName>')
def viewStudent(studentName):
    res = Student.query.filter_by(name = studentName ).first_or_404()
    d = res.to_dict()
    return jsonify(d)

@app.route('/student/<studentName>',methods=['DELETE'])
def deleteStudent(studentName):
    res = Student.query.filter_by(name = studentName ).first_or_404()
    db.session.delete(res)
    db.session.commit()
    return jsonify({'message' : 'Success!'})

if __name__ == '__main__':
    app.run(debug=True)

