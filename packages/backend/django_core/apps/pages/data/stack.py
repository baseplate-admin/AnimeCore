from django.templatetags.static import static

context = {
    "cards": {
        "django": {
            "type": "Web Framework",
            "description": "The web framework for perfectionists with deadlines.",
            "logo": static("images/logos/django.svg"),
        },
        "requests": {
            "type": "HTTP Request library",
            "description": "Requests is an elegant and simple HTTP library for Python,\
                    built for human beings.",
            "logo": static("images/logos/requests.png"),
        },
        "celery": {
            "type": "Task Queue",
            "description": "Distributed Task Queue",
            "logo": static("images/logos/celery.svg"),
        },
    },
}
