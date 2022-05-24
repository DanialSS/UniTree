from django.shortcuts import render
from django.views import View


class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'landing/index.html')

class Navbar(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'landing/navbar.html')

class Faq(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'landing/faq.html')