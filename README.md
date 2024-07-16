
# Todo List API

This is a Django project with a RESTful API to manage a todo list, incorporating email and Google Sign-In authentication.

## Setup Instructions

### 1. Clone the Repository

Clone the repository to your local machine:

```sh
git clone <repository-url>
cd todo_project
```

### 2. Create and Activate a Virtual Environment

Create a virtual environment and activate it:

```sh
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install Dependencies

Install the required dependencies using `pip`:

```sh
pip install -r requirements.txt
```

### 4. Create a `.env` File

Create a `.env` file in the root directory of your project and add the following content:

```env
GOOGLE_CLIENT_ID=your-client-id.apps.googleusercontent.com
GOOGLE_SECRET=your-client-secret
```

Replace `your-client-id` and `your-client-secret` with your actual Google OAuth credentials.

### 5. Run Migrations

Apply the migrations to set up the database:

```sh
python manage.py makemigrations
python manage.py migrate
```

### 6. Create a Superuser

Create a superuser to access the Django admin interface:

```sh
python manage.py createsuperuser
```

Follow the prompts to set up the superuser account.

### 7. Run the Development Server

Start the development server:

```sh
python manage.py runserver
```

### 8. Access the API Endpoints

You can now access the API endpoints and the Django admin interface:

- Django Admin: `http://127.0.0.1:8000/admin/`
- API Root: `http://127.0.0.1:8000/api/`

### 9. Setting Up Email Authentication

By default, the project uses the console email backend, which outputs emails to the console. To set up email authentication with a real email backend, update the `EMAIL_BACKEND` setting in `todo_project/settings.py`:

```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.example.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@example.com'
EMAIL_HOST_PASSWORD = 'your-email-password'
```

Replace the placeholder values with your actual email server settings.

### 10. Setting Up Google Sign-In Authentication

1. **Configure Google API Console:**
   - Go to the [Google API Console](https://console.developers.google.com/).
   - Create a new project.
   - Under "OAuth consent screen", configure the consent screen.
   - Under "Credentials", create OAuth 2.0 Client IDs. Set the authorized redirect URIs to `http://127.0.0.1:8000/auth/complete/google/`.

2. **Update Django settings:**
   Ensure that your `SOCIALACCOUNT_PROVIDERS` in `settings.py` is correctly configured:

   ```python
   SOCIALACCOUNT_PROVIDERS = {
       'google': {
           'SCOPE': [
               'profile',
               'email',
           ],
           'AUTH_PARAMS': {
               'access_type': 'online',
           },
           'CLIENT_ID': os.getenv('GOOGLE_CLIENT_ID'),
           'SECRET': os.getenv('GOOGLE_SECRET'),
       }
   }
   ```

### 11. Testing

Run the tests to ensure everything is working correctly:

```sh
python manage.py test
```

### API Endpoints

- **List all todo items**: `GET /api/todos/`
- **Retrieve a single todo item by ID**: `GET /api/todos/<id>/`
- **Create a new todo item**: `POST /api/todos/`
- **Update an existing todo item**: `PUT /api/todos/<id>/`
- **Delete a todo item**: `DELETE /api/todos/<id>/`

### Authentication Endpoints

- **Email Registration**: `POST /auth/registration/`
- **Email Login**: `POST /auth/login/`
- **Google Login**: `GET /auth/google/login/`

This setup ensures that only authenticated users can access the todo list API endpoints.

## Filtering and Pagination

You can add filtering capabilities to the list endpoint (e.g., filter by due date, completed status) and implement pagination by extending the `TodoViewSet` and adding relevant settings in `settings.py`.

## Validation

The `Todo` model includes validation to ensure the due date is in the future.

---

By following these instructions, you should be able to set up and run the Todo List API project successfully.
