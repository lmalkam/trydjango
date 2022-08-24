from multiprocessing import context
from turtle import title
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template
from blog.models import BlogPost

from .forms import ContactForm

def home_page(request):
    my_title= "Welcome to Try Django"
    qs=BlogPost.objects.all()
    context = {"title": my_title, "blog_list":qs}
  #  template_name ="title.txt"
  #  template_obj = get_template(template_name)
  #  rendered_string = template_obj.render(context)
    return render(request, "home.html", context)

def about_page(request):
    context={"title":"About us" , "list":[ 6 , 9]}
    return render(request, "about.html", context)

def contact_page(request):
    print(request.POST)
    form =ContactForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data) 
        form = ContactForm()
    context = {"title": "Contact us", "form":form}
    return render(request, "form.html", context)

def example_page(request):
    context ={"title": "Example"}
    #something_here= "hello.html"
    template_name = "hello.html"
    template_obj = get_template(template_name)
    return HttpResponse(template_obj.render(context))    


def form_page(request):
    context={"title": "form likh do"}
    template_name = "form.html"
    template_obj = get_template(template_name)
    return HttpResponse(template_obj.render(context))