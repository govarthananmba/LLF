class DebugHostHeaderMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print(f"HTTP_HOST: {request.META.get('HTTP_HOST')}")
        response = self.get_response(request)
        return response