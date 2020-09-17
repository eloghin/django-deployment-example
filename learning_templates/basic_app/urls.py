from . import views
from django.urls import path

# TEMPLATE TAGGINIG: register a namespace
app_name = 'basic_app'

urlpatterns = [
    path('other/', views.other, name='other'),
    path('relative/', views.relative, name='relative'),
    ]
