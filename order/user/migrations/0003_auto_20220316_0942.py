# Generated by Django 3.1.3 on 2022-03-16 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20220315_0815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_data',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date order'),
        ),
    ]