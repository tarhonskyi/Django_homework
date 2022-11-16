from django.db import models


class Film(models.Model):
    title = models.CharField(max_length=50)
    producer = models.CharField(max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Фільм'
        verbose_name_plural = 'Фільми'
        ordering = ('title',)


class Actor(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    oskars = models.PositiveIntegerField(default=0)
    films = models.ManyToManyField(Film, null=True)

    def __str__(self):
        return f'{self.name} {self.surname}'

    class Meta:
        verbose_name = 'Актор'
        verbose_name_plural = 'Актори'
        ordering = ('name',)
