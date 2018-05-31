from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Militar
from .forms import MilitarForm

# Create your views here.

@login_required()
def index(request):
	return render(request, 'index.html')

@login_required()
def militar_list(request):
	militares = Militar.objects.all()
	return render(request, 'militares.html',{'militares':militares})

@login_required()
def militar_new(request):
    form = MilitarForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('militar_list')
    return render(request, 'militar_form.html', {'form':form})

@login_required()
def militar_update(request, id):
    militar = get_object_or_404(Militar, pk=id)
    form = MilitarForm(request.POST or None, request.FILES or None, instance=militar)
    if form.is_valid():
        form.save()
        return redirect('militar_list')
    return render(request, 'militar_form.html', {'form':form})

@login_required()
def militar_delete(request, id):
    militar = get_object_or_404(Militar, pk=id)
    form = MilitarForm(request.POST or None, request.FILES or None, instance=militar)
    if request.method == 'POST':
        militar.delete()
        return redirect('militar_list')
    return render(request, 'militar_delete_confirm.html', {'militar':militar})