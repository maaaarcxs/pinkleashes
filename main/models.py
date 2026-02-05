from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from phonenumber_field.modelfields import PhoneNumberField
from django_resized import ResizedImageField


class ServiceType(models.Model):
    title = models.CharField(verbose_name="Название", max_length=85)
    price = models.IntegerField(verbose_name="Стоимость")

    def __str__(self):
        return f'{self.title} {self.price} сом'
    
    class Meta:
        verbose_name = "Тип услуги"
        verbose_name_plural = "Типы услуг"


class Service(models.Model):
    image = ResizedImageField(size=[800, 600], crop=['middle', 'center'], upload_to='gallery/',
                            verbose_name='Фото', null=True, blank=True, quality=90)
    title = models.CharField(verbose_name="Название", max_length=80)
    types = models.ForeignKey(ServiceType, verbose_name="тип услуги", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}'
    
    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"


class SocialMedia(models.Model):
    name = models.CharField(verbose_name="Название", max_length=70)
    
    class Meta:
        verbose_name = "Социальная сеть"
        verbose_name_plural = "Социальные сети"


class Master(models.Model):
    POSITIONS=(
        ("Master", "Мастер"),
        ("Apprentice", "Стажёр")
    )
    photo = ResizedImageField(size=[800, 600], crop=['middle', 'center'], upload_to='gallery/',
                              verbose_name='Фото', null=True, blank=True, quality=90)
    name = models.CharField(verbose_name="Имя", max_length=50)
    position = models.CharField(verbose_name="Должность", choices=POSITIONS, max_length=20)
    experience = models.IntegerField(verbose_name="Опыт (лет)")
    description = models.TextField(verbose_name="Описание", max_length=1200)
    services = models.ManyToManyField(Service, verbose_name="Услуги", related_name="masters")
    media = models.ForeignKey(SocialMedia, verbose_name="Соц сети", related_name="smedia", on_delete=models.CASCADE)
    link = models.URLField(verbose_name="ссылка")

    def __str__(self):
        return f'{self.name}, {self.position}, {self.experience}'
    
    class Meta:
        verbose_name = "Мастер"
        verbose_name_plural = "Мастера"

    
class Gallery(models.Model):
    image = ResizedImageField(size=[800, 600], crop=['middle', 'center'], upload_to='gallery/',
                              verbose_name='Фото', null=True, blank=True, quality=90)
    title = models.CharField(verbose_name="Название", max_length=60)
    service = models.ForeignKey(Service, verbose_name="Работы", related_name="works", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} {self.service}'
    
    class Meta:
        verbose_name = "Галерея работы"
        verbose_name_plural = "Галерея работ"


class Review(models.Model):
    master = models.ForeignKey(Master, verbose_name="Отзывы по мастеру", related_name="comments", on_delete=models.CASCADE)
    rating = models.IntegerField(verbose_name="Оценка", validators=[MinValueValidator(1),
                    MaxValueValidator(5)], help_text="Введите оценку от одного до пяти")
    comment = models.TextField(verbose_name="Комментарий", max_length=1200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.comment:
            has_comment = self.comment
        else:
            has_comment = "Комментарий отсутствует"
        return f'Отзыв по мастеру{self.master.name}: оценка {self.rating}/5, {has_comment}'
    
    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"


class Appointment(models.Model):
    customer_name = models.CharField(verbose_name="Введите имя", max_length=50)
    phone_number = PhoneNumberField(verbose_name="Номер телефона")
    service = models.ForeignKey(Service, verbose_name="Выберите услугу", on_delete=models.CASCADE)
    master = models.ForeignKey(Master, verbose_name="Выберите мастера", on_delete=models.CASCADE)
    date = models.DateField(verbose_name="Выберите даты", auto_now_add=False, auto_now=False)
    time = models.TimeField(verbose_name="Выберите время")
    comment = models.TextField(verbose_name="Оставьте комментарий", max_length=1000)

    def __str__(self):
        return f'{self.customer_name} на запись к {self.master.name}'
    
    class Meta:
        verbose_name = "Запись"
        verbose_name_plural = "Записи"