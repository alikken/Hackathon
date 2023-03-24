from django.db import models

from auths.models import CustomUser

from django.core.validators import (
    MaxValueValidator,
    MinValueValidator,
)


class UserCall(models.Model):
    """Call model for Users."""

    caller = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        verbose_name='заказчик'
    )
    appartment = models.IntegerField(
        validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ]
    )
    problem = models.TextField(
        verbose_name='причина обращения'
    )

    class Meta:
        ordering = ('-datetime_created',)
        verbose_name = 'обращение'
        verbose_name_plural = 'обращения'


class AdminCall(models.Model):
    """Call model for Admin."""

    user_call = models.ForeignKey(
        UserCall,
        on_delete=models.CASCADE
    )
    service_type = models.ForeignKey(
        'Service',
        on_delete=models.CASCADE
    )

    class Meta:
        ordering = ('-datetime_created',)
        verbose_name = 'обращение'
        verbose_name_plural = 'обращения'


class Service(models.Model):
    """Service model."""

    name = models.CharField(
        max_length=255,
        unique=True,
        verbose_name='название услуги'
    )

    class Meta:
        ordering = ('-id',)
        verbose_name = 'услуга'
        verbose_name_plural = 'услуги'


class MasterUser(CustomUser):
    """MasterUser model."""

    service_master = models.ForeignKey(
        Service,
        on_delete=models.CASCADE
    )

    class Meta:
        ordering = ('-datetime_created',)
        verbose_name = 'мастер'
        verbose_name_plural = 'мастера'

    
