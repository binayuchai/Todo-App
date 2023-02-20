from django.shortcuts import render, redirect, get_object_or_404
from todo_app.models import TODO
from todo_app.forms import TODOForm, UserRegisterForm
from django.http import HttpResponseRedirect, JsonResponse, HttpResponseBadRequest
from django.urls import reverse
import json
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user


@unauthenticated_user
def login_view(request):

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(username)
        print(password)
       
        valid_user = authenticate(username = username,password = password)
            

        if valid_user is not None:
            
            login(request,valid_user)
            messages.success(request,"Welcome" + username)

            return redirect("todo:home")
        else:
            messages.error(request,"Invalid email or password")
            return redirect("login.html")
    return render(request,"login.html")

@unauthenticated_user
def register_view(request):
    form = UserRegisterForm(request.POST or None)
    if request.method == "POST":

        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password1']

        print(username)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, 'Registered successfully. Please login in!')
            return redirect("todo:register")
    return render(request,"register.html",{"form":form})

def logout_view(request):
    logout(request)
    print("Logout")
    return redirect("todo:home")

def home(request):
    Task = TODO.objects.all()
    form = TODOForm()
    context = {"Task":Task, "form":form}  
    return render(request,"home.html",context)


@login_required(login_url='login')
def todo_add(request):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    if is_ajax:
        if request.method == 'POST':
            data = json.load(request)
            print(data)
            todo = data.get('payload')
            print(todo)
            TODO.objects.create(title=todo['title'],user=request.user)
            return JsonResponse({'status':'Task Added'})
        return JsonResponse({'status':'Invalid Request'},status=400)
    else:
        return HttpResponseBadRequest('Invalid Request')
            
@login_required(login_url='login')
def todo_show(request):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    if is_ajax:
        if request.method == 'GET':
            todos = list(TODO.objects.filter(user=request.user).values())
            return JsonResponse({'context':todos})
        return JsonResponse({'status':'Invalid Request'}, status=400)
    else:
        return HttpResponseBadRequest('INvalid request')
        

# def todo_update_view(request):       
#     taskid = request.POST.get("todoitem")
#     task = get_object_or_404(, id=taskid)

#     form = TODOForm(request.POST or None, instance=task)
#     if form.is_valid():
#         form.save()
#         return HttpResponseRedirect(reverse("todo:home"))
        
#     return render(request,"home.html",{"form":form})
@login_required(login_url='login')
def todo_update_view(request):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    if is_ajax:
        if request.method == "PUT":
            data = json.load(request)
            print(data)
            todo = data.get('payload')
            print(todo)
            task = get_object_or_404(TODO, id=todo['id'],user=request.user)
            print(task)
            task.title = todo['title']
            task.save()   
            return JsonResponse({'status':'TOdo Updated'})
            
        return JsonResponse({"status":"Invalid request"},status=400)
                                
    else:
        return HttpResponseBadRequest('Invalid Request')
    
            
            
            
        
    

# def todo_delete_view(request):
            
#     taskId = request.POST.get("_delitem")
#     task = get_object_or_404(, id=taskId)
#     task.delete()
    
#     return HttpResponseRedirect(reverse("todo:home"))
    
@login_required(login_url='login')
def todo_delete_view(request):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    if is_ajax:
        if request.method == "DELETE":
            data = json.load(request)
            print(data)
            todo = data.get('payload')
            print(todo)
            task = get_object_or_404(TODO, id=todo['id'],user=request.user)
            print(task)
            task.delete()
            return JsonResponse({"status":'TODO Deleted'})
        return JsonResponse({"status":"Invalid request"},status=400)
    else:
        return HttpResponseBadRequest('Invalid Request')
    
            

            
            
            
        
            
        
        