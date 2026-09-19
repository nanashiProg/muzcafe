from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError

class MenuDish(models.Model):

    # Задаем варианты: (значение_в_бд, отображаемое_имя_для_админа)
    STATUS_CHOICES = [
        ('hot', 'Горячее'),
        ('cold', 'Холодное'),
        ('drinks', 'Напитки'),
    ]

    category = models.CharField(max_length=200, verbose_name="Категория", choices=STATUS_CHOICES)
    menu_photo = models.ImageField(upload_to='menu/%Y/%m/%d/', verbose_name="Фото для позиции в меню", null=True, blank=True)
    menu_title = models.CharField(max_length=200, verbose_name="Название позиции в меню")
    description = models.TextField(blank=True, verbose_name="Описание")
    price = models.DecimalField(
        max_digits=10,
        decimal_places=0,
        default=0,
        verbose_name="Цена"
    )
    # Цена в целых числах (только положительные значения)
    count = models.PositiveIntegerField(
        default=0,
        verbose_name="Кол-во (шт)"
    )

    def __str__(self):
        return f'{self.category} {self.menu_photo} {self.menu_title} {self.description} {self.price} {self.count}'

    class Meta:
        verbose_name = "Позиция"
        verbose_name_plural = "Позиции"