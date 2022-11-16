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
    films = models.ManyToManyField(Film)

    def __str__(self):
        return f'{self.name} {self.surname}'

    class Meta:
        verbose_name = 'Актор'
        verbose_name_plural = 'Актори'
        ordering = ('name',)


class Author(models.Model):
    name = models.CharField(max_length=50, verbose_name="Ім'я автора")
    second_name = models.CharField(max_length=50, verbose_name="По батькові автора", blank=True, default='')
    surname = models.CharField(max_length=50, verbose_name="Прізвище автора")
    birth_date = models.DateField(auto_now=False, verbose_name='Дата народження')
    country = models.CharField(max_length=50, verbose_name='Країна походження')

    def __str__(self):
        return f"{self.name} {self.surname}"

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Автори'
        ordering = ('birth_date',)


class PublishingHouse(models.Model):
    name = models.CharField(max_length=50, verbose_name='Назва видавництва')
    country = models.CharField(max_length=50, verbose_name='Країна видавництва')
    motto = models.TextField(max_length=150, verbose_name='Гасло компанії', blank=True, default='')
    established = models.DateField(auto_now=False, verbose_name='Дата заснування')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Видавництво'
        verbose_name_plural = 'Видавництва'
        ordering = ('established',)


class Book(models.Model):
    GENRE_CHOICES = (
        ('фікшн', 'Фікшн'),
        ('роман', 'Роман'),
        ('комедія', 'Комедія'),
        ('новела', 'Новела'),
        ('проза', 'Проза'),
        ('поезія', 'Поезія'),
        ('історична література', 'Історична література'),
        ('автобіографія', 'Автобіографія'),
    )
    title = models.CharField(max_length=100, verbose_name='Назва книги')
    publication_date = models.DateField(auto_now=False, verbose_name='Дата публікації')
    genre = models.CharField(max_length=50, choices=GENRE_CHOICES, verbose_name='Жанр книги')
    author = models.ForeignKey(Author, verbose_name='Автор', on_delete=models.CASCADE)

    def __str__(self):
        return f'"{self.title}". {self.author}'

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        ordering = ('title',)


class BookInStore(models.Model):
    LANGUAGE_CHOICES = (
        ('UA', 'Українська'),
        ('EN', 'Англійська'),
        ('FR', 'Французька'),
        ('DE', 'Німецька'),
    )
    book = models.ForeignKey(Book, verbose_name='', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Ціна екземпляру')
    quantity = models.PositiveIntegerField(verbose_name='Кількість екземплярів')
    language = models.CharField(max_length=50, choices=LANGUAGE_CHOICES, verbose_name='Мова видання')
    publishing_house = models.ForeignKey(PublishingHouse, verbose_name='Видавництво', on_delete=models.CASCADE)
    number_of_pages = models.PositiveIntegerField(verbose_name='Кількість сторінок', blank=True, default=0)

    def __str__(self):
        return f"{self.book} x {self.quantity}"

    class Meta:
        verbose_name = "Екземпляри книги"
        verbose_name_plural = "Екземпляри книжок"
        ordering = ('quantity',)
