from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session

app = Flask(__name__)
HOST = '0.0.0.0'
PORT = '8000'

app = Flask(__name__)
conn = 'mysql+pymysql://{0}:{1}@localhost/{2}'.format(
    "open_root", "open_r00tPass", "users")

app.config['SQLALCHEMY_DATABASE_URI'] = conn
app.config['SECRET_KEY'] = 'secret_key'
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
ses = Session(app)

db = SQLAlchemy(app)

class Temp_table(db.Model):
    username = db.Column(db.String(80), primary_key=True)
    password = db.Column(db.String(80), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = password


@app.route("/", methods=['POST'])
def home():
    data = request.json
    username =data['username']
    password = data['password']
    print(username," ",password)
    new_model = Temp_table(username=username, password=password)
    db.session.add(new_model)
    db.session.commit()
    return render_template('index.html')

if __name__ == "__main__":
    db.create_all()
    app.run(host=HOST,port=PORT, debug=True)
