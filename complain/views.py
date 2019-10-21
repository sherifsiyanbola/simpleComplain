from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .models import Complain
from django.views.generic import ListView, DetailView
# from django.db.models import Q #Help in multiple filtering
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'index.html')

class complainCreateView(CreateView):
    model = Complain
    template_name = 'dashboard.html'
    fields = ['complaintitle', 'name', 'email','pn', 'gender', 'complain']
    
    def form_valid(self,form):
        instance = form.save(commit=False)
        instance.customer = self.request.user
        instance.save()
        messages.success(self.request, 'You have succesfully submitted your complaint!')
        return redirect('complains')

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["submitted"] = Project.objects.filter(manager=self.request.user).count() 
    #     return context

class complainListView(ListView):
    model = Complain
    template_name = "cview.html"
    context_object_name = "complains"

    def get_queryset(self):
        complains = super().get_queryset()
        return complains.filter(customer=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["treated"] = 'No'
        return context
    

class complainView(UpdateView):
    # model = Complain
    # template_name = "complainview.html"

    # def get_queryset(self):
    #     complains = super().get_queryset()
    #     return complains.filter(customer=self.request.user)
    model = Complain
    template_name = 'complainview.html'
    fields = ['complaintitle', 'name', 'email','pn', 'gender', 'complain']
    
    def form_valid(self,form):
        instance = form.save(commit=False)
        instance.customer = self.request.user
        instance.save()
        messages.success(self.request, 'You have succesfully updated your complaint!')
        return redirect('complains')

class complainDetailView(DetailView):
    model = Complain
    template_name = 'detail.html'

    def get_queryset(self):
        complains = super().get_queryset()
        return complains.filter(customer=self.request.user)

class complainDeleteView(DeleteView):
    model = Complain
    template_name = 'delete.html'
    success_url = '/dashboard/view'


    def delete(self,request, *args, **kwargs):
        # messages.success(self.request, 'Your contact has been succesfully deleted')
        return super().delete(self, request, *args, **kwargs)

