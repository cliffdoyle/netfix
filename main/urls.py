from django.urls import path
from . import views as v

app_name = "main"

urlpatterns = [
    path('', v.home, name='home'),
    path('logout/', v.logout, name='logout'),
    # path('most_requested/', v.most_requested_services, name='most_requested_services'),
    path('services/<str:field>/', v.services_by_category, name='services_by_category'),

]
