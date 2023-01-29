# Generated by Django 3.2.9 on 2023-01-27 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0008_auto_20230127_0939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='county',
            field=models.CharField(choices=[(1, 'Mombasa'), (2, 'Kwale'), (3, 'Kilifi'), (4, 'Tana River'), (5, 'Lamu'), (6, 'Taita-Taveta'), (7, 'Garissa'), (8, 'wajir'), (9, 'Mandera'), (9, 'Marsabit'), (10, 'Isiolo'), (11, 'Meru'), (12, 'Tharaka-Nithi'), (13, 'Embu'), (14, 'Kitui'), (15, 'Machakos'), (16, 'Makueni'), (17, 'Nyandarua'), (18, 'Nyeri'), (19, 'Kirinyaga'), (20, "Murang'a"), (21, 'Kiambu'), (22, 'Turkana'), (23, 'West Pokot'), (24, 'Samburu'), (25, 'Trans Nzoia'), (26, 'Uasin Gishu'), (27, 'Elgeyo-Marakwet'), (28, 'Nandi'), (29, 'Baringo'), (30, 'Laikipia'), (31, 'Nakuru'), (32, 'Narok'), (33, 'Kajiado'), (34, 'Kericho'), (35, 'Bomet'), (36, 'Kakamega'), (37, 'Vihiga'), (38, 'Bungoma'), (39, 'Busia'), (40, 'Siaya'), (41, 'Kisumu'), (42, 'Homa Bay'), (43, 'Migori'), (44, 'Migori'), (45, 'Nyamira'), (46, 'Nairobi City')], max_length=100, null=True),
        ),
    ]
