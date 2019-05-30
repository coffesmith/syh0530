from django.shortcuts import render,redirect,get_object_or_404
from .models import Blog
from.forms import BlogForms
# Create your views here.

def home(request):
    blogs = Blog.objects.all
    return render(request, 'home.html', {'blogs': blogs})

def new(request):
    if request.method == 'POST':
        forms = BlogForms(request.POST)

        if forms.is_valid:
            forms.save()
            return redirect('home')            
    forms=BlogForms()
    return render(request,'new.html',{'forms':forms})

def detail(request, blog_id):
        blog_one =get_object_or_404(Blog,id=blog_id)
        context = {'blog_one':blog_one}
        return render(request, 'detail.html',context)

def edit(request,blog_id):
    blog_edit = get_object_or_404(Blog, id = blog_id)
    if request.method == 'POST':
        forms = BlogForms(request.POST,instance=blog_edit)
        forms.save()
        return redirect('home')
    
    forms = BlogForms(instance=blog_edit)
    return render(request,'new.html',{'forms':forms})

def delete(request,blog_id):
        blog_delete = get_object_or_404(Blog,id = blog_id)
        blog_delete.delete()

        return redirect('home')


