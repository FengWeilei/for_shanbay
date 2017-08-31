# webapp based on python flask framework

1 app = Flask(__name__)  #实例化Flask类，传入name参数

The only required argument to the Flask class structure is the name of the main module or package of the application.
Flask uses this argument to determine the root path of the application so that it later can find resource files relative to the location of the application.
If you are using a single module, __name__ is always the correct value.


2 对mysql进行一些简单的配置：
以app.config['MYSQL_DB'] = 'FLASKAPP'为例
app是实例化的Flask类，继承了Flask类的方法
config是其中的一个方法，用.来调用config方法
这里设置使用MySql中的“FlaskApp”数据库。


3 mysql = MySQL(app)　来实例化一个mysql对象，传递了app参数。
在这之前有from flask_mysqldb import MySQL 语句 来导入MySql类。

http://flask-mysqldb.readthedocs.io/en/latest/ 中有介绍：
class flask_mysqldb.MySQL(app=None)
connection： Attempts to connect to the MySQL server.
Returns:	Bound MySQL connection object if successful or None if unsuccessful.


4 @app.route('/')
The application needs to know what code needs to run for each URL requested, so it keeps a mapping of URLs to Python functions.
The association between a URL and the function that handles it is called a route.
The app.route decorator defines a route in a Flask application, which registers the decorated function as a route.


5 def index():
	return render_template("index.html")

The index() is called a view function.
A response returned by a view function can be a simple string with HTML content, it can also take more complex forms.

这里提到了响应，就是访问这个URL地址，页面会显示什么。
这里响应是一个index.html的模板


6 render_template("index.html")

(1) To render a template you can use the render_template() method.
(2) The render_template() method provided by Flask integrates the Jinja2 template engine with the application.
(3) All you have to do is provide the name of the template and the variables you want to pass to the template engine as keyword arguments.
(4) Any additional arguments are key/value pairs that represent actual values for variables referenced in the template. For example, form=form.


7 到index.html中， {% extends 'layout.html'%}

{% ... %} for statements
这里使用了模板继承（Template Inheritance）。
The extends directive declears that this template derives from layout.html.
和python中类的继承类似。


8 {% block body %}

The block tags define elements that a derived template can change.
block概念相当于html中的标签的概念，必须成对出现，最后使用了{% endblock %}

9 <div>

<div> 可定义文档中的分区或节（division/section）。
<div> 标签可以把文档分割为独立的、不同的部分。它可以用作严格的组织工具，并且不使用任何格式与其关联。
如果用 id 或 class 来标记 <div>，那么该标签的作用会变得更加有效。

这里class都是CSS的属性。
class="jumbotron text-center" 为<div>标签class属性定义了两个值。
class="jumbotron"表示超大屏幕，该组件可以增加标题的大小，并为登陆页面内容添加更多的外边距（margin）。
class="text-center"表示文字居中。
或者可以试一下class="text-align:center"


10 <h1>FlaskApp</h1> 表示以及标题，大多数情况下，标签最后都要用</>来结束标签。
还有<h2>~<h6>标签。
<p>标签表示段落。


11 刚才index.html继承了layout.html中的内容，然后layout.html
html文件的基本结构
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title></title>
	</head>
	<body>

	</body>
</html>

<!DOCTYPE html> 是一个申明，表示这是一个HTML5文档。


12  <html>可告知浏览器其自身是一个 HTML 文档。
<html> 与 </html> 标签限定了文档的开始点和结束点，在它们之间是文档的头部和主体。


13 <head>
<head> 标签用于定义文档的头部，它是所有头部元素的容器。<head> 中的元素可以引用脚本、指示浏览器在哪里找到样式表、提供元信息等等。
文档的头部描述了文档的各种属性和信息，包括文档的标题、在 Web 中的位置以及和其他文档的关系等。绝大多数文档头部包含的数据都不会真正作为内容显示给读者。
下面这些标签可用在 head 部分：<base>, <link>, <meta>, <script>, <style>, 以及 <title>。
<title> 定义文档的标题，它是 head 部分中唯一必需的元素。


14 <title>FlaskApp</title>
<title> 元素可定义文档的标题。
浏览器会以特殊的方式来使用标题，并且通常把它放置在浏览器窗口的标题栏或状态栏上。


15 <link rel="stylesheet" type="text/css" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">

这里链接了一个外部样式表（CSS），外部样式表规定背景样式、字体样式等等。
<link> 标签定义文档与外部资源的关系。
rel规定当前文档与被链接文档之间的关系。
rel="stylesheet" 表示文档的外部样式表。
type 属性规定被链接文档的 MIME 类型。
这里type="text/css"，该类型描述样式表。
href 属性规定被链接文档的位置（URL），这里使用了https://www.bootstrapcdn.com/ 提供的外部样式表。


16 body 元素定义文档的主体。
body 元素包含文档的所有内容（比如文本、超链接、图像、表格和列表等等。）


17 {% include 'includes/_navbar.html' %}
nav 标签太长了，单独写了_navbar.html文件来存放。
这里使用include 方法调用_navbar.html中的内容。
Portions of template code that need to be repeated in several places can be stored in a separate file and included from all the templates to avoid repetition.


18 切换到_navbar.html
<nav> 标签定义导航链接的部分。
class="navbar navbar-default" 这里用的是bootstrap 类
class="navbar"表明这是一个导航条。
class="navbar-default"定义导航条颜色。
注释15中使用了bootstrapcdn的CSS表，这里navbar-default会默认使用bootstrapcdn中CSS表定义的颜色来作为导航栏的背景色。


19 bootstrap 应该早点儿看，天啊，整个app代码都能在bootstrap中找到出处。
Bootstrap是一组用于网站和网络应用程序开发的开源前端（所谓“前端”，指的是展现给最终用户的界面。与之对应的“后端”是在服务器上面运行的代码）框架，包括HTML、CSS及JavaScript的框架，提供字体排印、窗体、按钮、导航及其他各种组件及Javascript扩展，旨在使动态网页和Web应用的开发更加容易。

