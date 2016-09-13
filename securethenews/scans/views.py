from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Site


def index(request):
    sites = Site.objects.all()
    return render(request, 'scans/index.html', dict(
        sites=sites,
    ))


def site(request, slug):
    site = get_object_or_404(Site, slug=slug)
    return render(request, 'scans/site.html', dict(
        site=site,
    ))
