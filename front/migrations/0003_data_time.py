# Generated by Django 3.2.9 on 2023-01-31 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0002_alter_data_population'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='time',
            field=models.TimeField(auto_now_add=True, null=True),
        ),
    ]
