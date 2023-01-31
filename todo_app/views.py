from django.shortcuts import render, redirect, get_object_or_404
from todo_app.models import TODO
from todo_app.forms import TODOForm
from django.http import HttpResponseRedirect, JsonResponse, HttpResponseBadRequest
from django.urls import reverse
import json

# Create your views here.
# def home(request):
#     Task = #.objects.all()
#     if request.method == "POST":
#         form = TODOForm(request.POST)
        
#         if form.is_valid():
#             form.save()
#             return redirect("/")
#     else:
#         form = TODOForm()    
#     context = {"Task":Task, "form":form}    
#     return render(request,"home.html", context)

def home(request):
    Task = TODO.objects.all()
    form = TODOForm()
    context = {"Task":Task, "form":form}  
    return render(request,"home.html",context)

def todo_add(request):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    if is_ajax:
        if request.method == 'POST':
            data = json.load(request)
            print(data)
            todo = data.get('payload')
            print(todo)
            TODO.objects.create(title=todo['title'])
            return JsonResponse({'status':'Task Added'})
        return JsonResponse({'status':'Invalid Request'},status=400)
    else:
        return HttpResponseBadRequest('Invalid Request')
            

def todo_show(request):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    if is_ajax:
        if request.method == 'GET':
            todos = list(TODO.objects.all().values())
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

def todo_update_view(request):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    if is_ajax:
        if request.method == "PUT":
            data = json.load(request)
            print(data)
            todo = data.get('payload')
            print(todo)
            task = get_object_or_404(TODO, id=todo['id'])
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
    

def todo_delete_view(request):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    if is_ajax:
        if request.method == "DELETE":
            data = json.load(request)
            print(data)
            todo = data.get('payload')
            print(todo)
            task = get_object_or_404(TODO, id=todo['id'])
            print(task)
            task.delete()
            return JsonResponse({"status":'TODO Deleted'})
        return JsonResponse({"status":"Invalid request"},status=400)
    else:
        return HttpResponseBadRequest('Invalid Request')
    
            

            
            
            
        
            
        
        