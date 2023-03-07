from . import db
from werkzeug.security import generate_password_hash



class PropertyInfo(db.Model):
    # You can use this to change the table name. The default convention is to use
    # the class name. In this case a class name of UserProfile would create a
    # user_profile (singular) table, but if we specify __tablename__ we can change it
    # to `user_profiles` (plural) or some other name.
    __tablename__ = 'properties'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(80))
    bedrooms = db.Column(db.Integer)
    bathrooms = db.Column(db.Integer)
    location = db.Column(db.String(255))
    price=db.Column(db.Integer)
    type = db.Column(db.String(30))
    description = db.Column(db.Text())
    photo = db.Column(db.String(200))


    def __init__(self, title, bedrooms, bathrooms, location,price, type, description, photo):
        self.title = title
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
        self.location= location
        self.price=price
        self.type = type
        self.description = description
        self.photo = photo

   # def __repr__(self):
   #     return '<User %r>' % (self.username)