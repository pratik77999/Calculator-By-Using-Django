from django.shortcuts import render,redirect
from .forms import CalculatorForm
# Create your views here.

def CalculatorView(request):
    form=CalculatorForm()
    state=False
    result=0
    if request.method=='POST':
        form=CalculatorForm(request.POST)
        if form.is_valid():
            state=True
            try:
                result=eval((form.cleaned_data['value']))    
            except SyntaxError:
                result='You can not provide string value'
            except NameError:
                result='You can not provide string value'
                
    return render(request,'newapp/index.html',{'form':form,'state':state,'result':result})

