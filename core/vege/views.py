from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Receipe
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def receipies(request):
    if request.method == 'POST':
        recipe_name = request.POST.get('recipe_name')
        recipe_description = request.POST.get('recipe_description')
        recipe_image = request.FILES.get('recipe_image')

        # Debugging output to check the contents of the request
        print("POST data:", request.POST)
        print("FILES data:", request.FILES)

        # Ensure that the file is being processed correctly
        if recipe_image:
            Receipe.objects.create(
                recipe_name=recipe_name,
                recipe_description=recipe_description,
                recipe_image=recipe_image
            )
            return redirect('/receipes')
    queryset = Receipe.objects.all()
    context = {'receipes': queryset}
    return render(request, 'receipies.html', context)

def delete_receipe(request, id):
    queryset = Receipe.objects.get(id=id)
    queryset.delete()
    return redirect('/receipes')

def update_receipe(request, id):
    queryset = get_object_or_404(Receipe, id=id)
    if request.method == 'POST':
        recipe_name = request.POST.get('recipe_name')
        recipe_description = request.POST.get('recipe_description')
        recipe_image = request.FILES.get('recipe_image')

        # Update the queryset object with the new data
        queryset.recipe_name = recipe_name
        queryset.recipe_description = recipe_description
        if recipe_image:
            queryset.recipe_image = recipe_image
        queryset.save()

        return redirect('/receipes')
    if request.GET.get('search'):
        Receipe.objects.filter(recipe_name__icontains=request.GET.get('search'))


    context = {'receipe': queryset}
    return render(request, 'update_receipe.html', context)

def register_page(request) :
    if request.method =="POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('Username')
        password = request.POST.get('password')

        user = User.objects.filter(username = username)
        if user.exists():
            messages.info(request, "Username already exists")
            return redirect('/register')
        

        user = User.objects.create(
            first_name=first_name,
            last_name = last_name,
            username = username

        )
        user.set_password(password)
        user.save()
        messages.info(request, "account created successfully")

        return redirect('register')


    return render(request , 'register.html')

def login_page(request) :
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username = username).exists():
            messages.error(request,'Invalid Username')
            return redirect('/login')
        
        user = authenticate(username= username,password=password)
        if user is None:
            messages.error(request,'Invalid password')
            return redirect('/login')
        else:
            login(request,user)
            return redirect('receipies')



    return render(request , 'login.html')

def logout_page(request):
    logout(request)
    return redirect('/login')
