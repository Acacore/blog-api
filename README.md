# blog-api
A RESTful API for a blogging platform built with Django and Django REST Framework. Supports user authentication, CRUD operations for posts, and filtering by category and author.


# Blog API

A robust, SEO-friendly, and secure backend architecture for a modern content-driven application, built with Django and Django REST Framework.

## Overview
This API leverages a UUID-based primary key system for improved security against ID-enumeration and features automated, conflict-proof slug generation to ensure clean, readable, and SEO-optimized URL routing.



## Key Technical Features
* **Custom User System**: Extends Django's `AbstractUser` for profile management (bios, images) while maintaining native authentication and permission capabilities.
* **Automated URL Routing**: Custom `save()` methods in `Category` and `Post` models handle `slugify` logic, automatically appending counters to resolve naming collisions.
* **Resilient Data Integrity**: Utilizes `models.SET_NULL` for relationships to ensure comment history is preserved even if a user account or parent post is deleted.



## Core Data Models
* **User**: Custom `AbstractUser` using `UUIDField` as the primary key.
* **Category**: Manages content taxonomy with unique slug-based lookup.
* **Post**: Content model featuring status-based workflows (Draft/Published) and automated slug generation.
* **Comment**: Engagement layer linking Users and Posts with persistent deletion logic.

## API Endpoints

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `POST` | `/auth/users/` | Register a new user |
| `POST` | `/auth/jwt/create/` | Obtain JWT access/refresh tokens |
| `GET` | `/api/categories/` | List or create categories |
| `PATCH`| `/api/categories/<slug>/` | Update a category (slug-based) |
| `GET` | `/api/posts/` | List or create posts |
| `PATCH`| `/auth/users/me/` | Update current user profile |

## Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone <your-repository-url>
   cd blog-api
   ```


2. **Install dependencies**:
    ```Bash
    pip install -r requirements.txt
    ```
    

3. **Run migrations**:
    ```Bash
    python manage.py migrate
    ```

4. **Start the development server**:
    ```Bash
    python manage.py runserver
    ```


License
Distributed under the MIT License. See LICENSE for more information.


---

### Pro-Tips for your `README.md`:
* **Environment Variables**: If you are using `python-dotenv` or similar, add a section called "Environment Variables" to list the required keys (e.g., `SECRET_KEY`, `DATABASE_URL`).
* **Contribution Guide**: If you want other developers to help, create a `CONTRIBUTING.md` and link to it here.
* **Deployment**: If you plan to deploy this, add a section on how to serve it using Gunicorn or Nginx later.

Would you like me to draft a `CONTRIBUTING.md` file for you, or perhaps help you write a `requirements.txt` file based on the standard Django/DRF dependencies?