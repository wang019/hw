from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def index():
    x = "<h1>企管四B查誠麒的求職相關資訊</h1>"
    x += "<a href=/about>查誠麒個人簡介</a><br>"
    x += "<a href=/work>品管工程師工作相關介紹</a><br>"
    x += "<a href=/ucan>職涯測驗分析</a><br>"
    x += "<a href=/autobiography>自傳履歷</a><br>"
    return x


@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/work")
def work():
    return render_template("work.html")
    

@app.route("/ucan")
def ucan():
    return render_template("ucan.html")

@app.route("/autobiography")
def autobiography():
    return render_template("autobiography.html")

#if __name__ == "__main__":
     #app.run()