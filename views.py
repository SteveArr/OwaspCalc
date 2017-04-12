import string
from django.views.generic import *
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.utils.text import slugify
from django.utils.crypto import get_random_string
from owaspcalc.models import *
from owaspcalc.forms import *


class RiskAuditCreate(CreateView):
    model = RiskAudit
    fields = ['title', 'details', 'skill_level','motivation','opportunity','size','slug']

class RiskAuditUpdate(UpdateView):
    model = RiskAudit
    fields = ['title', 'details', 'skill_level','motivation','opportunity','size','slug']
    template_name_suffix = '_update_form'

class RiskAuditDelete(DeleteView):
    model = RiskAudit
    success_url = reverse_lazy('owaspcalc:index')

def index(request):
    return HttpResponse("Hello, world.")

def create(request):
    if request.method == "POST":
        form = RiskAuditCreateForm(request.POST)
        if form.is_valid():
                post = form.save(commit=False)
                post.slug = slugify(get_random_string(5, string.ascii_uppercase+string.digits))
                post.save()
                return redirect('owaspcalc:index')
    else:
        form = RiskAuditCreateForm()
    
    return render(request, 'owaspcalc/create.html', {'form': form})

def edit(request, slug):
    risk = get_object_or_404(RiskAudit, slug=slug)
    form = RiskAuditEditForm(request.POST or None, instance=risk)
    if form.is_valid():
            #If user changes slug, the slug parameter is the old one.
            #Thus, we need to get the slug from the edit form so when
            #we redirect on success, we redirect to new slug.
            post = form.save(commit=False)
            slug = post.slug
            form.save()
            return redirect('owaspcalc:detail', slug)
    
    return render(request, 'owaspcalc/edit.html', {'form': form}) 

def detail(request, slug):
    risk = get_object_or_404(RiskAudit, slug=slug)
    return render(request, 'owaspcalc/detail.html', {'ra': risk})

def list(request):
    risks = RiskAudit.objects.all()
    return render(request, 'owaspcalc/list.html', {'risks': risks})