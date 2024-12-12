from urllib import request
from django.http import HttpResponse
from django.shortcuts import render

from visits.models import PageVisits



def home_page_views(request, *args, **kwargs):
    qs = PageVisits.objects.all()
    page_qs = PageVisits.objects.filter(path=request.path)
    my_title = "My Page"
    my_context = {
        "page_title": my_title,
        "page_visit_count": page_qs.count(),
        "total_visit_count": qs.count()
    }
    html_template = "home.html"
    PageVisits.objects.create()
    return render(request, html_template, my_context)  