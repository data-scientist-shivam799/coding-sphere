from mongoengine import Document, StringField

class User(Document):
    username = StringField(required=True, unique=True)
    password = StringField(required=True)  # Hashed password
    role = StringField(required=True, choices=["admin", "user"])

class Project(Document):
    name = StringField(required=True)
    description = StringField(required=True)
