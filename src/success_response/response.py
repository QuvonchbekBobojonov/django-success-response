from rest_framework.response import Response
from rest_framework import status as drf_status


# Custom response class that standardizes API responses with an additional
# 'success' field, indicating success or failure, and a 'result' field holding the actual data.
class SuccessResponse(Response):
    def __init__(self, data=None, headers=None, exception=False, content_type=None, success=True, status=drf_status.HTTP_400_BAD_REQUEST):
        # Wrap the data in a standardized format with 'success' indicating success status,
        # and 'result' containing the response payload.
        if success:
            data = {'success': success, 'result': data}
        else:
            data = {'success': success, 'error': {
                'code': status,
                **data
            }}

        # Default the status code to 200 (OK) unless otherwise specified.
        status = drf_status.HTTP_200_OK

        # Call the parent class constructor to build the response with the given data.
        super().__init__(data, status, headers, exception, content_type)
