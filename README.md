# Django Success Response

`django-success-response` is a Django REST Framework extension that standardizes success and error response formats in API views. It simplifies response handling by providing a consistent structure and offers easy customization for data formats.

Official Docs: [django-success-response.moorfo.uz](http://django-success-response.moorfo.uz/)

## Installation

Install the package via pip:

```bash
pip install django-success-response
```

## Usage

### Standard Success Response

To return a standard success response, use `SuccessResponse` in your Django views.

#### Example:

```python
from success_response.response import SuccessResponse
from rest_framework.views import APIView

class MyView(APIView):
    @staticmethod
    def get(request):
        data = {'key': 'value'}
        return SuccessResponse(data)
```

#### Response:

```json
{
    "success": true,
    "result": {
        "key": "value"
    }
}
```

### Error Response

For error responses, set `success=False` and provide an error message.

#### Example:

```python
from success_response.response import SuccessResponse
from rest_framework.views import APIView

class MyView(APIView):
    @staticmethod
    def get(request):
        data = {'detail': 'error'}
        return SuccessResponse(data, success=False)
```

#### Response:

```json
{
    "success": false,
    "result": {
        "detail": "error"
    }
}
```

## Error Handling

To format all error responses using the `SuccessResponse` structure, configure the `EXCEPTION_HANDLER` in your `settings.py`:

```python
REST_FRAMEWORK = {
    'EXCEPTION_HANDLER': 'success_response.views.success_exception_handler'
}
```

## Generic Views and ViewSets

`django-success-response` provides customized DRF generic views and viewsets that automatically return responses in the `SuccessResponse` format.

### Available Views and ViewSets:

| Standard View                  | Success Equivalent                     |
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