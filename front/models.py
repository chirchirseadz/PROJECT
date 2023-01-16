from django.db import models

# Create your models here.

class Data(models.Model):
    COUNTY = (
       ('Nairobi City','Nairobi City'),
            ('Mombasa', 'Mombasa'),
            ('Kwale', 'Kwale'),
            ('Kilifi', 'Kilifi'),
            ('Tana River', 'Tana River'),
            ('Lamu','Lamu'),
            ('Taita-Taveta','Taita-Taveta'),
            ('Garissa','Garissa'),
            ('wajir','wajir'),
            ('Mandera','Mandera'),
            ('Marsabit', 'Marsabit'),
            ('Isiolo','Isiolo'),
            ('Meru','Meru'),
            ('Tharaka-Nithi','Tharaka-Nithi'),
            ('Embu','Embu'),
            ('Kitui','Kitui'),
            ('Machakos','Machakos'),
            ('Makueni','Makueni'),
            ('Nyandarua','Nyandarua'),
            ('Nyeri','Nyeri'),
            ('Kirinyaga','Kirinyaga'),
            ("Murang'a", "Murang'a"),
            ('Kiambu','Kiambu'),
            ('Turkana','Turkana'),
            ('West Pokot','West Pokot'),
            ('Samburu','Samburu'),
            ('Trans Nzoia','Trans Nzoia'),
            ('Uasin Gishu','Uasin Gishu'),
            ('Elgeyo-Marakwet','Elgeyo-Marakwet'),
            ('Nandi','Nandi'),
            ('Baringo','Baringo'),
            ('Laikipia','Laikipia'),
            ('Nakuru','Nakuru'),
            ('Narok','Narok'),
            ('Kajiado','Kajiado'),
            ('Kericho','Kericho'),
            ('Bomet','Bomet'),
            ('Kakamega','Kakamega'),
            ('Vihiga','Vihiga'),
            ('Bungoma','Bungoma'),
            ('Busia','Busia'),
            ('Siaya','Siaya'),
            ('Kisumu','Kisumu'),
            ('Homa Bay','Homa Bay'),
            ('Migori','Migori'),
            ('Kisii','Migori'),
            ('Nyamira','Nyamira'),
            

        
    )
    county = models.CharField(max_length=100, choices=COUNTY, null=True)
    population = models.PositiveBigIntegerField(null=True, default=1)
    max_temp = models.IntegerField(null=True)
    min_temp = models.IntegerField(null=True)
    humidity = models.PositiveBigIntegerField(null=True)
    rainfall = models.PositiveBigIntegerField(null=True)
    precipitation = models.PositiveBigIntegerField(null=True)
    fishing = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.county} details'

   