from django.views import generic
from .models import Result
from django.urls import reverse_lazy


class IndexView(generic.ListView):
    model = Result

class DetailView(generic.DetailView):
    model = Result
    
class CreateView(generic.edit.CreateView):
    model = Result
    fields = '__all__'

class UpdateView(generic.edit.UpdateView):
    model = Result
    fields = '__all__'

class DeleteView(generic.edit.DeleteView):
    model = Result
    success_url = reverse_lazy('testapp:index')

