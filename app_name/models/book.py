# pylint: disable=too-few-public-methods
from mongoengine import (
    signals,
    EmbeddedDocumentListField,
    IntField,
    StringField
)
from app_name.extensions import db
from app_name.models.base import BaseModel


class BookAuthor(db.EmbeddedDocument):
    """
    Book Author model: Embedded Document
    """
    first_name = StringField()
    last_name = StringField()


class Book(db.Document, BaseModel):
    """
    Book model
    """
    meta = {"collection": "books"}
    title = StringField()
    abstract = StringField()
    year = IntField()
    authors = EmbeddedDocumentListField(BookAuthor)
    status = StringField() # active | loaned | inactive


signals.pre_save.connect(Book.pre_save, sender=Book)
