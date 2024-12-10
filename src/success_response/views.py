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

        # Ensure the response data is a dictionary for consistent formatting.
        if not isinstance(data, dict):
            # Extract the first error message if the data isn't already a dictionary.
            data = {'detail': ''.join(i for i in data)}

        # Wrap the error response in a standardized format.
        response = SuccessResponse(data, success=False)
    else:
        # Return a generic internal server error response if no response was created.
        response = SuccessResponse(
            {'detail': 'Internal Server Error'},
            success=False,
        )

    return response
