from django.db import models

from core.models import PublishedModel


class Category(PublishedModel):
    title = models.CharField(verbose_name='Название', max_length=256)
    slug = models.SlugField(verbose_name='Слаг', max_length=64, unique=True)
    output_order = models.PositiveSmallIntegerField(
        verbose_name='Порядок отображения',
        default=100
        )

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class Topping(PublishedModel):
    title = models.CharField(verbose_name='Название', max_length=256)
    slug = models.SlugField(verbose_name='Слаг', max_length=64, unique=True)

    class Meta:
        verbose_name = 'топпинг'
        verbose_name_plural = 'топпинги'

    def __str__(self):
        return self.title


class Wrapper(PublishedModel):
    title = models.CharField(
        verbose_name='Название',
        max_length=256,
        help_text='Уникальное название обёртки, не более 256 символов')

    class Meta:
        verbose_name = 'обёртка'
        verbose_name_plural = 'обёртки'

    def __str__(self):
        return self.title


class IceCream(PublishedModel):
    title = models.CharField(verbose_name='Название', max_length=256)
    description = models.TextField(verbose_name='Описание')
    wrapper = models.OneToOneField(
        Wrapper,
        verbose_name='обёртка',
        on_delete=models.SET_NULL,
        related_name='ice_cream',
        null=True,
        blank=True,
    )
    category = models.ForeignKey(
        Category,
        verbose_name='категория',
        on_delete=models.CASCADE,
        related_name='ice_creams',
    )
    toppings = models.ManyToManyField(Topping, verbose_name='топпинги')
    is_on_main = models.BooleanField(verbose_name='На главную', default=False)

    class Meta:
        verbose_name = 'мороженое'
        verbose_name_plural = 'мороженое'

    def __str__(self):
        return self.title

