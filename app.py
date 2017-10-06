import os
from flask import Flask, render_template, redirect, request
import mlab
from mongoengine import Document, StringField, IntField

mlab.connect()

class GirlType(Document):
    name = StringField()
    image = StringField()
    description = StringField()

girl_types = GirlType(  name = "Gái tiểu thư",
                        image = "http://via.placeholder.com/400x200",
                        description = "Thường đến các nơi sang chảnh như : royal tea,... thích chỗ sạch sẽ, thích con trai chất chơi")
# girl_types.save()
# 1. connect to mlap (x)
# 2. app some data
# 3. Get data for render_template


app = Flask (__name__)

g_type = [{
        "type" : "Gái tiểu thư ",
        "image" : "http://via.placeholder.com/400x200",
        "description" : "Thường đến các nơi sang chảnh như : royal tea,... thích chỗ sạch sẽ, thích con trai chất chơi."
    },
    {
        "type" : "Gái ngoan ",
        "image" : "http://via.placeholder.com/400x200",
        "description" : " tính bình dân , ăn mặc trẻ như học sinh, già như công sở, chăm học, cẩn thân, hay xuất hiện ở thư viện: L'espace , ... "
    },
    {
        "type" : "Gái hư ",
        "image" : "http://via.placeholder.com/400x200",
        "description" : "Nhìn là biết"
    }
]

#app.config ["DEBUG"] = True

class GirlType(Document):
    name = StringField()
    image = StringField()
    description = StringField()

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

#@app.route("/use/<name>/")
#def fnam(name):
#    return "<h3> hello {0} </h3>".format (name)

@app.route('/shool')
def hello():
    return redirect("http://techkids.vn/")


if __name__ == "__main__":
	app.run (debug = True)
