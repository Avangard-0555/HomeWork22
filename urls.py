from django.urls import path
from . import views

urlpatterns = [
    # Страница с новостями
    path('news/', views.news_list, name='news_list'),
]
