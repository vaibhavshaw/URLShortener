from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.views import View
from .forms import SubmitUrlForm
from .models import ShortenDB
from django.urls import reverse

# Create your views here.


class Home(View):
    def get(self, request, *args, **kwargs):
        form = SubmitUrlForm()
        title = "Hey! There, This is vit.ly"
        context = {
            "title": title,
            "form": form
        }
        return render(request, 'URLShortener/home.html', context)

    def post(self, request, *args, **kwargs):
        form = SubmitUrlForm(request.POST)
        title = "Submit a Valid URL"
        context = {
            "title": title,
            "form": form
        }
        template = 'URLShortener/home.html'
        if form.is_valid():
            new_url = form.cleaned_data.get("url")
            if 'http' not in new_url:
                new_url = 'http://'+new_url
            obj, created = ShortenDB.objects.get_or_create(url=new_url)
            context = {
                "object": obj,
                "created": created,
            }
            if created:
                template = "URLShortener/success.html"
            else:
                template = "URLShortener/already-exists.html"

        return render(request, template, context)


class URLRedirectView(View):
    def get(self, request, shortcode=None, *args, **kwargs):
        obj = get_object_or_404(ShortenDB, shortcode__iexact=shortcode)
        return HttpResponseRedirect(obj.url)
