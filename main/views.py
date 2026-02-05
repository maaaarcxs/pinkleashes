from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import FormView
from . models import Service, Master, Gallery, ServiceType, Review
from . forms import AppointmentMForm, ReviewMForm


class HomepageView(TemplateView):
    template_name = "homepage.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["services"] = Service.objects.all()
        context["masters"] = Master.objects.all()
        context["gallery"] = Gallery.objects.all()
        context["reviews"] = Review.objects.filter(rating__gte=4)
        return context
    

class AboutUsPageView(TemplateView):
    template_name = "aboutus.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["masters"] = Master.objects.all()
        context["services"] = Service.objects.all()
        return context


class ServiceView(ListView):
    model = Service
    template_name = "service.html"
    context_object_name = "services"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["servicetypes"] = ServiceType.objects.all()
        return context


class MastersView(ListView):
    model = Master
    template_name = "masters.html"
    context_object_name = "masters"
    

class MasterDetailView(TemplateView):
    template_name = "aboutmaster.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        master_id = self.kwargs["id"]
        master = get_object_or_404(Master, id=master_id)
        context["master"] = master
        context["reviews"] = Review.objects.filter(master=master_id)
        context["gallery"] = Gallery.objects.filter(service__in=master.services.all())
        return context
    

class AppointmentView(FormView):
    template_name = "base.html"
    form_class = AppointmentMForm
    success_url = reverse_lazy("homepage")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)