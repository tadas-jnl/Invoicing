from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class Index(TemplateView):
    template_name = "core/index.html"

class Example(TemplateView):
    template_name = "core/example.html"