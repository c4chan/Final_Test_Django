from django.urls import path
from .views import logout
from .views import logout_view
from . import views

urlpatterns = [
    path("<int:id>", views.index, name="index"),
    path("", views.home, name="home"),
    path("create/", views.create, name="create"),
    path("view/", views.view, name="view"),
    path('logout/', views.logout, name='logout'),
    path('logout/', views.logout_view, name='logout'),
]