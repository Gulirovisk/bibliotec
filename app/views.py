from django.shortcuts import render
from django.views import View
from .models import *

class IndexView(View):
    def get(self, request):
<<<<<<< HEAD
        uf = Uf.objects.all()
        return render(request, 'index.html', {'uf': Uf})
=======
        estado = Uf.objects.all()
        return render(request, 'index.html', {'uf': estado})
>>>>>>> 56ca819e743752563115669e6112d16d187fc9e5
    
    def post(self, request):
        pass