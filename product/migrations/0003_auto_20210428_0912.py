# Generated by Django 3.2 on 2021-04-28 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='height',
            field=models.IntegerField(null=True, verbose_name='Высота, в сантиметрах'),
        ),
        migrations.AddField(
            model_name='product',
            name='length',
            field=models.IntegerField(null=True, verbose_name='Длина, в сантиметрах'),
        ),
        migrations.AddField(
            model_name='product',
            name='weight',
            field=models.IntegerField(null=True, verbose_name='Вес, в граммах'),
        ),
        migrations.AddField(
            model_name='product',
            name='width',
            field=models.IntegerField(null=True, verbose_name='Ширина, в сантиметрах'),
        ),
    ]
