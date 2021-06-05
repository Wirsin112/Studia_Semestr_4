from flask import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, LoginManager, login_user, current_user, logout_user, login_required, login_manager
from werkzeug.security import generate_password_hash, check_password_hash

data = []
Base = declarative_base()
db = SQLAlchemy()
app = Flask(__name__)


class Questionnaire():
    def __init__(self):
        self.engine = create_engine('sqlite:///Ankieta2.db', echo=True)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

    def Add_question(self, Question):
        self.session.add(Question)
        self.session.commit()

    def Add_answer(self, Answer):
        self.session.add(Answer)
        self.session.commit()

    def Get_Questions(self):
        global data
        abc = self.session.query(Question).filter(Question.id != -1).all()
        for i in range(3):
            dikt = {}
            if abc[i].o != None:
                dikt = {'q': abc[i].q,
                        'o': eval(abc[i].o),
                        'a': abc[i].a}
            else:
                dikt = {'q': abc[i].q,
                        'a': abc[i].a}
            data.append(dikt)
        print(data)


class Question(Base):
    __tablename__ = 'Question'
    id = Column(Integer, primary_key=True)
    q = Column(String)
    o = Column(String)
    a = Column(String)

    def __init__(self, q, o, a):
        self.q = q
        self.o = o
        self.a = a


class Answers(Base):
    __tablename__ = 'Answers'
    id = Column(Integer, primary_key=True)
    q1 = Column(String)
    q2 = Column(String)
    q3 = Column(String)

    def __init__(self, q1, q2, q3):
        self.q1 = q1
        self.q2 = q2
        self.q3 = q3


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    name = db.Column(db.String(100))
    password = db.Column(db.String(100))

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        ans = request.form
        err = False
        answer = Answers(ans['0'], ans['1'], ans['2'])
        a = Questionnaire()
        a.Add_answer(answer)
        for qnr, a in ans.items():
            if a != data[int(qnr)]['a']:
                err = True
        if err:
            print("Error")
        else:
            print("ok")
        return redirect(url_for('index'))
    return render_template('index.html', questions=data)


if __name__ == "__main__":
    a = Questionnaire()
    # q1 = Question("Lubisz pyton:", str(["Tak", "Nie", "Dejango"]), "Tak")
    # q2 = Question("Ile to 2+2-1 w slynnej piosence o zimnym facecie:", str(["5", "4", "3"]), "3")
    # q3 = Question("ping:", None, "pong")

    # a.Add_question(q1)
    # a.Add_question(q2)
    # a.Add_question(q3)
    a.Get_Questions()
    app.run()
