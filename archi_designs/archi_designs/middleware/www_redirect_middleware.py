from django.http import HttpResponsePermanentRedirect

class WWWRedirectMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.META.get('HTTP_HOST').startswith('www.'):
            new_url = request.scheme + '://www.' + request.META['HTTP_HOST'] + request.path
            return HttpResponsePermanentRedirect(new_url)

        response = self.get_response(request)
        return response
