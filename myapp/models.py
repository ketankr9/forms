from django.db import models
from django.utils import timezone
# Create your models here.
class Person(models.Model):
    first_name=models.CharField("First Name",max_length=30)
    last_name=models.CharField("Last Name",max_length=30,null=True,blank=True)
    dob=models.DateField("DOB",null=True)
    cpi=models.IntegerField("CPI",null=True)
    YEARS=(('i','First'),('ii','Second'),('iii','Third'),('iv','Fourth'),('v','Fifth'),)
    year=models.CharField(max_length=3,choices=YEARS,null=True)
    DEPT=(('cse','computer science'),('mec','mechanical engineering'),('mnc','mathematica and computing'),)
    dept=models.CharField("Department",max_length=3,choices=DEPT,null=True)

    def __str__(self):
        return self.first_name+" "+self.last_name
