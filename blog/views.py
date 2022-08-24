from re import template
from time import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.http import Http404
from django.utils import timezone
from django.shortcuts import render, get_object_or_404 , redirect

# Create your views here.

from .models import BlogPost
from .forms import BlogPostModelForm

def blog_post_list_view(request):
    now =timezone.now()

    #qs=BlogPost.objects.all() #queryset -> list of python object
    qs=BlogPost.objects.filter(publish_date__lte=now)  # for hiding the blogs if it is not published
    template_name = 'list.html'
    context={'object_list':qs}
    return render(request,template_name , context)


# @login_required
@staff_member_required
def blog_post_create_view(request):
    form = BlogPostModelForm(request.POST or None)
    if form.is_valid(): 
        obj = form.save(commit=False)
        obj.title = form.cleaned_data.get("title")
        obj.user =request.user  
        obj.save()
        form =BlogPostModelForm()
    template_name = 'form.html'
    context={'form':form}
    return render(request,template_name , context)

def blog_post_detail_view(request, slug):
    obj = get_object_or_404(BlogPost , slug=slug)
    template_name = 'detail.html'
    context = {"object":obj}  #{"title":obj.title}
    return render(request, template_name, context)

def blog_post_update_view(request,slug):
    obj=get_object_or_404(BlogPost , slug=slug )
    form = BlogPostModelForm(request.POST or None , instance=obj)
    if form.is_valid():
        form.save()
    template_name = 'form.html'
    context = {'form': form, "title": f"Update { obj.title }"}
    return render(request,template_name,context)

def blog_post_delete_view(request, slug):
    obj = get_object_or_404(BlogPost,slug=slug)
    template_name = 'delete.html'
    if request.method == "POST":
        obj.delete() 
        return redirect("/blog")
    context = {"object":obj}
    return render(request,template_name,context)