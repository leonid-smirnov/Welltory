# Generated by Django 3.2.8 on 2022-01-11 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('welltory_test', '0005_alter_data_from_users_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data_from_users',
            name='date',
            field=models.DateTimeField(default='', verbose_name='Дата создания'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='data_from_users',
            name='pulse',
            field=models.FloatField(blank=True, null=True, verbose_name='Пульс'),
        ),
        migrations.AlterField(
            model_name='data_from_users',
            name='steps',
            field=models.FloatField(blank=True, null=True, verbose_name='Количество шагов'),
        ),
        migrations.AlterField(
            model_name='data_from_users',
            name='temperature',
            field=models.FloatField(blank=True, null=True, verbose_name='Температура'),
        ),
    ]