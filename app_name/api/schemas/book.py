from flask_restx import fields
from app_name.api.restplus import api


book_author_schema = api.model('Book Author', {
    'first_name': fields.String(required=True),
    'last_name': fields.String(required=True),
})

book_schema = api.model('Book Schema', {
    "title": fields.String(required=True, description="Book Title"),
    "abstract": fields.String(description="Book Abstract"),
    "year": fields.Integer(required=True, description="Book Year"),
    "status": fields.String(required=True,
                            enum=["active", "loaned", "inactive"],
                            description="Book Status"),
    "authors": fields.List(fields.Nested(book_author_schema)),
})

book_schema_dump = api.clone('Book Schema Dump', book_schema, {
    "id": fields.String(description="Book id"),
})