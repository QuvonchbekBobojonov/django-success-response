# Welcome to django-success-response Documentation

`django-success-response` is an extension for Django REST Framework (DRF) that standardizes success and error responses in your API views. This package simplifies handling responses by providing a consistent structure for success and error cases, making it easier to maintain and understand the API response format.

## Key Features
- **Standardized Response Format**: Ensures that all API responses follow a uniform structure, making your API easier to use and maintain.
- **Simplifies Response Handling**: Automatically formats success and error responses in your DRF views.
- **Customizable Error Handling**: Provides an easy way to handle errors and return structured error responses.
- **Integration with DRF Views**: Seamlessly integrates with Django REST Framework’s generic views and viewsets to automatically format responses.

## Why Use django-success-response?

In a typical Django REST Framework project, handling success and error responses can become repetitive and inconsistent. `django-success-response` helps to address this by providing a standard format for all responses.

Using this package, you can:
- **Standardize the response structure**: All responses are formatted with `success` and `result` keys.
- **Reduce boilerplate code**: Automatically formats responses without the need to manually structure each response.
- **Easily handle errors**: Return structured error messages using the `success=False` flag.

## Table of Contents
- [Installation](installation.md)
- [Usage](usage.md)
- [Error Handling](error_handling.md)
- [Generic Views and ViewSets](views_viewsets.md)
- [API Reference](api_reference.md)
- [Changelog](changelog.md)

## Installation

To get started with `django-success-response`, install it via pip:

```bash
pip install django-success-response
```

Once installed, you can begin using it in your Django views.

## Basic Example

After installation, you can easily integrate `SuccessResponse` into your views. Here’s a simple example:

```python
from success_response.response import SuccessResponse
from rest_framework.views import APIView

class MyView(APIView):
    @staticmethod
    def get(request):
        data = {'key': 'value'}
        return SuccessResponse(data)
```

This will return a standardized success response like:

```json
{
    "success": true,
    "result": {
        "key": "value"
    }
}
```

### Error Response

If you need to return an error response, simply set `success=False` and provide a detailed error message:

```python
from success_response.response import SuccessResponse
from rest_framework.views import APIView

class MyView(APIView):
    @staticmethod
    def get(request):
        data = {'detail': 'error'}
        return SuccessResponse(data, success=False)
```

This will return an error response:

```json
{
    "success": false,
    "result": {
        "detail": "error"
    }
}
```

For more advanced usage, check out the [Usage](usage.md) page.

## Error Handling

To automatically format all error responses using the `SuccessResponse` structure, configure the `EXCEPTION_HANDLER` in your Django `settings.py` file:

```python
REST_FRAMEWORK = {
    'EXCEPTION_HANDLER': 'success_response.views.success_exception_handler'
}
```

This will ensure that all exceptions in your DRF views are formatted consistently.

## Generic Views and ViewSets

`django-success-response` also provides customized versions of DRF's generic views and viewsets. These views automatically return responses in the `SuccessResponse` format, saving you time and effort.

| Standard View                   | Success Equivalent                     |
|---------------------------------|----------------------------------------|
| `CreateAPIView`                 | `SuccessCreateAPIView`                 |
| `RetrieveAPIView`               | `SuccessRetrieveAPIView`               |
| `UpdateAPIView`                 | `SuccessUpdateAPIView`                 |
| `DestroyAPIView`                | `SuccessDestroyAPIView`                |
| `ListAPIView`                   | `SuccessListAPIView`                   |
| `RetrieveUpdateAPIView`         | `SuccessRetrieveUpdateAPIView`         |
| `RetrieveDestroyAPIView`        | `SuccessRetrieveDestroyAPIView`        |
| `RetrieveUpdateDestroyAPIView`  | `SuccessRetrieveUpdateDestroyAPIView`  |
| `ModelViewSet`                  | `SuccessModelViewSet`                  |
| `ReadOnlyModelViewSet`          | `SuccessReadOnlyModelViewSet`          |

These views behave like their DRF counterparts but automatically format responses using `SuccessResponse`.

## Documentation

- [Installation](installation.md): Learn how to install the package.
- [Usage](usage.md): Explore examples and advanced usage of `SuccessResponse`.
- [Error Handling](error_handling.md): Learn how to configure global error handling.
- [Generic Views and ViewSets](views_viewsets.md): Explore customized DRF views and viewsets for automatic response handling.
- [API Reference](api_reference.md): Detailed reference for all available methods and settings.
- [Changelog](changelog.md): View changes and updates in the package.

---

If you need help or have any questions, feel free to contact us at [contact@moorfo.uz](mailto:contact@moorfo.uz).
```

### Explanation of Sections:
1. **Introduction**: A brief description of the package and its purpose.
2. **Key Features**: Lists the core features of the package, focusing on standardization and simplicity.
3. **Why Use django-success-response?**: Explains the problem the package solves and the benefits it brings.
4. **Table of Contents**: Links to different sections of the documentation for easy navigation.
5. **Installation**: Provides simple steps to install the package via pip.
6. **Basic Example**: A code example demonstrating how to use the package to return a success response.
7. **Error Response**: Shows how to handle error responses using the package.
8. **Error Handling**: Explains how to globally handle exceptions in DRF using the package’s handler.
9. **Generic Views and ViewSets**: Highlights the convenience of using the customized DRF views and viewsets that automatically use the success response format.
10. **Documentation**: Lists links to other important sections in the documentation.
11. **Contact Info**: Provides a way for users to reach out for help or queries.

This structured approach ensures users get a clear understanding of the package and how to use it effectively in their Django projects.
