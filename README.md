# FastAPI JWT API

A RESTful API with JWT authentication and Role-Based Access Control (RBAC).

## Features
- User registration and login
- JWT authentication
- Role-based access (Admin/User)
- CRUD operations for projects

## Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/data-scientist-shivam799/coding-sphere
    cd coding-sphere
    ```

2. Create a virtual environment and install dependencies:

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```

3. Configure environment variables by creating a `.env` file:

    ```bash
    SECRET_KEY=yourkey
    MONGO_URI=your_mongo_uri
    ```

4. Run the FastAPI app:

    ```bash
    uvicorn app.main:app --reload
    ```

## Endpoints

- **POST** `/auth/register`: Register a new user
- **POST** `/auth/login`: User login and JWT token generation
- **GET** `/projects`: Retrieve all projects (Read-only for users)
- **POST** `/projects`: Create a new project (Admin only)

## Testing

To run tests, use `pytest`:

```bash
pytest tests/
