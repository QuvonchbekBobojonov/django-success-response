from rest_framework.exceptions import ValidationError
from rest_framework import status as drf_status


class SuccessValidationError(ValidationError):
    """
    Custom validation error to return HTTP 200 OK status and a custom response format.
    The response includes 'saccess' and 'result' to standardize error handling.
    """
    # Override the default status code to always return HTTP 200 OK for this exception.
    status_code = drf_status.HTTP_200_OK

    def __init__(self, detail=None, code=None, success=False):
        """
        Initializes the custom validation error with a modified detail structure.

        :param detail: The error message or details related to the validation error.
        :param code: Optional error code.
        :param success: Optional flag to indicate success (default: False).
        """
        # Customize the detail structure to include the 'success' key along with the error result.
        detail = {'success': success, 'result': detail}

        # Call the parent constructor with the custom detail structure.
        super().__init__(detail, code)
