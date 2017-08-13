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
def login():  # 58
    if request.method == 'POST':  # 62
        # Get Form Fields
        username = request.form['username']  # 63
        password_candidate = request.form['password']

        # Create cursor
        cur = mysql.connection.cursor()  # 64
        # Get user by username
        result = cur.execute(
            "SELECT * FROM users WHERE username = %s", [username])

        if result > 0:   # 65
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



if __name__ == '__main__':
	app.secret_key="It doesn't matter"
	app.run(debug=True)