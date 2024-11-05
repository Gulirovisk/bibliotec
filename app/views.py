from django.shortcuts import render
from django.views import View
from .models import *

class IndexView(View):
    def get(self, request):
        Uf = Uf.objects.all()
        return render(request, 'index.html', {'uf': Uf})
    
    def post(self, request):
        pass