Bootstrap对一系列HTML组件的基本样式进行了定义，并且为文本、表格和表单元素设计了一套独特的、现代化的样式。

除了基本HTML元素，Bootstrap还包括了其他常用的界面元素，例如带有高级功能的按钮（例如按钮组合、带有下拉菜单选项的按钮、导航栏、水平和垂直标签组、导航、分页等等）、标签、高级排版、缩略图、警告信息、进度条等。
这些组件都使用CSS的类实现。在页面中需要将其对应到特定的HTML元素上面。


20 <div class="navbar-header">

What does “navbar-header” class do in Bootstrap?
(From stackoverflow.)

The navbar-header is mostly an architectural class for Bootstrap navbar. It allocates approximately 150px to the left of the navbar to wrap the navbar-brand and allow the brand name or logo to make use of the entire area on click or hover. But the most useful property of the navbar-header is its responsiveness to 100% width on and after 768px (tablet views). This allows the brand to be centered at the top of the viewport which it is a nicety to have to avoid your responsive menu overlapping your brand when it opens. EDIT --> The navbar-brand doesn't respond to 100% width.

But you are right, little it's said about this class in the web, because it doesn't per se execute a function. Most people just either leave it alone, replace it, or use it as a hook (parent) class to target the navbar-brand or any other element they wanted to include within.


21 <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">

这几行是从getbootstrap网站例子中复制过来的。

为了给导航栏添加响应式特性(响应式网页设计意思就是把网页的宽度兼容多分辨率的意思)，您要折叠的内容必须包裹在带有 class .collapse、.navbar-collapse 的 <div> 中。折叠起来的导航栏实际上是一个带有class .navbar-toggle 及两个 data- 元素的按钮。第一个是 data-toggle，用于告诉 JavaScript 需要对按钮做什么，第二个是 data-target，指示要切换到哪一个元素。三个带有 class .icon-bar 的 <span> 创建所谓的汉堡按钮。这些会切换为 .nav-collapse <div> 中的元素。为了实现以上这些功能，您必须包含 Bootstrap 折叠（Collapse）插件。


22 <span class="sr-only">Toggle navigation</span>

sr-only全称是 screen reader only，意为：（仅供）屏幕阅读器，这个 class 主要用于增强 accessbility（可访问性）。

有时候 UI(User Interface,用户界面)上会出现一些仅供视觉识别的元素，比如说“汉堡包菜单按钮”，只有视力正常的人才能清楚辨识这些元素的作用。而残障人士，比如弱势或盲人是不可能知道这些视觉识别元素是什么的。他们上网使用的是屏幕阅读器，也就是 screen reader（sr），屏幕阅读器需要找到能辨识的文本说明然后“读”出来给用户听。问题是图形元素怎么可能“读出来”呢？因此我们还要写上这些元素的文本说明，但是又不需要展示给普通用户看到，于是加上 sr-only 的意义就在于能保证屏幕阅读器正确读取且不会影响 UI 的视觉呈现。
改变浏览器的大小就会看到变化。


23 <span class="icon-bar"></span>

<span></span>是行内元素，它占它自身大小的位置，而且不能设置宽高以及边距。
<span>的存在就是方便你给行内元素应用一些样式，但它本身并没有什么意义，就是说span标签没有语义。

icon-bar是小尺寸时用来存放隐藏菜单项的。
小尺寸时，注释25中内容会被隐藏。
这里连用了三个，两个时候显示的效果和三个一样啊。


24 <a class="navbar-brand" href="#">Flaskapp</a>

为FlaskApp设置了一个超链接。
class="navbar-brand"可以让字体看起来大一些。
ref="#" 没有设置地址，点击FlaskApp还会留在原网页。


25 <div id="navbar" class="collapse navbar-collapse">

<div>定义了一个新的分区。
id具有唯一性，指的是这个id不能重复使用。可以通过id来访问这个div内容。
这个分区的class有两个属性。
collapse有折叠的意思。就是页面显示不下那么多内容时，这些内容会被折叠起来。


26 <ul class="nav navbar-nav">
		<li class="active"><a href="/">Home</a></li>
		<li><a href="/about">About</a></li>
		<li><a href="/articles">Articles</a></li>
	</ul>

这里定义了一个列表,class="nav navbar-nav"表明这是导航栏。
第一个<li>标签定义了class="active",导航栏中Home会高亮。
<a>标签定义链接，href属性指向链接地址，这里"/about"和flaskapp.py中定义的路由相对应。


27 <ul class="nav navbar-nav navbar-right">
这里class属性多了navbar-right值，导航标签会显示在屏幕右边。


28 <ul class="nav navbar-nav navbar-right">
		{% if session.logged_in %}  <!-- 28 -->
			<li><a href="/dashboard">Dashboard</a></li>
			<li><a href="/logout">Logout</a></li>
		{% else %}
			<li><a href="/register">Register</a></li>
			<li><a href="/login">Login</a></li>
		{% endif %}
	</ul>

这里使用了jinja2中的条件语句，用户登录时会创建一个session,设置了logged_in=True,如果条件语句成立（用户登录），显示Dashboard链接和Louout链接，否则显示Register和login链接。


29 讲完了_navbar.html，回到layout.html
<div class="container">

Bootstrap需要为页面内容和栅格系统包裹一个容器（container）.
.container 用于固定宽度并支持响应式布局的容器。
.container-fluid 用于100%宽度，占据全部视口（viewport）的容器。


30 {% include 'includes/_messages.html' %}

这里和_navbar 一样（注释17），定义显示的消息内容太多，另外写了一个_messages.html的文档。用include方法来调用_messages.html中的内容。


31 转到_messages.html中。
{% with messages = get_flashed_messages(with_categories=true) %}
	{% if messages %}
		{% for category, message in messages %}
			<div class="alert alert-{{ category }}" >{{ message }}</div>
		{% endfor %}
	{% endif %}
{% endwith %}

