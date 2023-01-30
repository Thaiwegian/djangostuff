from django.urls import path

from .views import Address

app_name = 'columnsort'

urlpatterns = [
    path('', Address.as_view(), name='address_list'),
]
