# Generated by Django 3.2.9 on 2023-01-16 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='humidity',
            field=models.PositiveBigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='precipitation',
            field=models.PositiveBigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='rainfall',
            field=models.PositiveBigIntegerField(null=True),
        ),
    ]