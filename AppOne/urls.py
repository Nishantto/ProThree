from AppOne import views
from django.urls import path
urlpatterns = [
    path('index/', views.index,name="app1_index"),
    path('login/', views.login)



]