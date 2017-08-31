from flask import Flask,render_template,request,flash,redirect,url_for,session
from wtforms import StringField, SubmitField,validators, PasswordField, TextAreaField
from flask_wtf import FlaskForm
from flask_mysqldb import MySQL
from passlib.hash import sha256_crypt
from functools import wraps

# 1
app = Flask(__name__)

# 2
#Config to mysql
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'abc230002'
app.config['MYSQL_DB'] = 'FLASKAPP'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'


#Initialize the extension
mysql = MySQL(app)  # 3

@app.route('/')  # 4
def index():  # 5
	return render_template("index.html")  # 6

@app.route('/about')  # 36
def about():
    return render_template("index.html")

# 37
class RegisterForm(FlaskForm):
	# 38
    name = StringField('Name', [validators.Length(min=1, max=50)])
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email', [validators.Length(min=6, max=50)])
	# 39
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords do not match')
    ])
	# 40
    confirm = PasswordField('Confirm Password')

@app.route('/register',methods=["GET","POST"])  # 41
def register():  # 43
    form = RegisterForm(request.form)  # 42
	# 51
    if request.method == 'POST' and form.validate_on_submit():
        name = form.name.data   # 52
        email = form.email.data
        username = form.username.data
		# 53
        password = sha256_crypt.encrypt(str(form.password.data))

		# 54
        ##Creat cursor
        cur = mysql.connection.cursor()
        #Execute query
        cur.execute("INSERT INTO users(name, email, username, password) VALUES(%s, %s, %s, %s)",(name, email,username,password))
        #Commit to DB
        mysql.connection.commit()
        #Close connection
        cur.close()

		# 55
        flash("You are now registered.Please log in.",'success')
		# 56
        return redirect(url_for('index'))
	# 57
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
                return redirect(url_for('dashboard'))
            else:
                error = 'Please check your password.'
                return render_template('login.html', error=error)
            # Close connection
            cur.close()
        else:
            error = 'Username not found'
            return render_template('login.html', error=error)

    return render_template('login.html')


# 67
def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('Unauthorized, Please login', 'danger')
            return redirect(url_for('login'))
    return wrap


#Logout
@app.route("/logout")
@is_logged_in  # 68
def logout():
    session.clear()
    flash("You're now logged out.","success")
    return redirect(url_for('login'))

# 69
@app.route('/dashboard')
@is_logged_in
def dashboard():
    cur = mysql.connection.cursor()

    result = cur.execute("SELECT * FROM articles")

    articles = cur.fetchall()

    if result > 0:
        return render_template("dashboard.html",articles=articles)

    else:
        msg = "No Articles Found"
        return render_template("dashboard.html")

    cur.close()

# 71
class ArticleForm(FlaskForm):
    title = StringField('Title', [validators.Length(min=1, max=200)])
    body = TextAreaField('Body', [validators.Length(min=3)])

# Add Article
# 72
@app.route('/add_article', methods=['GET', 'POST'])
@is_logged_in
def add_article():
    form = ArticleForm(request.form)
    if request.method == 'POST' and form.validate_on_submit():
        title = form.title.data
        body = form.body.data

        # Create Cursor
        cur = mysql.connection.cursor()

        # Execute
        cur.execute("INSERT INTO articles(title, body, author) VALUES(%s, %s, %s)",
                    (title, body, session['username']))

        # Commit to DB
        mysql.connection.commit()

        # Close
        cur.close()

        flash('Article Created', 'success')

        return redirect(url_for('dashboard'))
    return render_template('add_article.html', form=form)


# 74
@app.route('/articles')
@is_logged_in
def articles():
    # Create cursor
    cur = mysql.connection.cursor()

    # Get articles
    result = cur.execute("SELECT * FROM articles")

    articles = cur.fetchall()

    if result > 0:
        return render_template('articles.html', articles=articles)
    else:
        msg = 'No Articles Found'
        return render_template('articles.html', msg=msg)
    # Close connection
    cur.close()

# 76
# Single Article
@app.route('/article/<string:id>/')
@is_logged_in
def article(id):
    cur = mysql.connection.cursor()
    result = cur.execute("SELECT * FROM articles WHERE id = %s", [id])
    article = cur.fetchone()
    return render_template('article.html', article=article)


#78
@app.route('/edit_article/<string:id>', methods=['GET', 'POST'])
@is_logged_in
def edit_article(id):
    # Create cursor
    cur = mysql.connection.cursor()

    # Get article by id
    result = cur.execute("SELECT * FROM articles WHERE id = %s", [id])
    article = cur.fetchone()
    cur.close()

    # Get form
    form = ArticleForm(request.form)

    # Populate article form mysql
    form.title.data = article['title']
    form.body.data = article['body']

    if request.method == 'POST' and form.validate_on_submit():
        title = request.form['title']
        body = request.form['body']

        cur = mysql.connection.cursor()
        cur.execute(
            "UPDATE articles SET title=%s, body=%s WHERE id= %s", (title, body, id))
        mysql.connection.commit()
        cur.close()

        flash('Article Updated', 'success')

        return redirect(url_for('dashboard'))
    return render_template('edit_article.html', form=form)


# 81
# Delete Article
@app.route('/delete_article/<string:id>', methods=["POST"])
@is_logged_in
def delete_article(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM articles WHERE id=%s", [id])
    mysql.connection.commit()
    cur.close()
    flash('Article Deleted', 'success')
    return redirect(url_for('dashboard'))

#CSRF
app.config.from_object('config')

if __name__ == "__main__":  # 83
    #app.secret_key="It doesn't matter"
    app.run(debug=True)  # 84
