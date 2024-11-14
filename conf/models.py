from mongoengine import Document, CASCADE
from mongoengine.fields import ListField, StringField, ReferenceField, BooleanField


class Author(Document):
    fullname = StringField(max_length=200, required=True)
    born_date = StringField()
    born_location = StringField(max_length=100)
    description = StringField()


class Quotes(Document):
    tags = ListField()
    author = ReferenceField(Author, reverse_delete_rule=CASCADE)
    quote = StringField()


class Contact(Document):
    fullname = StringField(required=True)
    email = StringField(required=True)
    sent = BooleanField(default=False)
