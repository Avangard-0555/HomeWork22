from django.db import models

# Модель для категорий новостей
class NewsCategory(models.Model):
    # Название категории
    name = models.CharField(max_length=100)
    # Дата создания категории (автоматически устанавливается при добавлении)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # Это метод отображения категории в админке
        return self.name


# Модель для новостей
class News(models.Model):
    # Заголовок новости
    title = models.CharField(max_length=200)
    # Основной текст новости
    content = models.TextField()
    # Связь с категорией (одна новость относится к одной категории)
    category = models.ForeignKey(NewsCategory, on_delete=models.CASCADE)
    # Дата создания новости (автоматически при добавлении)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # Это метод отображения новости в админке
        return self.title
