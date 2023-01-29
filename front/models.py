from django.db import models
import joblib
from sklearn.preprocessing import StandardScaler
from sklearn import svm
# Create your models here.

class Data(models.Model):
    
    CHOICE = (
        (1, 'Yes'),
        (0, 'No'), 
    )
    COUNTY = (
            
            (1, 'Mombasa'),
            (2, 'Kwale'),
            (3, 'Kilifi'),
            (4, 'Tana River'),
            (5,'Lamu'),
            (6,'Taita-Taveta'),
            (7,'Garissa'),
            (8,'wajir'),
            (9,'Mandera'),
            (9, 'Marsabit'),
            (10,'Isiolo'),
            (11,'Meru'),
            (12,'Tharaka-Nithi'),
            (13,'Embu'),
            (14,'Kitui'),
            (15,'Machakos'),
            (16,'Makueni'),
            (17,'Nyandarua'),
            (18,'Nyeri'),
            (19,'Kirinyaga'),
            (20, "Murang'a"),
            (21,'Kiambu'),
            (22,'Turkana'),
            (23,'West Pokot'),
            (24,'Samburu'),
            (25,'Trans Nzoia'),
            (26,'Uasin Gishu'),
            (27,'Elgeyo-Marakwet'),
            (28,'Nandi'),
            (29,'Baringo'),
            (30,'Laikipia'),
            (31,'Nakuru'),
            (32,'Narok'),
            (33,'Kajiado'),
            (34,'Kericho'),
            (35,'Bomet'),
            (36,'Kakamega'),
            (37,'Vihiga'),
            (38,'Bungoma'),
            (39,'Busia'),
            (40,'Siaya'),
            (41,'Kisumu'),
            (42,'Homa Bay'),
            (43,'Migori'),
            (44,'Migori'),
            (45,'Nyamira'),
            (46,'Nairobi City'),
            
    )
    # county = models.IntegerField(choices=COUNTY, null=True)
    population = models.PositiveBigIntegerField(null=True, default=1)
    max_temp = models.IntegerField(null=True)
    min_temp = models.IntegerField(null=True)
    humidity = models.PositiveBigIntegerField(null=True)
    rainfall = models.PositiveBigIntegerField(null=True)
    precipitation = models.PositiveBigIntegerField(null=True)
    fishing = models.IntegerField(choices=CHOICE)
    results = models.CharField(max_length=10, null=True, blank=True)
    accuracy = models.CharField(max_length=10,null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f'Hunger Prediction on County index {self.id}'

    # def save(self, *args, **kwargs):
    #     ml_model = joblib.load('Mlmodel/hunger_prediction.joblib')
    #     ml_model.predict(
    #         [[self.population,
    #         self.max_temp, self.min_temp, self.humidity, self.rainfall, self.precipitation, self.fishing, self.results]])
    #     return super().save(*args, **kwargs)
   



