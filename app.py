from flask import Flask
from flask import render_template
from flask import request
import datetime
import calendar


app = Flask(__name__)

datetime_object = datetime.datetime.now()
pages = 176
pagef=round(pages * (datetime_object.day)/calendar.monthrange(datetime_object.year,datetime_object.month)[1])
percentagef=round((pagef/pages)*100)
@app.route('/')
@app.route("/")
def index():
    return render_template("index.html",percentage=percentagef,page=pagef)


if __name__ == '__main__':
    app.run()
    app.debug = False
