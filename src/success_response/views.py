from rest_framework.views import exception_handler
from .response import SuccessResponse


def success_exception_handler(exc, context):
    """
    Custom exception handler to format all error responses using SuccessResponse.

    :param exc: The exception instance.
    :param context: The context in which the exception occurred.
    :return: Formatted error response.
    """
    # Call the default DRF exception handler for the initial response.
    response = exception_handler(exc, context)

    if response is not None:
        data = response.data

        # Check if 'detail' key exists, otherwise format error messages.
        if 'detail' not in data:
            # If 'detail' is missing, combine all error messages into a single string.
            # For each key in data, join associated errors into a string.
            data = {'detail': ' '.join(f"{key}: {' '.join(errors)}" for key, errors in data.items())}

        # Wrap the error response in a standardized format using SuccessResponse.
        response = SuccessResponse(data, success=False)
    else:
        # If DRF doesn't provide a response, return a generic internal server error response.
        response = SuccessResponse(
            {'detail': 'Internal Server Error'},
            success=False,
        )

    return response
