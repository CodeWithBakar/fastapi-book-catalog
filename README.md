# 📚 FastAPI Book Catalog API

<div align="center">

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)
![Pytest](https://img.shields.io/badge/pytest-%233776AB.svg?style=for-the-badge&logo=pytest&logoColor=white)

*A comprehensive RESTful API built with FastAPI to manage a catalog of books*


</div>

---

## 🌟 Project Overview

This API provides a complete set of endpoints for **Creating, Reading, Updating, and Deleting (CRUD)** book records. Built with modern Python web development best practices, it demonstrates a clean service-oriented architecture, asynchronous support, comprehensive data validation, and a robust testing suite.

### 🛠️ Core Technologies

| Technology | Purpose | Version |
|------------|---------|---------|
| **FastAPI** | High-performance, asynchronous API framework | Latest |
| **SQLAlchemy** | Object-Relational Mapping (ORM) | Latest |
| **Alembic** | Database schema migrations | Latest |
| **Pydantic** | Data validation, serialization, and settings | Latest |
| **Pytest** | Comprehensive testing framework | Latest |
| **SQLite** | Lightweight database for development | Latest |

---

## ✨ Features

<table>
<tr>
<td>

### 🔄 **Full CRUD Operations**
Complete Create, Read, Update, Delete functionality for book management

### ⚡ **Async Support** 
Asynchronous endpoints for optimal performance

### 🛡️ **Data Validation**
Robust Pydantic models with strict validation rules

</td>
<td>

### 🏗️ **Clean Architecture**
Service-oriented design with clear separation of concerns

### 🔄 **Database Migrations**
Version-controlled schema changes with Alembic

### 🧪 **Comprehensive Testing**
Unit and integration tests ensuring reliability

</td>
</tr>
</table>

### 📋 Feature Checklist

- ✅ **Full CRUD Functionality** - Complete book management endpoints
- ✅ **Asynchronous Endpoints** - High-performance async operations
- ✅ **Robust Data Validation** - Strict validation (e.g., realistic publication years)
- ✅ **Service-Oriented Architecture** - Clean layered design
- ✅ **Database Migrations** - Version-controlled schema management
- ✅ **Comprehensive Testing** - Unit and integration test coverage
- ✅ **Auto-Generated Documentation** - Interactive Swagger UI and ReDoc

---

## 🏗️ Project Architecture

The project follows a **clean, MVC-style architecture** ensuring maintainability and scalability:

```
📁 fastapi-book-catalog/
├── 📁 alembic/                    # Database migration scripts
│   ├── 📁 versions/               # Migration version files
│   └── 📄 env.py                  # Alembic environment config
├── 📁 app/
│   ├── 📁 controllers/            # 🎮 API endpoint definitions (View layer)
│   ├── 📁 services/               # 💼 Business logic layer
│   ├── 📁 repositories/           # 🗄️ Data access layer
│   ├── 📁 models/                 # 📊 SQLAlchemy ORM models
│   ├── 📁 schemas/                # 📋 Pydantic validation schemas
│   ├── 📁 db/                     # 🔌 Database connection setup
│   └── 📄 main.py                 # 🚀 Application entry point
├── 📁 tests/
│   ├── 📁 fixtures/               # 🔧 Reusable test fixtures
│   ├── 📄 test_services.py        # 🧪 Service layer tests
│   └── 📄 test_endpoints.py       # 🌐 API integration tests
├── 📄 alembic.ini                 # ⚙️ Alembic configuration
├── 📄 requirements.txt            # 📦 Project dependencies
└── 📄 README.md                   # 📖 This documentation
```

---

## 🚀 Quick Start

### 📋 Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.11+** 🐍
- **pip** (Python package manager) 📦
- **Git** (for cloning the repository) 📥

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/CodeWithBakar/fastapi-book-catalog.git
cd fastapi-book-catalog
```

### 2️⃣ Set Up Virtual Environment

<details>
<summary>🪟 <strong>Windows</strong></summary>

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\activate
```
</details>

<details>
<summary>🐧 <strong>macOS/Linux</strong></summary>

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
source venv/bin/activate
```
</details>

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Database Setup with Alembic

Initialize your database schema:

```bash
# Apply all migrations to create the database schema
alembic upgrade head
```

> 📝 **Note:** This creates a `book_catalog.db` file in your project root.

### 5️⃣ Start the Server

```bash
uvicorn app.main:app --reload
```

🎉 **Success!** Your API is now running at: http://127.0.0.1:8000

---

## 📖 API Documentation

FastAPI automatically generates beautiful, interactive API documentation:

<div align="center">

| Documentation Type | URL | Description |
|-------------------|-----|-------------|
| **Swagger UI** | http://127.0.0.1:8000/docs | Interactive API testing interface |
| **ReDoc** | http://127.0.0.1:8000/redoc | Clean, responsive documentation |

</div>

### 🔧 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/books/` | List all books (async) |
| `POST` | `/books/` | Create a new book |
| `GET` | `/books/{id}` | Get a specific book |
| `PUT` | `/books/{id}` | Update a book |
| `DELETE` | `/books/{id}` | Delete a book |

---

## 🗄️ Database Management

### Creating Migrations

When you modify SQLAlchemy models, generate new migration scripts:

```bash
# Generate migration automatically
alembic revision --autogenerate -m "Descriptive change message"

# Apply the migration
alembic upgrade head
```

### Migration Commands Reference

| Command | Purpose |
|---------|---------|
| `alembic upgrade head` | Apply all pending migrations |
| `alembic downgrade -1` | Rollback last migration |
| `alembic history` | View migration history |
| `alembic current` | Show current migration version |

---

## 🧪 Testing

The project includes a comprehensive test suite using **Pytest** with isolated, in-memory SQLite databases.

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage report
pytest --cov=app

# Run specific test file
pytest tests/test_services.py

# Run with verbose output
pytest -v
```

### Test Structure

- **Unit Tests** 🔧 - Test individual service methods
- **Integration Tests** 🌐 - Test complete API endpoints
- **Fixtures** 🛠️ - Reusable test data and configurations

---

## 🎯 Development Workflow

### 1. Making Changes
1. Create a feature branch: `git checkout -b feature/your-feature`
2. Make your changes
3. Write/update tests
4. Run the test suite: `pytest`

### 2. Database Changes
1. Modify SQLAlchemy models in `app/models/`
2. Generate migration: `alembic revision --autogenerate -m "description"`
3. Review the generated migration file
4. Apply migration: `alembic upgrade head`

### 3. Deployment Preparation
1. Ensure all tests pass: `pytest`
2. Update documentation if needed
3. Create pull request for review

---

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. **Fork** the repository
2. **Create** a feature branch
3. **Make** your changes with tests
4. **Ensure** all tests pass
5. **Submit** a pull request

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **FastAPI** team for the amazing framework
- **SQLAlchemy** for the powerful ORM
- **Pydantic** for excellent data validation
- **Alembic** for seamless migrations

---

<div align="center">

**[⬆ Back to Top](#-fastapi-book-catalog-api)**

Made with ❤️ and Python 🐍

</div>
