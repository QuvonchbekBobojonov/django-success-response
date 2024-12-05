Here's an example `error_handling.md` for the **django-success-response** documentation:

---

# Error Handling

`django-success-response` provides a standardized way of handling both successful and error responses in your Django REST Framework views. It allows you to format error responses in a consistent structure, making it easier to handle errors across your API.

### 1. Customizing Error Responses

By default, errors in your API responses are structured as follows:

```json
{
    "success": false,
    "result": {
        "detail": "error message"
    }
}
```

This structure helps maintain consistency in your API responses, making it clear whether the response is a success or an error, and what the error message is.

### 2. Using `SuccessResponse` for Error Handling

You can explicitly specify an error response by setting the `success` field to `false` and providing the appropriate error message in the `result` field.

#### Example: Error Response

```python
from success_response.response import SuccessResponse
from rest_framework.views import APIView


class MyView(APIView):
    @staticmethod
    def get(request):
        # Simulating an error
        data = {'detail': 'An error occurred'}
        return SuccessResponse(data, success=False)
```

#### Result:

```json
{
    "success": false,
    "result": {
        "detail": "An error occurred"
    }
}
```

### 3. Global Error Handling with Custom Exception Handler

You can globally customize error handling for all views in your Django project by updating the `EXCEPTION_HANDLER` setting in your `settings.py` file.

In your `settings.py`, add the following configuration:

```python
REST_FRAMEWORK = {
    'EXCEPTION_HANDLER': 'success_response.views.success_exception_handler',
}
```

This ensures that all exceptions raised in your views are caught and formatted using the `SuccessResponse` structure.

### 4. Example: Handling Different Error Types

You can customize the error structure depending on the type of exception or error you want to return. For example, in a view, you can check for specific exceptions and provide custom messages:

```python
from rest_framework.exceptions import NotFound, ValidationError
from success_response.response import SuccessResponse
from rest_framework.views import APIView

class MyView(APIView):
    @staticmethod
    def get(request):
        try:
            # Some operation that may raise an error
            raise ValidationError("This is a validation error.")
        except ValidationError as e:
            return SuccessResponse({'detail': str(e)}, success=False)
        except NotFound as e:
            return SuccessResponse({'detail': str(e)}, success=False)
        except Exception as e:
            return SuccessResponse({'detail': 'An unexpected error occurred.'}, success=False)
```

#### Result (Validation Error):

```json
{
    "success": false,
    "result": {
        "detail": "This is a validation error."
    }
}
```

### 5. Example: Handling Database Errors

For errors such as database issues or missing objects, you can catch and format them as error responses using the `SuccessResponse` structure:

```python
from django.core.exceptions import ObjectDoesNotExist
from success_response.response import SuccessResponse
from rest_framework.views import APIView

class MyView(APIView):
    @staticmethod
    def get(request):
        try:
            # Attempt to retrieve an object from the database
            obj = SomeModel.objects.get(id=1)
        except ObjectDoesNotExist:
            return SuccessResponse({'detail': 'Object not found'}, success=False)
        return SuccessResponse({'data': obj.name})
```

#### Result (Object Not Found Error):

```json
{
    "success": false,
    "result": {
        "detail": "Object not found"
    }
}
```

### 6. Handling Validation Errors

For validation errors, Django REST Framework provides built-in validation mechanisms. You can catch and format those validation errors using `SuccessResponse`:

```python
from success_response.exceptions import SuccessValidationError
from success_response.response import SuccessResponse
from rest_framework.views import APIView

class MyView(APIView):
    @staticmethod
    def post(request):
        # Simulate a validation error
        if 'key' not in request.data:
            raise SuccessValidationError({"detail":"Missing required field: 'key'"})
        
        return SuccessResponse({'message': 'Data received successfully'})
```

#### Result (Validation Error):

```json
{
    "success": false,
    "result": {
        "detail": "Missing required field: 'key'"
    }
}
```

---

Let me know if you'd like to adjust anything or need further assistance!