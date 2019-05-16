from AppTwo import views
from django.urls import path

urlpatterns = [
    path('index/', views.index,name="app2_index"),
    path('login/', views.login)

]
