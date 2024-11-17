from django.contrib import admin
from .models import NewsCategory, News

# Регистрируем модель категории новостей в админке
admin.site.register(NewsCategory)

# Регистрируем модель новостей в админке
admin.site.register(News)
