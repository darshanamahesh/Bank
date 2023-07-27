from . import views
from  django.urls import  path

urlpatterns = [

    path('register', views.register, name='register'),
    path('login',views.login,name='login'),
    path('', views.home, name='home'),
    path('district/<int:district_id>/', views.district_wikipedia, name='district_wikipedia'),
    path('customer_form/', views.customer_form, name='customer_form'),
    path('application_accepted/', views.application_accepted, name='application_accepted'),
    path('logout', views.logout, name='logout'),
]