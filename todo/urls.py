from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('team/', views.team, name='team'),
    path('todo/', views.todo, name='todo'),
    path('contact/', views.contactus, name='contactus'),
    # path('login/', views.account, name='account'),
    path('account/', views.account, name='account'),
    path('signup/', views.signup, name='signup'),
    path('add-todo/', views.add_todo, name='add_todo'),
    path('logout/', views.signout, name='signout'),
    path('forgetpassword/', views.forgetpassword, name='forgetpassword'),
    path('deletetodo/<int:id>/', views.deletetodo, name='deletetodo'),
    path('edittodo/<int:id>/', views.edittodo, name='edittodo'),
    path('updatetodo/<int:id>/', views.updatetodo, name='updatetodo'),
    path('profile/', views.profile, name='profile'),
    path('updateprofile/', views.updateprofile, name='updateprofile'),
    path('search/', views.search, name='search'),
]
