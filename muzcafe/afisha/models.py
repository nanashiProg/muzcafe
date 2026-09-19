from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError

class Posters(models.Model):
    photo = models.ImageField(upload_to='afisha/%Y/%m/%d/', verbose_name="Фото для афишы")
    date = models.DateTimeField(verbose_name="Дата и время публикации")
    is_free = models.BooleanField(default=False, verbose_name="Вход свободный?")
    # Дополнительное поле (обязательно blank=True)
    price = models.CharField(blank=True, null=True, verbose_name="Стоимость за вход")

    def clean(self):
        super().clean()
        # Если галочка СНЯТА (False), а поле причины пустое — выводим ошибку
        if not self.is_free and not self.price:
            raise ValidationError({
                'dismissal_reason': 'Вы обязаны указать цену, если вход не свободный!'
            })

    def save(self, *args, **kwargs):
        # Если галочка стоит (сотрудник активен), автоматически пишем нужный текст
        if self.is_free:
            self.price = "Вход свободный"
            # Либо можно очищать поле: self.dismissal_reason = None
        super().save(*args, **kwargs)

    title = models.CharField()
    description = models.TextField(verbose_name="Описание события")

    def __str__(self):
        return f'{self.photo} {self.date} {self.is_free} {self.price} {self.title} {self.price}'

    class Meta:
        verbose_name = 'Афиша'
        verbose_name_plural = 'Афишы'
