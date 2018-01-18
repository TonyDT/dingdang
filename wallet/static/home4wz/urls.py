
from django.urls import path,include
from  wallet import views
urlpatterns = [
    path('cpjs/',views.cpjs),

]
