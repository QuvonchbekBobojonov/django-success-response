from rest_framework.views import exception_handler
from rest_framework import status
from django.utils.translation import gettext_lazy as _
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

        # Replace 'detail' key with 'message' if it exists.
        if 'detail' in data:
            data['message'] = data.pop('detail')

        # If neither 'detail' nor 'message' exists, format the error messages.
        if 'message' not in data:
            data = {
                'message': ' '.join(
                    f"{key}: {' '.join(errors)}" for key, errors in data.items()
                )
            }

        # Wrap the error response in a standardized format using SuccessResponse.
        response = SuccessResponse(
            data,
            success=False,
            status=response.status_code
        )
    else:
        # Handle cases with no response by returning a generic error response.
        response = SuccessResponse(
            {'message': _('Internal Server Error')},
            success=False,
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

    return response
