from flask import Flask,render_template,request
from datetime import datetime

app = Flask(_name_)

@app.route("/")
def index():
	homepage += "<h1>楊承恩職涯網頁</h1>"
	homepage += "<a href=/相關工作介紹></a><br>"
	homepage += "<a href=/welcome?nick=tcyang>職崖測驗結果</a><br>"
	homepage += "<a href=/about>求職履歷自傳</a><br>"
	return homepage

@app.route("/mis")
def course():
	return "<h1>資訊管理導論</h1>"

@app.route("/today")
def today():
	now = datetime.now()
	return render_template("today.html", datetime = str(now))

@app.route("/about")
def about():
	return render_template("about.html")

@app.route("/welcome", methods=["GET", "POST"])
def welcome():
	user = request.values.get("nick")
	return render_template("welcome.html", name=user)

@app.route("/account", methods=["GET", "POST"])
def account():
	if request.method == "POST":
		user = request.form["user"]
		pwd = request.form["pwd"]
		result = "您輸入的帳號是：" + user + "; 密碼為：" + pwd
		return result
	else:
		return render_template("account.html")

if _name_ == "_main_":
	app.run()