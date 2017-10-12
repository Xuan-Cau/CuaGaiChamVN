import os
from flask import Flask, render_template, redirect, request, redirect
import mlab
from mongoengine import Document, StringField, IntField
from models.girl_type import GirlType,dump_data
mlab.connect()

#import feedparser

#dump_data()

#girl_types.save()
# 1. connect to mlap (x)
# 2. app some data
# 3. Get data for render_template


app = Flask (__name__)


@app.route ('/')
def index ():
    return render_template ('index.html',girl_types = GirlType.objects())

# @ app.route ("/")
# def get_news ():
#          feed = feedparser.parse (RSS_FEEDS [publication])


@app.route("/girl_type/<girl_id>")
def girl_type_detail(girl_id):

    girl_type = GirlType.objects().with_id(girl_id)

    if girl_type is not None:
        return render_template("girl_type_detail.html", girl_type=girl_type)
    else :
        return "<h4> khong thay  </h4>"

# http://127.0.0.1:5000/bmi?height=175&weight=70



#froute
@app.route('/admin')
def hello():
    return render_template("admin.html",girl_types=GirlType.objects())

@app.route ('/delete_girl_type/<girl_id>')
def delete_girl_type(girl_id):
    #1. Delete girl type from database
    girl_type = GirlType.objects().with_id(girl_id)
    if girl_type is not None:
        #Fount it
        girl_type.delete()

    #2. Come back to admin
    return redirect("/admin")

@app.route('/edit_girl_type/edit/<girl_id>')
def edit_girl_type(girl_id):
    girl_type = GirlType.objects().with_id(girl_id)
    if girl_type is not None:
        return render_template ("girl_type_edit.html", girl_type = girl_type)
    return " Loại nè đã tiệt chủng ;) "


if __name__ == "__main__":
    app.run (debug = True)
