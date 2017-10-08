import os
from flask import Flask, render_template, redirect, request, redirect,url_for
import mlab
from mongoengine import Document, StringField, IntField
from werkzeug.utils import secure_filename
mlab.connect()

UPLOAD_FOLDER = '/path/to/the/uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

class GirlType(Document):
    name = StringField()
    image = StringField()
    description = StringField()
    detailX = StringField()


#girl_types.save()
# 1. connect to mlap (x)
# 2. app some data
# 3. Get data for render_template


app = Flask (__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route ('/')
def index ():
    return render_template ('index.html',girl_types = GirlType.objects())

@app.route("/about")
def about():
    return "About this page"

# http://127.0.0.1:5000/bmi?height=175&weight=70

@app.route("/bmi")
def bmi():
    print (request.args)
    args = request.args
    weight = int( args["weight"])
    height = int(args["height"]) / 100
    bmi = weight / (height ** 2)

    return str(bmi)


@app.route("/bmi-calc")
def bmi_calc():
    return render_template("bmi_calc.html")

@app.route("/chi-tiet-1")
def chitiet():
    return render_template("chi-tiet-1.html")

#@app.route("/use/<name>/")
#def fnam(name):
#    return "<h3> hello {0} </h3>".format (name)
#https://www.w3schools.com/
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



if __name__ == "__main__":
    app.run (debug = True)
