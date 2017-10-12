from mongoengine import Document, StringField, IntField
from faker import Faker

class GirlType(Document):
    name = StringField()
    image = StringField()
    description = StringField()


def dump_data():
    f = Faker ()
    for _ in range(10):
        girl_type = GirlType( name = f.name,
                            image = "http://vietnamshopping.net/wp-content/uploads/2016/01/big-girl-dont-cry-400x200.jpg",
                            description = f.text() )
