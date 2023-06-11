from django.db import connection


class LogTenantMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        print(
            f"From Tenant: {connection.tenant.schema_name} | {getattr(connection.tenant, 'domain_url', '')}")
        return response
