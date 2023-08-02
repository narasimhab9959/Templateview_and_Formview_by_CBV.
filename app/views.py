from django.shortcuts import render
from app.forms import *
from django.views.generic import TemplateView,FormView
from django.http import HttpResponse
# Create your views here.

# this is TemplateView by using this we can return data in to HTml page.
class TempDataRender(TemplateView):
    template_name='TempDataRender.html'
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['name']='narasimha'

        return context 

# this is used for Inserting the data by using TemplateView.
class TemplateInsertData(TemplateView):
    template_name='TemplateInsertData.html'

    def get_context_data(self,**kwargs):
        ECDO=super().get_context_data(**kwargs)
        SFO=StudentForm()
        ECDO['SFO']=SFO
        return ECDO

    def post(self,request):
        SFD=StudentForm(request.POST)
        if SFD.is_valid():
            SFD.save()
            return HttpResponse('TemplateInsertData')

class StudentFormviewinsert(FormView):
    template_name='StudentFormviewinsert.html'
    form_class=StudentForm

    def form_valid(self,form):
        form.save()
        return HttpResponse('StudentFormData is inserted')

