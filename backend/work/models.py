from django.db import models

# Create your models here.

class workTable(models.Model):
    workId = models.CharField(max_length=50)
    workDate = models.DateField()
    workTime = models.CharField(max_length=50)

    class Meta:
        db_table = 't_work'