from flask import request
from flask_restx import Resource, marshal, fields
from mongoengine import ValidationError
from app_name.api.schemas.book import book_schema, book_schema_dump
from app_name.models import BookAuthor, Book
from app_name.api.restplus import api
from app_name.api.middleware import token_required

ns = api.namespace(
    'books', description='Operations related to books')

# Default response for POST and PUT
schema_response = api.model('Book Response', {
    'book_id': fields.String(),
})


@ns.route('/')
class BookCollection(Resource):

    @classmethod
    @ns.marshal_list_with(book_schema_dump)
    def get(cls):
        """
        Returns all books.
        """

        books = Book.objects()

        books_dump = []
        for book in books:
            books_dump.append(marshal(book, book_schema_dump))

        return books_dump

    @classmethod
    @ns.response(201, "Book successfully created.", schema_response)
    @ns.expect(book_schema, validate=True)
    def post(cls):
        """
        Creates a new book.
        """
        data = request.json
        book_new = Book(**data)

        try:
            book_new.save()
        except ValidationError:
            return {"message": "Unexpected error"}, 500

        result = {
            "book_id": str(book_new.id)
        }

        return result, 201


@ns.route('/<string:book_id>')
@ns.response(404, 'Book not found.')
class BookItem(Resource):

    @classmethod
    @ns.marshal_with(book_schema_dump)
    def get(cls, book_id):
        """
        Returns a book.
        """

        book_obj = Book.objects.get_or_404(id=book_id)

        return marshal(book_obj, book_schema_dump)

    @classmethod
    @ns.expect(book_schema, validate=True)
    @ns.response(200, 'Book successfully updated.', schema_response)
    def put(cls, book_id):
        """
        Updates a Book.
        """
        book_obj = Book.objects.get_or_404(id=book_id)
        data = request.json

        for arg in data.keys():
            if arg == "authors":
                book_obj.authors = [BookAuthor(**author)
                                              for author in data["authors"]]
            else:
                setattr(book_obj, arg, data[arg])

        try:
            book_obj.save()
        except ValidationError:
            return {"message": "Unexpected error"}, 500

        result = {
            "book_id": str(book_obj.id)
        }

        return result

    @classmethod
    @ns.response(204, 'Book successfully deleted.')
    @api.doc(security='Authorization')
    @token_required
    def delete(cls, book_id):
        """
        Deletes Book.
        """
        book_obj = Book.objects.get_or_404(id=book_id)

        try:
            book_obj.delete()
        except ValidationError:
            return {"message": "Unexpected error"}, 500

        return None, 204
