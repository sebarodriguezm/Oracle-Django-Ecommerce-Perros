# Generated by Django 4.1.3 on 2023-02-26 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulo1', '0004_alter_marca_options_alter_producto_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='direccion',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
