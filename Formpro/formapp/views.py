from django.shortcuts import render
from .form import Registration
# Create your views here.
def first_View(request):
    form=Registration()
    submit=False
    names=''
    
    if request.method=='POST':
        form=Registration(request.POST)
        if form.is_valid():
            names=form.cleaned_data['name']
            age=form.cleaned_data['age']
            marks=form.cleaned_data['marks']
            feedback=form.cleaned_data['feedback']
            print(names,age,marks,feedback)
            submit=True
    
    return render(request,'testapp/index.html',{'data':form,'names':names,'submit':submit})
