# Generated by Django 3.2.16 on 2022-12-15 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equivalencias', '0004_auto_20221212_0826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entidad',
            name='codigo',
            field=models.CharField(blank=True, default=None, max_length=5, null=True, unique=True, verbose_name='Código'),
        ),
    ]
