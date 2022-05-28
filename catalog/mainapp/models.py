# from django.db import models
#
# # Create your models here.
#
#

# class Catalog(models.Model):
#     title = models.CharField(max_length=64, unique=True, null=False)
#
#
# class Product(models.Model):
#
#     class UnitOfMeasure(models.TextChoices):
#         one_piece = '1', 'шт.'
#         one_kilogram = '2', 'кг.'
#         one_pack = '3', 'упаковка'
#
#     name = models.CharField(verbose_name='наименование товара', max_length=64, unique=True)
#     catalog = models.ManyToManyField(Catalog, on_delete=models.CASCADE)
#     price = models.FloatField(verbose_name='стоимость единицы товара')
#     unit_of_measure = models. CharField(max_length=10,
#                                         choices=UnitOfMeasure.choices,
#                                         default=UnitOfMeasure.one_piece)
#     quantity = models.PositiveIntegerField(default=0, null=False)
#     date_of_receipt = models.DateTimeField(verbose_name='Дата поступления', null=False, auto_now_add=True)
#     is_active = models.BooleanField(verbose_name='статус товара в БД', default=True)
#     supplier = models.CharField(verbose_name='поставщик товара', max_length=64, null=False)
#     add_date = models.DateTimeField(verbose_name='дата добавления', auto_now_add=True)
#     modified_date = models.DateTimeField(verbose_name='Дата изменения', auto_now=True)
#
#