The with statement makes it possible to create a new inner scope.
jinja2中语法，with ... 理解成python中的 while/for 语句
http://flask.pocoo.org/docs/0.10/patterns/flashing/ 中有介绍。
get_flashed_messages()用来接收flash中的消息。（注释55）
例如flaskapp.py中语句flash("You are now registered.Please log in.",'success')
messages = get_flashed_messages(with_categories=true)会判断有没有传入flash语句和flash语句的种类。
然后if语句会按照flash语句内容和种类来输出flash语句。
{{ message }}  {{ ... }} for Expressions to print to the template output. 这里会输出flash语句。

 class="alert alert-{{ category }}"
 使用flash（）方法时传入了两个参数，输出语句和类型，类型有success，danger 等。
 这里使用的仍然是boostrap class. class="alert"表示警告，alert-success 颜色是绿色，alert-danger 颜色是红色。


32 {% if error %}
	   <div class="alert alert-danger">{{error}}</div>
	 {% endif %}
	 {% if msg %}
	   <div class="alert alert-success">{{msg}}</div>
	 {% endif %}

这里没有使用get_flashed_messages（）方法，而是直接将要输出的消息传入jinja2模板。
{% if error %} 如果传入了error 消息，按照class="alert alert-danger" 的方式输出error消息。（注释31）
{{ ... }} for Expressions to print to the template output. 这里会输出传入的error消息。
例如flaskapp.py中的：
error = 'Please check your password.'
return render_template('login.html', error=error)
会将传入login.html模板中的error消息输出，背景色为红色。（login.html模板会有相应的模板继承方法来使用_messages.html中的语句。）
{% if msg %} 同理。


33 回到layout.html
{% block body%}{% endblock %}

The block tags define elements that a derived template can change.（注释8）
这里没什么用，去掉也不影响。这里<div class="container">定义了一个分区，调用_messages.html中的方法来输出消息。
但是_messages.html中已经能直接输出消息，这一句删除了也不影响。


34 <script type="text/javascript" src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>

<script> 标签用于定义客户端脚本，比如 JavaScript。
JavaScript 的常见应用于图像操作、表单验证以及动态内容更新。
type属性指示脚本的 MIME 类型。
MIME (Multipurpose Internet Mail Extensions) 是描述消息内容类型的因特网标准。MIME 消息能包含文本、图像、音频、视频以及其他应用程序专用的数据。

src属性规定外部脚本文件的 URL。这里直接使用bootstrapcdn网站提供的JavaScript文件。


35 这里使用ckeditor替换原本的web表单中的输入框（web表单在后面的注释）。

<script src="//cdn.ckeditor.com/4.7.1/basic/ckeditor.js"></script>
<script type="text/javascript">
	CKEDITOR.replace('editor')
</script>

http://cdn.ckeditor.com/ 网站有js地址和使用方法。
这里使用replace()方法替换id=editor 的编辑器（或者只是个输入框）。
（注释25中提到过id具有唯一性，一个标签只能有一个id，这里通过id能找到相应的标签。）
对应的add_article.html和edit_article.html中有
{{render_field(form.body, class_="form-control",id="editor")}} 语句。


36 @app.route('/about')
参见注释4~6。


37 class RegisterForm(FlaskForm)

之前有from flask_wtf import FlaskForm 语句导入了FlaskForm类。wtforms中也有Form类，这里flask_wtf是wtforms的扩展包，从flask_wtf中导入了FlaskForm类（运行是提示Form类将会被FlaskForm类取代，所以这里导入了FlaskForm类）

这里定义了一个RegisterForm子类。继承了FlaskForm类中的所有功能。


38 name = StringField('Name', [validators.Length(min=1, max=50)])

这里name变量是RegisterForm的一个属性。

StringField类是从wtforms中导入的基类。
StringField相当于属性type="text" 的<input> 元素。即单行文本输入字段，这个文本输入字段的名字为'Name'。

StringField 构造函数中的可选参数validators 指定一个由验证函数组成的列表，在接受用户提交的数据之前验证数据。
Length()是其中的验证函数，保证用户输入字段长度在1~50之间。


39 password = PasswordField('Password', [
			validators.DataRequired(),
			validators.EqualTo('confirm', message='Passwords do not match')
	])

	email,和username部分和name部分类似。

	password这里，PasswordField 依然是从wtforms中导入的基类。
	password变量会成为RegisterForm的一个属性。
	PasswordField构造函数中有两个参数，Password是密码输入字段的名字。

	[
				validators.DataRequired(),
				validators.EqualTo('confirm', message='Passwords do not match')
	]
	列表用来验证用户输入数据。DataRequired()验证函数确保用户输入数据不为空，EqualTo（）验证函数确保password字段输入数据和confirm字段输入数据相同，如果不同，输出提示消息'Passwords do not match'。


40 confirm = PasswordField('Confirm Password')

这里没有验证函数组成的验证列表，只有名字'Confirm Password'，注释39中用了EqualTo()验证函数，保证Password和confirm这里输入数据一致。


41 @app.route('/register',methods=["GET","POST"])

这里路由的定义和功能在注释4中有介绍。

methods=["GET","POST"] 向app.route 修饰器中添加了methods 参数，告诉Flask 在URL 映射中把这个视图函数注册为GET 和POST 请求来处理程序。
"GET","POST"分别对应了HTTP协议中的GET和POST方法。
Get是用来从服务器上获得数据，而Post是用来向服务器上传递数据。

提交表单大都作为 POST 请求进行处理，因为GET 请求没有主体，提交的数据以查询字符串的形式附加到URL 中，可在浏览器的地址栏中看到。提交表单作为POST 请求进行处理更加便利。

如果没指定methods 参数，就只把视图函数注册为GET 请求
的处理程序。


42 form = RegisterForm(request.form)

