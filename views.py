from django.shortcuts import render
from .models import News

# Представление для отображения списка новостей
def news_list(request):
    # Получаем все новости из базы данных
    news = News.objects.all()
    # Отправляем новости в шаблон для отображения
    return render(request, 'news_list.html', {'news': news})
