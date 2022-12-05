from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Товар')
    image = models.ImageField(blank=True, upload_to='static/lesson_5/product/', verbose_name='Зображення')
    price = models.DecimalField(max_digits=8, decimal_places=2, blank=True, verbose_name='Ціна')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товари'


class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    text = models.TextField(max_length=255, verbose_name='Текст коментаря')

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Коментар'
        verbose_name_plural = 'Коментарі'
