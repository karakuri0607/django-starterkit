from django.urls import path
from . import views

app_name = 'app'
urlpatterns = [
    path('list/', views.ListView.as_view(), name='list'),
    path('detail/<int:id>/', views.DetailView.as_view(), name='detail'),
    path('contact/', views.ContactFormView.as_view(), name='contact_form'),
    path('contact/result/', views.ContactResultView.as_view(), name='contact_result'),
]