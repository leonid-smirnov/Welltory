# Generated by Django 3.2.8 on 2022-01-17 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('welltory_test', '0009_alter_data_from_users_pearson_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='data_from_users',
            name='title',
            field=models.CharField(blank=True, max_length=20, verbose_name='Название'),
        ),
    ]