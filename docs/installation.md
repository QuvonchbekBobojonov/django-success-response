# Installation

To install `django-success-response`, follow these simple steps:

### 1. Install via `pip`

You can easily install the `django-success-response` package using `pip`:

```bash
pip install django-success-response
```

This command will install the package and all its dependencies.

### 2. Add to Installed Apps

Once the package is installed, you need to add `success_response` to your `INSTALLED_APPS` in your Django project's `settings.py` file:

```python
INSTALLED_APPS = [
    # Other apps
    'success_response',
]
```

### 3. Configure Django REST Framework

`django-success-response` extends Django REST Framework's response handling. To ensure that error responses are formatted consistently, you can update your Django settings to use the custom exception handler provided by the package.

In your `settings.py`, add or update the following configuration:

```python
REST_FRAMEWORK = {
    'EXCEPTION_HANDLER': 'success_response.views.success_exception_handler',
}
```

This will ensure that all error responses are formatted in the `SuccessResponse` structure.

### 4. Optional: Customizing Response Structure

By default, `SuccessResponse` wraps the response data with a `success` field and a `result` field. You can customize this behavior by modifying the response structure in your views or global settings as needed.