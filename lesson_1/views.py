from django.http import HttpRequest, HttpResponse


def hello(request: HttpRequest) -> HttpResponse:
    return HttpResponse("""
                        <title>Hello World</title>
                        <h1>Hello World!</h1>
                        <p>Django є одним з найбільших framework на Python</p>
                        """)

