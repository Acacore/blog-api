# Blog API
A robust, SEO-friendly, and secure backend architecture for a modern content-driven application, built with Django and Django REST Framework.


## Overview
Custom User System: Extends AbstractUser to support granular roles (Admin, Staff, User) and profile management while utilizing UUIDs for all user identification.

Automated URL Routing: Advanced save() logic in Category and Post models handles slugify operations, automatically appending unique counters to resolve naming collisions.

Resilient Data Integrity: Strategically utilizes models.SET_NULL for relationships to ensure community engagement (comments) remains preserved even if parent records are removed.

Performance Optimized: (Optional but recommended to add) Optimized with select_related and prefetch_related to handle complex relational data with minimal database hits.




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
   git clone git@github.com:Acacore/blog-api.git
   cd blog-api
```

2. **Initialize and activate Virtual Environment**
```bash
    python -m venv venv
    source venv/bin/activate
```

3. **Install dependencies**:
    ```Bash
    pip install -r requirements.txt
    ```

4. **Run migrations**:
 ```bash
    python manage.py migrate
 ```

5. **Optional: Populate Database with Damy data**
 
 ```bash
    python manage.py populate
 ```


6. **Start the development server**:
```bash
    python manage.py runserver
```
---


🌐 Live Demo: 
The API is currently live and hosted on PythonAnywhere. You can interact with the production build here:


**Live Demo**: [https://pythonanywhere.acacore.com](https://pythonanywhere.acacore.com)

🚀 Deployment & CI/CD
This project is deployed using a standard WSGI configuration on PythonAnywhere, focusing on a lightweight and efficient backend footprint.

Server: PythonAnywhere (WSGI-based hosting).

Static Files: Managed via Django collectstatic for optimized delivery.

Environment Security: Sensitive configurations (like SECRET_KEY) are managed via environment variables to keep the codebase secure and production-ready.


## Project Philosophy
The goal of this project was to build a clean, maintainable, and robust RESTful API without unnecessary overhead.

Focus on Core DRF: Leveraging built-in features like ModelViewSets and PermissionClasses to keep the code DRY (Don't Repeat Yourself).

Direct Deployment: A straightforward git-based deployment workflow.

Database: Powered by SQLite3 for simplicity and portability in the current development phase.


Maintained by Acacore


Author
Edoh Mensah Akpedzene
Institution: ALX
Program: ALX Backend
Nexus Poroject Cohort 8 (2026)


License
Distributed under the MIT License. See LICENSE for more information.