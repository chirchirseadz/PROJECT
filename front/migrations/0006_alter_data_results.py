# Generated by Django 3.2.9 on 2023-01-27 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0005_alter_data_fishing'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='results',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
