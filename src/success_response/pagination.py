from rest_framework.pagination import PageNumberPagination
from .response import SuccessResponse


# Custom pagination class extending PageNumberPagination to return paginated data
# in a consistent format using SuccessResponse.
class SuccessPageNumberPagination(PageNumberPagination):

    # Override the method that generates the paginated response.
    def get_paginated_response(self, data):
        # Use SuccessResponse to wrap the paginated data and include pagination details.
        return SuccessResponse({
            'count': self.page.paginator.count,  # Total number of items.
            'total_pages': self.page.paginator.num_pages,  # Total number of pages.
            'current_page': self.page.number,  # Current page number.
            'next': self.page.next_page_number() if self.page.has_next() else None,  # Next page number (if available).
            'next_link': self.get_next_link(),  # URL link to the next page (if available).
            'previous': self.page.previous_page_number() if self.page.has_previous() else None,
            # Previous page number (if available).
            'previous_link': self.get_previous_link(),  # URL link to the previous page (if available).
            'items': data  # The actual data of the current page.
        })

    # Override to provide a detailed schema for the paginated response, useful for documentation (e.g., OpenAPI/Swagger).
    def get_paginated_response_schema(self, schema):
        # Define the schema for the paginated response.
        return {
            'type': 'object',
            'properties': {
                'count': {
                    'type': 'integer',
                    'example': 100  # Example of the total number of items.
                },
                'total_pages': {
                    'type': 'integer',
                    'example': 10  # Example of the total number of pages.
                },
                'current_page': {
                    'type': 'integer',
                    'example': 1  # Example of the current page number.
                },
                'next': {
                    'type': 'integer',
                    'example': 2,  # Example of the next page number.
                    'nullable': True  # Can be null if there's no next page.
                },
                'next_link': {
                    'type': 'string',
                    'example': 'https://example.com/api/v1/users/?{page_query_param}=2'.format(
                        page_query_param=self.page_query_param),
                    'nullable': True,  # Can be null if there's no next page.
                    'format': 'uri'  # URL format for the next page.
                },
                'previous': {
                    'type': 'integer',
                    'example': 1,  # Example of the previous page number.
                    'nullable': True  # Can be null if there's no previous page.
                },
                'previous_link': {
                    'type': 'string',
                    'example': 'https://example.com/api/v1/users/?{page_query_param}=1'.format(
                        page_query_param=self.page_query_param),
                    'nullable': True,  # Can be null if there's no previous page.
                    'format': 'uri'  # URL format for the previous page.
                },
                'items': schema  # The actual data schema.
            }
        }
