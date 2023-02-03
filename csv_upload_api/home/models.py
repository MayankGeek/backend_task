from django.db import models

# Create your models here.
class CsvFile(models.Model):
    id = models.CharField(primary_key=True, max_length=6)
    year = models.CharField(max_length=100)
    Industry_aggregation_NZSIOC = models.CharField(max_length=200)
    Industry_code_NZSIOC=models.IntegerField()
    Industry_name_NZSIOC=models.CharField(max_length=200)
    units=models.CharField(max_length=200)
    def __str__(self):
        return self.Industry_name_NZSIOC


        