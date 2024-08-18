from django.urls import path
from .views import GenerateCSVView, index

urlpatterns = [
    path('', index, name='index'),
    path('api/generate/', GenerateCSVView.as_view(), name='generate_csv'),
]
