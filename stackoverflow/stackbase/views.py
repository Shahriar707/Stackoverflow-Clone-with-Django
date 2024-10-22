from django.shortcuts import render
from django.views.generic import ListView 
from .models import Question

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'base.html')


# CRUD Function

class QuestionListView(ListView):
    model = Question 
    context_object_name = 'questions'
    ordering = ['-date_created']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search_input = self.request.GET.get('search-area') or ""
        if search_input:
            context['questions'] = context['questions'].filter(title__icontains = search_input)
            context['search_input'] = search_input
        return context