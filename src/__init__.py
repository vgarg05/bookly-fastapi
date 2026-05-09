from fastapi import FastAPI
from src.books.routes import book_router

version='v1'

app=FastAPI(
    title='Book API',
    description='A REST API for book review web service',
    version=version,
)

app.include_router(book_router,prefix=f'/api/{version}/books',tags=['books'])

# prefix is used to add a common path prefix to all the routes defined in the book_router. 
# In this case, all routes will be prefixed with /api/v1/books. 
# For example, the route for getting all books will be /api/v1/books/ and the route for getting a specific book by ID will be /api/v1/books/{book_id}.


# tags are used to group related routes together in the API documentation. 
# In this case, all routes defined in the book_router will be tagged with 'books' in the API documentation, making it easier for developers to find and understand the available endpoints related to books.