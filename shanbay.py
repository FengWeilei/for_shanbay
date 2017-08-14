from flask import Flask,render_template,request,flash,redirect,url_for,session
from wtforms import StringField, SubmitField,validators, PasswordField, TextAreaField
from flask_wtf import FlaskForm
from flask_mysqldb import MySQL
from passlib.hash import sha256_crypt

app = Flask(__name__)
mysql = MySQL(app)

#Config to mysql
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'abc230002'
app.config['MYSQL_DB'] = 'shanbay'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

@app.route("/")
def index():
	return render_template("index.html")

class RegisterForm(FlaskForm):
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email', [validators.Length(min=6, max=50)])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords do not match')
    ])
    confirm = PasswordField('Confirm Password')

@app.route('/register',methods=["GET","POST"])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate_on_submit():
    	username = form.username.data
    	email = form.email.data
    	password = sha256_crypt.encrypt(str(form.password.data))
    	cur = mysql.connection.cursor()
    	cur.execute("INSERT INTO users(username, email, password) VALUES(%s, %s, %s)",(username, email, password))
    	mysql.connection.commit()
    	cur.close()

    	flash("You are now registered.Please log in.",'success')

    	return redirect(url_for('index'))
    return render_template('register.html',form=form)

#User login
@app.route("/login",methods=['GET','POST'])
def login():
    if request.method == 'POST':
        # Get Form Fields
        username = request.form['username']
        password_candidate = request.form['password']

        # Create cursor
        cur = mysql.connection.cursor()
        # Get user by username
        result = cur.execute(
            "SELECT * FROM users WHERE username = %s", [username])

        if result > 0:
            # Get stored hash
            data = cur.fetchone()
            password = data['password']

            # Compare Passwords
            if sha256_crypt.verify(password_candidate, password):  # 66
                # Passed
                session['logged_in'] = True
                session['username'] = username

                flash('You are now logged in', 'success')
                return redirect(url_for('index'))
            else:
                error = 'Please check your password.'
                return render_template('login.html', error=error)
            # Close connection
            cur.close()
        else:
            error = 'Username not found'
            return render_template('login.html', error=error)

    return render_template('login.html')

#Logout
@app.route("/logout")
def logout():
    session.clear()
    flash("You're now logged out.","success")
    return redirect(url_for('login'))


@app.route('/dashboard')
def dashboard():
    cur = mysql.connection.cursor()

    result = cur.execute("SELECT * FROM words")

    words = cur.fetchall()

    if result > 0:
        return render_template("dashboard.html",words=words)

    else:
        msg = "No words Found"
        return render_template("dashboard.html")

    cur.close()


class WordForm(FlaskForm):
    word = StringField('单词', [validators.Length(min=1, max=200)])
    meaning = TextAreaField('解释', [validators.Length(min=2)])


# Add Word
@app.route('/add_word', methods=['GET', 'POST'])
def add_word():
    form = WordForm(request.form)
    if request.method == 'POST' and form.validate_on_submit():
        word = form.word.data
        meaning = form.meaning.data

        # Create Cursor
        cur = mysql.connection.cursor()

        # Execute

        cur.execute("INSERT INTO words(word, meaning) VALUES(%s, %s)",
                    (word, meaning))

        # Commit to DB
        mysql.connection.commit()

        # Close
        cur.close()

        flash('Word Created', 'success')

        return redirect(url_for('dashboard'))
    return render_template('add_word.html', form=form)

# edit words
@app.route('/words')
def words():
    # Create cursor
    cur = mysql.connection.cursor()

    # Get articles
    result = cur.execute("SELECT * FROM words")

    words = cur.fetchall()

    if result > 0:
        return render_template('words.html', words=words)
    else:
        msg = 'No Words Found'
        return render_template('words.html', msg=msg)
    # Close connection
    cur.close()

@app.route('/word/<string:id>/')
def article(id):
    cur = mysql.connection.cursor()
    result = cur.execute("SELECT * FROM words WHERE id = %s", [id])
    word = cur.fetchone()
    next = int(id) + 1
    previous = int(id) - 1
    return render_template('word.html', word=word, previous=previous, next=str(next))

# Edit word
@app.route('/edit_word/<string:id>', methods=['GET', 'POST'])
def edit_word(id):
    # Create cursor
    cur = mysql.connection.cursor()

    # Get article by id
    result = cur.execute("SELECT * FROM words WHERE id = %s", [id])
    word = cur.fetchone()
    cur.close()

    # Get form
    form = WordForm(request.form)

    # Populate article form mysql
    form.word.data = word['word']
    form.meaning.data = word['meaning']

    if request.method == 'POST' and form.validate_on_submit():
        word = request.form['word']
        meaning = request.form['meaning']

        cur = mysql.connection.cursor()
        cur.execute(
            "UPDATE words SET word=%s, meaning=%s WHERE id= %s", (word, meaning, id))
        mysql.connection.commit()
        cur.close()

        flash('Word Updated', 'success')

        return redirect(url_for('dashboard'))
    return render_template('edit_word.html', form=form)


if __name__ == '__main__':
	app.secret_key="It doesn't matter"
	app.run(debug=True)