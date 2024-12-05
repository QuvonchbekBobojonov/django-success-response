# Django Success Response

`django-success-response` is a Django REST Framework extension that provides a standardized success response format for API views. It simplifies handling both successful and error responses with customizable data structures.

## Installation

Install the package via pip:

```bash
pip install django-success-response
```

## Usage

In your Django views, use `SuccessResponse` to wrap the response data.

### Example: Standard Success Response

```python
from success_response.response import SuccessResponse
from rest_framework.views import APIView


class MyView(APIView):
    @staticmethod
    def get(request):
        data = {'key': 'value'}
        return SuccessResponse(data)
```

### Result:

```json
{
    "success": true,
    "result": {
        "key": "value"
    }
}
```

### Example: Error Response

To handle errors, pass `success=False`:

```python
from success_response.response import SuccessResponse
from rest_framework.views import APIView


class MyView(APIView):
    @staticmethod
    def get(request):
        data = {'key': 'value'}
        return SuccessResponse(data, success=False)
```

### Result:

```json
{
    "success": false,
    "result": {
        "detail": "error"
    }
}
```

## Error Handling

You can also customize Django REST Framework's error responses globally by modifying the `EXCEPTION_HANDLER` setting in your `settings.py`:

```python
REST_FRAMEWORK = {
    'EXCEPTION_HANDLER': 'success_response.views.success_exception_handler'
}
```

This will format all exceptions using the `SuccessResponse` structure.

## Generic Views and ViewSets

This package also provides customized DRF generic views and viewsets for standardized response handling.

| Standard View                  | Success Equivalent                     |
|--------------------------------|---------------------------------------|
| `CreateAPIView`                | `SuccessCreateAPIView`                |
| `RetrieveAPIView`              | `SuccessRetrieveAPIView`              |
| `UpdateAPIView`                | `SuccessUpdateAPIView`                |
| `DestroyAPIView`               | `SuccessDestroyAPIView`               |
| `ListAPIView`                  | `SuccessListAPIView`                  |
| `RetrieveUpdateAPIView`        | `SuccessRetrieveUpdateAPIView`        |
| `RetrieveDestroyAPIView`       | `SuccessRetrieveDestroyAPIView`       |
| `RetrieveUpdateDestroyAPIView` | `SuccessRetrieveUpdateDestroyAPIView` |
| `ModelViewSet`                 | `SuccessModelViewSet`                 |
| `ReadOnlyModelViewSet`         | `SuccessReadOnlyModelViewSet`         |

These classes behave like their DRF counterparts but automatically format responses using `SuccessResponse`.
