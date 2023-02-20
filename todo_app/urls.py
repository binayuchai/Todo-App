from django.urls import path
from todo_app.views import home, todo_update_view, todo_show, todo_add, todo_delete_view, register_view, login_view, logout_view

app_name = "todo"

urlpatterns = [
    path("",home,name="home"),
    path("todo-add/",todo_add,name="todo_add"),
    path('todo-show/',todo_show,name="todo_show"),
    path("todo-update/",todo_update_view, name="todo_update_view"),
    path("todo-delete/",todo_delete_view, name="todo_delete_view"),
    path("login/",login_view,name="login"),
    path("register/",register_view,name="register"),
    path("logout/",logout_view,name="logout"),

    

]
