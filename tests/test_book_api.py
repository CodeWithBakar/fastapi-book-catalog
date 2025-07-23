class TestBookAPI:
    """Test suite for the Book API endpoints."""

    def test_create_book_api(self, client):
        """Test creating a book successfully."""
        response = client.post(
            "/books/",
            json={
                "title": "API Test Book",
                "author": "API Author",
                "published_year": 2025,
            },
        )
        assert response.status_code == 201
        data = response.json()
        assert data["title"] == "API Test Book"
        assert "id" in data

    def test_read_books_api(self, client, create_book):
        """Test retrieving a list of books."""
        create_book(title="Book 1", author="Author 1")

        response = client.get("/books/")
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        assert len(data) == 1
        assert data[0]["title"] == "Book 1"

    def test_read_single_book_api(self, client, create_book):
        """Test retrieving a single book by its ID."""
        book = create_book(title="Specific Book")

        response = client.get(f"/books/{book.id}")
        assert response.status_code == 200
        data = response.json()
        assert data["id"] == book.id
        assert data["title"] == "Specific Book"

    def test_update_book_api(self, client, create_book):
        """Test updating an existing book."""
        book = create_book(title="Old Title")

        response = client.put(
            f"/books/{book.id}",
            json={
                "title": "New Title",
                "author": book.author,
                "published_year": book.published_year,
            },
        )
        assert response.status_code == 200
        data = response.json()
        assert data["title"] == "New Title"

    def test_delete_book_api(self, client, create_book):
        """Test deleting a book."""
        book = create_book(title="Delete Me")

        delete_response = client.delete(f"/books/{book.id}")
        assert delete_response.status_code == 200

        get_response = client.get(f"/books/{book.id}")
        assert get_response.status_code == 404
