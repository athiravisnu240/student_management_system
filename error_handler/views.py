from django.shortcuts import render
from django.views import generic as views

class Http401ErrorView(views.TemplateView):
    template_name = "errors/401.html"

class Http404ErrorView(views.TemplateView):
    template_name = "errors/404.html"

class Http500ErrorView(views.TemplateView):
    template_name = "errors/500.html"