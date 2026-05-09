from pydantic import BaseModel, ConfigDict
class Book(BaseModel):
    id: int
    title: str
    author: str
    publisher: str
    published_date: str
    page_count: int
    language: str

class BookUpdateModel(BaseModel):
    title:   str
    author: str
    publisher: str
    page_count: int
    language: str
    model_config = ConfigDict(extra="forbid")
    # ConfigDict(extra="forbid") allows us to prevent extra fields from being included in the request body when updating a book. 
    # This means that if a client tries to send additional fields that are not defined in the BookUpdateModel, 
    # the request will be rejected with a validation error.
