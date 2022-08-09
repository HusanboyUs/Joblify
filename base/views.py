from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .forms import UserResgistrationForm
from django.contrib.auth import authenticate,login,logout
from . models import Jobs


    
#hadnling user registration and user staff
def loginView(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
    context={}
    return render(request, 'main/login.html')        
    
def registerView(request):
    form=UserResgistrationForm()
    if request.method=='POST':
        form=UserResgistrationForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    context={'form':form}
    return render(request, 'main/register.html', context)

def logoutView(request):
    logout(request)
    return redirect('/')




#hadnling with user main pages such as Home and dahsboard staff

@login_required(login_url='login/')
def homeView(request, *args, **kwargs):
    jobs=request.user.Jobs.order_set.all()
    '''
    pending=
    scheduled=
    declined=
    '''
    return render(request, 'main/index.html')

def allJobsView(request):
    jobs=Jobs.objects.filter(user=request.user)
    context={'jobs':jobs}
    return render(request, 'main/jobs.html',context)   