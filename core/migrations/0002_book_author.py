# Generated by Django 4.0.3 on 2022-03-12 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.CharField(max_length=100, null=True, verbose_name='Имя автора'),
        ),
    ]