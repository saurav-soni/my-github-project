from flask import Flask, render_template, redirect, url_for, flash
from forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'AJDAYDGAJWDBDJA'
app.config['SQLALCHEMY-DATEBASE-URI'] = 'sqlite3:///site.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(20), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"{self.username}, {self.email}"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey(User.id))

    def __repr__(self):
        return f"{self.title},{self.date_posted}"


posts = [
    {
        'Author': 'author 1',
        'Title': 'tILTLE 1',
        'Content': 'first content',
        'Date_posted': '25th July 2022'
    },
    {
        'Author': 'author 1',
        'Title': 'tILTLE 1',
        'Content': 'first content',
        'Date_posted': '25th July 2022'
    }
]


@app.route('/home')
@app.route('/')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('home.html', title='About')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', form=form, title='Register')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.in' and form.password.data == '12345':
            flash(f'successfully logged in !', 'success')
            return redirect(url_for('home'))
        else:
            flash(f'login not successful. Please check details', 'danger')
    return render_template('login.html', form=form, title='login')


if __name__ == '__main__':
    app.run(debug=True)
