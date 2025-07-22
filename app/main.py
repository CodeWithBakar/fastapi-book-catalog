from fastapi import FastAPI
from app.controllers import book_controller


app = FastAPI(
    title="Book Catalog API",
    description="A simple RESTful API to manage a catalog of books.",
    version="1.0.0",
)

# Include the book controller router
app.include_router(book_controller.router)


@app.get("/", tags=["Root"])
def read_root():
    return {"message": "Welcome to the Book Catalog API!"}
