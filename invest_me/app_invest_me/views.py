from django.shortcuts import render,HttpResponse, redirect
from .models import Investment
from .forms import InvestmentForm
from django.contrib.auth.decorators import login_required

def investments(request):
    data = {
        'data': Investment.objects.all()
    }
    return render(request, 'investments/investment.html', context=data)

def details(request,investment):
    data = {
        'data': Investment.objects.get(pk=investment)    
    }
    return render(request,'investments/details.html', data)

@login_required
def create(request):
    if request.method == 'POST':
        investment_form = InvestmentForm(request.POST)
        if investment_form.is_valid():
            investment_form.save()
        return redirect('investments')    
    else:    
        investment_form = InvestmentForm()
        form = {
            'form': investment_form
        }
        return render(request,'investments/new_investment.html', context=form)

@login_required
def edit(request, investment):
   investment = Investment.objects.get(pk=investment)
   if request.method == 'GET':
    form = InvestmentForm(instance=investment)
    return render(request,'investments/new_investment.html', {'form': form})        
   else:
    form = InvestmentForm(request.POST, instance=investment) 
    if form.is_valid():
        form.save()
    return redirect('investments')    

@login_required
def delete(request,investment):
    investment = Investment.objects.get(pk=investment)
    if request.method == 'POST':
        investment.delete()
        return redirect('investments')
    return render(request, 'investments/confirm_deletion.html', {'item': investment})    