from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('erstellen/', views.create, name='create'),
    path('bearbeiten/<str:movie_id>', views.edit, name='edit'),
    path('löschen/<str:movie_id>', views.delete, name='delete')
]