request.form 用来接收用户提交表单数据，作为参数传递给RegisterForm类，数据被RegisterForm类中的验证函数验证通过后，会示例化一个form表单对象。

注释38中提到，name、email、password等都是RegisterForm的属性。
form是实例化的RegisterForm对象，依然会拥有这些属性。
form.name自然能访问form表单中name属性。


43  不看中间的if语句，register()视图函数个结构很简单了：
def register():
    form = RegisterForm(request.form)
		return render_template('register.html',form=form)

视图函数就是用户能看到的部分。
注释42中介绍了form = RegisterForm(request.form)语句。

刚开始用户没有输入数据，request.form语句没有意义。网页中只是显示Name，Email等字段（名字加输入框）。
用户输入数据、点击提交后，form表单中就有了用户提交的注册信息。
request.form会接收用户提交的数据，作为参数传递到RegisterForm构造函数，用于实例化form对象。

return语句将form表单作为参数传到register.html模板中，刚开始没有输入数据时，什么都没有。
用户输入数据后会在Name字段等中显示用户输入信息。

注释6中：Any additional arguments are key/value pairs that represent actual values for variables referenced in the template.
所以这里使用form=form传入form参数。



44  转到register.html

{% extends 'layout.html' %} 见注释7。
{% block body %} 见注释8。


45 <h1> 表示一级标题。

{% from "includes/_formhelpers.html" import render_field %}
和python中的import方法类似，表示从_formhelpers.html文件中导入render_field方法。

render_field()方法用来渲染带有一个标签的字段和错误列表（用户输入数据和验证函数不匹配）。
错误列表，这里不用这个方法也没差别。
render_field(field)方法注释48中有介绍，先把register.html中的内容讲完。


46 <form method="POST",action="">

<form>定义供用户输入的HTML表单。
method="POST"定义了表单提交方法为"POST"。注释41,有介绍，Post是用来向服务器上传递数据。
Get是用来从服务器上获得数据，而Post是用来向服务器上传递数据。
提交表单大都作为 POST 请求进行处理，因为GET 请求没有主体，提交的数据以查询字符串的形式附加到URL 中，可在浏览器的地址栏中看到。提交表单作为POST 请求进行处理更加便利。
action 规定当表单提交时向何处发送表单数据，这里没有为action属性设置URL地址，不用向别处发送数据。

47 {{ form.csrf_token }}

写代码时两次遇到这样的问题:信息按照要求填写，其他代码也没问题，提交数据时网页总是没有反应。
加上了{{ form.csrf_token }}代码后，顺利提交了。
网站为了保护自己不受csrf的攻击，需要用户提交密钥，验证身份。
这里为form加上了CSRF密钥，验证通过后能顺利提交表单了。

更多内容可以参考：http://netsecurity.51cto.com/art/201308/407554.htm

恶意网站把请求发送到被攻击者已登录的其他网站时就会引发跨站请求伪造（Cross-Site Request Forgery，
CSRF,CSRF）的攻击。
默认情况下，Flask-WTF 能保护所有表单免受跨站请求伪造（CSRF）的攻击。

CSRF攻击之所以能够成功，是因为攻击者可以伪造用户的请求，该请求中所有的用户验证信息都存在于Cookie中，因此攻击者可以在不知道这些验证信息的情况下直接利用用户自己的Cookie来通过安全验证。由此可知，抵御CSRF攻击的关键在于：在请求中放入攻击者所不能伪造的信息，并且该信息不存在于Cookie之中。鉴于此，系统开发者可以在HTTP请求中以参数的形式加入一个随机产生的token，并在服务器端建立一个拦截器来验证这个token，如果请求中没有token或者token内容不正确，则认为可能是CSRF攻击而拒绝该请求。


48  <div class="form-group">
      {{render_field(form.name,class_="form-control")}}
    </div>

（1）<div>定义了一个分区/节，或者说一个独立的部分。
（2）class="form-group" 定义分区的样式。是一个bootstrap class。
设置了两个输入框之间的间距。
.form-group {
  margin-bottom: 15px;
}

（3）注释45提到了render_field（），render_field()方法用来渲染带有一个标签的字段和错误列表，这里传递了field.name到render_field()方法中。具体解释见注释50。
同时传递了class_="form-control"属性到render_field()方法中，依然是一个bootstrap class。

（4）form.name 视图函数中将form作为参数传入了register.html模板中，form.name来访问form对象中的name属性。
flaskapp.py中name = StringField('Name', [validators.Length(min=1, max=50)])
这里是一个单行文本输入框，名字是Name。

（5）form-control会设置输入框样式(class前面有_可能是因为class是python的保留字，加上_来区分)。
.form-control {
  display: block;
  width: 100%;
  height: 34px;
  padding: 6px 12px;
  font-size: 14px;
  line-height: 1.42857143;
  color: #555;
  background-color: #fff;
  background-image: none;
  border: 1px solid #ccc;
  border-radius: 4px;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, .075);
          box-shadow: inset 0 1px 1px rgba(0, 0, 0, .075);
  -webkit-transition: border-color ease-in-out .15s, -webkit-box-shadow ease-in-out .15s;
       -o-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
          transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
}



49 <p><input type="submit" class="btn btn-primary" value="Submit"></p>

email,username等分区代码和name部分类似。都是有名字，输入框，供用户输入注册信息，
点击提交时，会验证用户注册信息是否满足RegisterForm中定义的验证条件。

<p>标签表示段落。
<input> 标签用于搜集用户信息。上面的wtforms中的StringField相当于type="text"的input标签。
type="submit" 定义提交按钮,会把表单数据发送到服务器。
class="btn btn-primary" 依然是bootstrap class。 btn for botton, btn-primary 定义按钮颜色为蓝色。
value="Submit" 定义这个按钮显示的值为"Submit"

