from django.conf import settings
from django.db import models


class Doctor(models.Model):
    full_name = models.CharField(max_length=255, verbose_name='ФИО')
    specialization = models.CharField(max_length=255, verbose_name='Специализация')
    experience = models.PositiveIntegerField(verbose_name='Стаж работы (лет)')
    description = models.TextField(verbose_name='Описание')
    photo = models.ImageField(
        upload_to='doctors/',
        blank=True,
        null=True,
        verbose_name='Фото'
    )
    is_active = models.BooleanField(default=True, verbose_name='Активен')

    class Meta:
        verbose_name = 'Врач'
        verbose_name_plural = 'Врачи'
        ordering = ['full_name']

    def __str__(self):
        return f'{self.full_name} - {self.specialization}'


class Appointment(models.Model):
    STATUS_CHOICES = (
        ('new', 'Новая'),
        ('confirmed', 'Подтверждена'),
        ('completed', 'Завершена'),
        ('canceled', 'Отменена'),
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='appointments',
        verbose_name='Пользователь'
    )
    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.CASCADE,
        related_name='appointments',
        verbose_name='Врач'
    )
    service = models.ForeignKey(
        'services.Service',
        on_delete=models.CASCADE,
        related_name='appointments',
        verbose_name='Услуга'
    )
    appointment_date = models.DateField(verbose_name='Дата приёма')
    appointment_time = models.TimeField(verbose_name='Время приёма')
    comment = models.TextField(
        blank=True,
        verbose_name='Комментарий'
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='new',
        verbose_name='Статус'
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')

    class Meta:
        verbose_name = 'Запись на приём'
        verbose_name_plural = 'Записи на приём'
        ordering = ['-appointment_date', '-appointment_time']

    def __str__(self):
        return (
            f'{self.user.username} - {self.service.title} - '
            f'{self.appointment_date} {self.appointment_time}'
        )