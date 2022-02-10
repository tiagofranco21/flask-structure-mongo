# pylint: disable=too-few-public-methods
"""Base model
"""
from datetime import datetime
from mongoengine import DateTimeField


class BaseModel:
    """Base model
    """

    __abstract__ = True

    date_created = DateTimeField(default=datetime.utcnow)
    date_modified = DateTimeField(default=datetime.utcnow)

    @classmethod
    # pylint: disable=unused-argument
    def pre_save(cls, sender, document, **kwargs):
        document.date_modified = datetime.utcnow