50 转到_formhelpers:
{% macro render_field(field) %}  {# 50 #}
  <dt>{{ field.label }}
  <dd>{{ field(**kwargs)|safe }}
  {% if field.errors %}
    <ul class=errors>
    {% for error in field.errors %}
      <li>{{ error }}</li>
    {% endfor %}
    </ul>
  {% endif %}
  </dd>
{% endmacro %}

整个文件用来渲染带有一个标签的字段和错误列表（如果有的话）。
（1）{% macro render_field(field) %}
{{ ... }} for statement
macro 相当于python中的def 关键字，用来定义一个方法。
render_field(field) 使用时需要将渲染的字段作为参数传入render_field方法。
如{{render_field(form.name,class_="form-control")}}

（2）<dt>{{ field.label }}
<dt> 标签定义定义列表中的项目。
{{ field.label }} 用来输出字段中的label属性。这里没有，不输出。

（3）<dd>{{ field(**kwargs)|safe }}
	定义定义列表中项目的描述。
	这里接收一堆传递给WTForms字段函数的参数，为我们渲染字段。
	**kwargs 就是当你传入key=value时存储的字典，函数的参数不确定时，可以使用**kwargs。
	使用 |safe 过滤器告诉 Jinja2 这些数据已经经过 HTML 转义了。

（4） {% if field.errors %}
		    <ul class=errors>
		    {% for error in field.errors %}
		      <li>{{ error }}</li>
		    {% endfor %}
		    </ul>
		  {% endif %}
这里连起来，如果渲染的字段出现了错误，定义一个列表，逐条输出错误信息。
<ul>定义无序列表。
<li>定义列表的项目。

关键是，注册时如果有错误，错误列表只有一个元素，也没有字段标签，这一段代码暂时没啥用。



回到flaskapp.py:
51 if request.method == 'POST' and form.validate_on_submit():
			 ....
			 return redirect(url_for('index'))

if 条件语句，request.method == 'POST'判断表单提交方法是不是"POST"方法。
form.validate_on_submit()判断用户注册信息是不是能通过验证函数然后再提交的。
满足if 条件语句中的条件后执行之后的语句，最后跳转到index页面（路由定义为"/"，注释4~5）。
不满足条件直接执行视图函数中的响应return render_template('register.html',form=form)


52 name = form.name.data

	 访问form表单中name属性的数据，用name变量来存储数据。
	 name变量中的数据等下会被写入MySql数据库中。

	 email = form.email.data
	 username = form.username.data
	 同理。

53 password = sha256_crypt.encrypt(str(form.password.data))

	 使用了passlib.hash中的ha256_crypt（）方法来包装加密password，password不会直接显示用户输入的密码。


54  http://flask-mysqldb.readthedocs.io/en/latest/ 中的方法。

		cur = mysql.connection.cursor()
		cur.execute("INSERT INTO users(name, email, username, password) VALUES(%s, %s, %s, %s)",(name, email,username,password))
		mysql.connection.commit()
		cur.close()

（1）mysql是实例化的MySql类，继承了MySql类中的方法。
flask_mysqldb文件中关于connection方法的介绍。
def connection(self):
		"""Attempts to connect to the MySQL server.

		:return: Bound MySQL connection object if successful or ``None`` if
				unsuccessful.
		"""

（2）这里吧flask程序连接到MYSQL数据库后创建了一个指针，用来执行之后的代码。
注释2配置MySql的时候设置了app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
然后建立了一个cursor，来执行之后的语句，
https://dev.mysql.com/doc/connector-python/en/connector-python-api-mysqlcursor.html
网站中也没有找到为什么。

（3）execute方法会运行之后的MySQL命令。
INSERT INTO 语句用于向表格中插入新的行。INSERT INTO 表名称 VALUES (值1, 值2,....)
我们也可以指定所要插入数据的列：
INSERT INTO table_name (列1, 列2,...) VALUES (值1, 值2,....)

（3）mysql.connection.commit()用来提交数据到MySQL数据库，刚刚只是在指针中运行。
然后用户注册信息就保存在了MySQL数据库中的users表中。

（4）close() 来断开这个MySQL连接。
Use close() when you are done using a cursor. This method closes the cursor, resets all results, and ensures that the cursor object has no reference to its original connection object.


55 flash("You are now registered.Please log in.",'success')
官方介绍：
http://flask.pocoo.org/docs/0.12/patterns/flashing/

这里直接使用flask类中的flash()方法来闪现一条消息。
这里flash()方法里的第一个参数是要显示的消息，第二个参数是消息的种类。
To flash a message use the flash() method, to get hold of the messages you can use get_flashed_messages() which is also available in the templates.
To flash a message with a different category, just use the second argument to the flash() function.

这里提到了get_flashed_messages()方法，注释31中已经使用了这个方法。


56 return redirect(url_for('index'))

if 条件语句运行到最后，返回了一个重定向的响应。最后会转到index页面，（"/"路由定义的index视图函数）
redirect() 是个辅助函数，用来生成HTTP 重定向响应，redirect() 函数的参数是重定向的URL。
这里重定向的地址使用Flask提供的URL生成函数url_for()。
使用url_for()函数映射生成URL，能保证URL和定义的路由兼容，而且修改路由名字后
依然可用。


57 return render_template('register.html',form=form)

register()视图函数最后返回响应是一个register.html模板，同时传入了form参数。
form=form
第一个form是要传递给register.html的参数，第二个form是form变量。
注释42中有form的介绍。
注释6中也提到了：
Any additional arguments are key/value pairs that represent actual values for variables referenced in the template.


58  def login():
				if request.method == 'POST':
			  ...
				return render_template('login.html')

	这个login()视图函数，运行时判断if条件语句是否成立，如果成立，运行if语句之后的代码。
	这里刚开始运行，没有提交数据，会返回一个login.html模板的响应。


59 转到layout.html
（1）{% extends 'layout.html' %} 同注释7，使用了模板继承，在login.html模板中继承layout.html模板的内容。
（2）{{ block body }} 见注释8。
（3）<h1>Login</h1> 表示一级标题。
（4）<form action="", method="POST">  见注释46。
		 <form>表示供用户输入的表单，<form>中action属性规定表单向何处提交，method="POST"表示表单提交方法为"POST"


60 <div class="form-group">
	   <label>Username</label>
		 <input type="text" name="username" class="form-control">
	 </div>

	  见注释48。
		<div>表示一个分区，即一个独立的部分。class="form-group"设置了两个输入框之间的间距。
		<label>标签定义 input 元素的标注。
		<input>定义输入控件。type="text"属性表示这是一个单行输入文本。name="username"属性表示这个输入文本的名字。
		class="form-control"规定了输入框的样式。


61 <button type="submit" class="btn btn-primary">Submit</button>
<botton>定义按钮。
type="submit"定义该按钮为提交按钮。
class="btn btn-primary" 是bootstrap类，btn for button，btn-primary表示按钮为蓝色。


62 if request.method == 'POST'
判断网页请求是不是"POST"(<form>定义表单时指定了"POST"方法)。


63  username = request.form['username']
		password_candidate = request.form['password']

username变量用来存储用户提交的form表单中的username数据。
password_candidate变量 同理。


64  cur = mysql.connection.cursor()
		result = cur.execute("SELECT * FROM users WHERE username = %s", [username])

参考register部分（注释54）。
"SELECT * FROM users WHERE username = %s", [username]
MySQL中的命令，用来查找username=username的数据，这里第一个username是MySQL数据库中的数据，第二个是注释63中的username变量。
%s is a formatter， it tells python to take the variable on the right ,and put it on the replace the %s with its value.


65 if result > 0:
			 data = cur.fetchone()
			 password = data['password']
			 ...

	 else:
			 error = 'Username not found'
			 return render_template('login.html', error=error)

	if result > 0 判断数据数据库中有没有搜索结果，即用户输入的用户名之前有没有注册。
	如果在数据库中查询不到结果，继续留在当前页面，并将错误信息作为参数传到login.html。
	注释32中有输出错误信息的介绍。
	includes/_formhelpers.html中有以下语句，layout.html使用了include方法来调用这些代码，login.html又继承了layout.html模板。
	{% if error %}
	  <div class="alert alert-danger">{{error}}</div>
	{% endif %}

data = cur.fetchone()从查询到的数据中选择第一个。存储造data变量中。
password = data['password'] 这里使用了python中字典查询的方法，将data变量中的password数据存储在password变量中。
（MySQl配置的时候使用了app.config['MYSQL_CURSORCLASS'] = 'DictCursor' 语句）


66  if sha256_crypt.verify(password_candidate, password):
					session['logged_in'] = True
					session['username'] = username
					flash('You are now logged in', 'success')
					return redirect(url_for('dashboard'))
			else:
					error = 'Please check your password.'
					return render_template('login.html', error=error)
			cur.close()

if sha256_crypt.verify(password_candidate, password)
使用passlib.hash库中的ha256_crypt.verify()方法来验证用户输入的密码和数据库中的密码（注册密码）是否形同。
密码一致，执行之后的语句。密码不一致留在当前页面，输出错误信息。

密码一致，创建一个回话，设置session['logged_in'] = True，同时session['username']设置成username变量中的值。
很容易找到session的介绍，这里保持保持用户登录状态，同时在其他页面依然能使用session['username']中的数据（用户名）。

最后cur.close()关闭和MySQL的连接。


67  def is_logged_in(f):
		    @wraps(f)
		    def wrap(*args, **kwargs):
		        if 'logged_in' in session:
		            return f(*args, **kwargs)
		        else:
		            flash('Unauthorized, Please login', 'danger')
		            return redirect(url_for('login'))
		    return wrap

这里定义了一个简单的装饰器，来验证用户是否登录，如果登录，也没有对页面进行什么包装，看不出变化。
如果用户没有登录，闪现一条消息，在重定向到login页面。

def is_logged_in(f)定义一个is_logged_in函数，同时传入f参数。
@wraps(f)对f进行装饰。
def wrap(*args, **kwargs)定义装饰函数，对所有参数进行装饰。
当函数的参数不确定时,可以使用*args 和**kwargs,*args 没有key值,**kwargs有key值。
if 'logged_in' in session 在用户登录时设置了session['logged_in'] = True。
return f(*args, **kwargs) 返回这些参数。


68  @app.route("/logout")
		@is_logged_in
		def logout():
		    session.clear()
		    flash("You're now logged out.","success")
		    return redirect(url_for('login'))

在视图函数之前，先验证用户是否登录（注释67）。
logout实现比较简单，直接清除回话就可以了。
登出之后，后闪现一条消息，然后重定向到login页面。


69 有了前面的基础，剩余的代码就水到渠成了。

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

（1）@app.route('/dashboard') 定义路由，URL为'/dashboard'
（2）URL(Uniform Resoure Locator:统一资源定位器)是对可以从互联网上得到的资源的位置和访问方法的一种简洁的表示，是互联网上标准资源的地址。
（3）@is_logged_in 验证用户是否登录。
（4）def dashboard()定义视图函数，这个最后没有返回响应，而是在条件语句之后啊，可以加上一个响应。
（5）cur = mysql.connection.cursor() 连接MySQL数据库。
（6）result = cur.execute("SELECT * FROM articles") 查找articles表中的所有数据。
		（add_article部分在MySQL创建了articles表，然后会添加文章）
（7）articles = cur.fetchall()抓取articles表中的数据并存储在articles变量中。
（8）
if result > 0:
		return render_template("dashboard.html",articles=articles)
else:
		msg = "No Articles Found"
		return render_template("dashboard.html")

		判断查询结果，数据库中有articles的记录，返回一个dashboard.html的响应，并传入articles参数。
		数据库中没有记录，只返回dashboard.html的模板响应。
（9）cur.close()断开和MySQL数据库的连接。



70 dashboard.html中的内容几乎前面都有解释。

（1）{% extends 'layout.html' %} 使用了模板继承来继承layout.html模板。
（2）{% block body %}{% endblock %}中间内容可被更改。
（3）<h1>Dashboard</h1> 表示一级标题。
（4）<a class="btn btn-success" href="/add_article">Add Article</a>
		<a>标签用来创建一个链接，class="btn btn-success"规定链接类型，btn for button,btn-success表示按钮颜色为绿色。
		href="/add_article"规定链接指向的URL地址。点击Add Article会跳转到指定页面。
（5）<hr> 标签在 HTML 页面中创建一条水平线，可以在视觉上将文档分隔成各个部分
（6）<table class="table table-striped"></table>
		<table> 标签定义 HTML 表格。
		class="table table-striped"是bootstrap类。
		table表明这是一个表格，table-striped可以使奇数行的背景设为灰色。
（7）tr 元素定义表格行，th 元素定义表头，td 元素定义表格单元。
		 这里是一个6行n列的表格。
（8）{% for article in articles %}
			...
		 {% endfor %}
		 刚开始传递了articles参数到dashboard.html中，这里会将articles表中的数据逐行输出。
（9）<td><a href="edit_article/{{article.id}}" class="btn btn-default pull-right">Edit</a></td>
		<td>定义表格单元。这里表格单元和（4）中一样，是一个超链接按钮。
		href="edit_article/{{article.id}}"规定超链接指向的URL地址。
		class="btn btn-default pull-right">
		{{article.id}} {{}}可以显示的内容。这里访问了article中的id属性（MySQL中定义articles表的时候定义了id）。
		btn 按钮。btn-default按钮没有颜色。pull-right按钮右浮动。
（10）这里专门文delete定义了一个form表单，没想通为什么，中间的代码含义很好解释。
<form action="{{url_for('delete_article', id=article.id)}}" method="post">
		<input type="hidden" name="_method" value="DELETE">
		<input type="submit" value="Delete" class="btn btn-danger">
</form>


回到flaskapp.py
71 add_article这儿和register部分一样，这里使用WTForms为添加文章设置了一个表单。
class ArticleForm(FlaskForm):
    title = StringField('Title', [validators.Length(min=1, max=200)])
    body = TextAreaField('Body', [validators.Length(min=3)])

参考注释37~40。


72 add_article部分的路由和视图函数这儿参考注释41~57。
和用户注册一样，用户注册时有五个输入框，用户输入信息点击提交，数据验证通过后会提交到MySQL数据库中。
这里add_article部分相当于有两个输入框，用户输入数据提交，验证函数验证通过后，会记录到MySQL数据库中，然后重定向到dashboard页面。


73 add_article.html模板中简化版的register.html模板。
几乎所有内容都可以在register.html模板的注释中找到解释。
只是在Form.body这一块儿为form.body添加了id属性。
layout.html中使用了CKEDITOR.replace('editor')方法，将输入框替换成了CKEDITOR。
注释35中有详细介绍。
CKEDITOR网站：http://cdn.ckeditor.com/

<div class="form-group">
	{{render_field(form.body, class_="form-control",id="editor")}}
</div>


74 articles 这部分的代码功能很简单，连接数据库，查询articles表中取出所有数据，并将数据存储在articles变量中。
如果查询结果不为空，返回articles.html模板的响应，同时传入articles参数。
如果查询没有结果，将msg消息传入articles.html模板中。
最后断开和数据库的联系。

@app.route('/articles')
def articles():
    cur = mysql.connection.cursor()
    result = cur.execute("SELECT * FROM articles")
    articles = cur.fetchall()
    if result > 0:
        return render_template('articles.html', articles=articles)
    else:
        msg = 'No Articles Found'
        return render_template('articles.html', msg=msg)
    cur.close()


75 articles.html模板中实现的功能也很简单，将flaskapp.py传过来的articles标题各自创建一份链接，按列表输出。

（1）<a class="btn btn-success" href="/add_article">Add Article</a>
定义了一个Add Article超链接（一个按钮），链接地址指向"/add_article"。
（2）<hr> 标签在 HTML 页面中创建一条水平线，可以在视觉上将文档分隔成各个部分。
（3）<ul class="list-group">
		<ul>定义一个无序列表，class="list-group"依然指明这是一个无序列表。
（4）{% for article in articles %}
			 <li class="list-group-item"><a href="article/{{article.id}}">{{article.title}}</a></li>
		 {% endfor %}
		 将articles中的标题数据创建超链接，超链接的URL地址为"article/"和从数据库中article的id属性值，然后逐条输出。


76 article部分功能就是点击articles页面创建的超链接，查看一篇完整的文章。

@app.route('/article/<string:id>/')
def article(id):
    cur = mysql.connection.cursor()
    result = cur.execute("SELECT * FROM articles WHERE id = %s", [id])
    article = cur.fetchone()
    return render_template('article.html', article=article)

（1）@app.route('/article/<string:id>/')这里设置了一个动态路由。
	 	articles.html中article/{{article.id}}可以传递过来，点击不同的文章标题，会跳转到相应的URL地址页面。
（2）"SELECT * FROM articles WHERE id = %s", [id]  语句这里根据id来查询articles表中的数据。
		%s 会将右边的[id]变量的值替换到%s的位置（路由中传入了id变量）。
（3）最后视图函数会返回一个article.html的模板响应，同时传入article参数。

77 article.html中实现的功能也不多。

（1）{% extends 'layout.html' %} 继承了layout.html模板。
（2）{% block body %} 定义一个区块，中间内容可被改变。
（3）<h1>{{article.title}}</h1> 定义一个一级标题，标题内容为article参数的title属性值。
（4）<small>Written by {{article.author}} on {{article.create_date}}</small>
		<small> 标签呈现小号字体效果。同时根据article参数的author属性值和create_date属性值来输出一段话。
		（在MySQL数据库中创建articles表时定义了这些）
（5）为了方便在单独文章也编辑文章，在页面中添加了一个Edit按钮的超链接。
  <a href="http://127.0.0.1:5000/edit_article/{{article.id}}" class="btn btn-default pull-right">Edit</a>
	<a>标签中href属性指向超链接的URL地址，其中前一部分为绝对地址，后一部分加上了article参数的id属性值。
	<a>标签中class属性用来描述这个标签，class属性有三个值，btn for botton,按钮；btn-default，没有颜色的按钮；pull-right 向右浮动。
（6）<hr> 标签在 HTML 页面中创建一条水平线，可以在视觉上将文档分隔成各个部分。
（7）<div>定义一个独立的部分。
（8）{{article.body |safe}} 会输出article的body属性值， |safe告诉python内容已经经过转义。



78 编辑文章这儿的代码可以参考添加文章部分代码。
（1）@app.route('/edit_article/<string:id>', methods=['GET', 'POST'])
		编辑文章这儿首先设置了动态路由，根据每篇文章的id设置一个URL地址。
		请求方法为methods=['GET', 'POST']，GET用来接收数据，POST用来上传数据。
（2）视图函数这儿，首先从数据库中查询到要编辑的文章，编辑框中有了文章供用户编辑。
def edit_article(id):
    cur = mysql.connection.cursor()
    result = cur.execute("SELECT * FROM articles WHERE id = %s", [id])
    article = cur.fetchone()
    cur.close()
    form = ArticleForm(request.form)
    form.title.data = article['title']
    form.body.data = article['body']

（1）def edit_article(id)视图函数中首先传入了id参数（来自动态URL地址中的<string:id>）。
（2）cur = mysql.connection.cursor() 创建和MySQL数据库的联系。
（3）result = cur.execute("SELECT * FROM articles WHERE id = %s", [id]) 按照id查询MySQL数据库中的数据。
（4）查询到之后，取出一组数据，存入article变量中。
（5）cur.close()关闭和数据库的联系。
（6）form = ArticleForm(request.form) 这里使用了add_article部分定义的ArticleForm表单实例化了一个form表单变量。
		form表单变量继承了ArticleForm类中的属性title和body（两个输入框）。
		form.title.data = article['title'] 将数据库中的title数据先填充到form.tiele输入框中。
		form.body.data = article['body']同理。
		这样，form表单中就有了可供用户编辑的数据。



79 if 条件语句这儿只是数据库操作和添加文章部分的代码不同。

（1）if request.method == 'POST' and form.validate_on_submit()
		 判断表单提交方法是不是"POST"请求，在验证用户提交数据能不能通过验证函数的验证。
(2)title = request.form['title']将用户提交的表单中title属性的数据存储在title变量中。
(3)body = request.form['body'] 将用户提交的表单中body属性的数据存储在body变量中。
(4)cur.execute("UPDATE articles SET title=%s, body=%s WHERE id= %s", (title, body, id))
	 add_article中用了INSERT INTO 方法，这里使用了UPDATE 方法。
(5)flash('Article Updated', 'success') flash a message with categories.
(6)return redirect(url_for('dashboard')) if 语句最后重定向到dashboard页面。


80 edit_article.html部分代码和add_article.html部分代码几乎一样。
	 只是修改了标题为<h1>Edit Artitle</h1>。


81 在dashboard页面设置的delete_article的超链接，点击超链接会跳转到相应的URL地址。
   这里依然为每篇文章设置了一个独特的地址。
	 点击删除文章，视图函数中会连接到MySQL数据库，根据文章id来删除文章。
	 这里功能很简单，没有模板响应，最后直接重定向到dashboard页面。


82 app.config.from_object('config')
应用程序需要某种形式的配置才能正常运行。
这里从独立文件config.py中对flaskapp进行配置。
更多介绍参考http://www.pythondoc.com/flask/config.html


config.py中：
CSRF_ENABLED = True设置了启用CSRF验证。
SECRET_KEY = "It doesn't matter" 设置了CSRF密钥。


83 if __name__ == "__main__":

	 在Python中，一个.py文件就是一个模块。
	 全局变量__name__存放的就是模块的名字。
	 当模块被直接运行时模块名为 __main__ 。
	 if __name__ == "__main__": 意思是当代码被直接运行时，执行if 条件语句之后的代码。
（当模块是被导入时，if语句后代码块不被运行。）


84 app.run(debug=True)

最开始示例化了一个app对象 app = Flask(__name__)
这里用 run()方法来让应用运行在本地服务器上。
虽然 run() 方法适用于启动本地的开发服务器，但是每次修改代码后都要手动重启它。
如果启用了调试支持，服务器会在代码修改后自动重新载入，并在发生错误时提供一个相当有用的调试器。

这里直接将debug=True作为 run 方法的一个参数传入，运行时可以启用调试模式。


85 关于在MySQL数据库中建立users表和articles表来保存用户数据。
	 代码如下。
创建users表：
mysql -u root -p
CREATE DATABASE FLASKAPP;
USE FLASKAPP;
CREATE TABLE users(id INT(11) AUTO_INCREMENT PRIMARY KEY, name VARCHAR(100),email VARCHAR(100), username VARCHAR(30), password VARCHAR(100), register_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP);

创建articles表：
mysql -u root -p
CREATE DATABASE FLASKAPP;
USE FLASKAPP;
CREATE TABLE articles (id INT(11) AUTO_INCREMENT PRIMARY KEY, title VARCHAR(200), author VARCHAR(100), body TEXT, create_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP);


86 基本上写完了所有注释，今天8月6号，加了这条注释。
以后的学习，要看RESTful API的设计，MVC模式，然后就是看那些bootstrap开发的网站，理解那些代码。
再然后，补那些算法的知识。
希望能赶紧找到工作，什么工作都行，越学习，感觉需要学习的东西越多。
