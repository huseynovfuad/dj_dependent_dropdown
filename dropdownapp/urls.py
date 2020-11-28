from django.urls import path
from . import views


urlpatterns = [
    path('',views.create_travel,name='create-travel'),
    path('update/<travel_id>/',views.update_travel,name='update-travel'),
    path('ajax/upload/cities/',views.upload_cities,name='upload-cities')
]