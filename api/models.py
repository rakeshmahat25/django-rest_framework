from django.db import models

# Create your models here.


#creating company model

class Company(models.Model):
    name = models.CharField(max_length=50)
    company_id =models.AutoField(primary_key=True)
    location = models.CharField(max_length=50)
    about = models.TextField()
    type = models.CharField(max_length=100, choices=(('IT','IT'),('Non IT','Non IT')))
    added_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)


    def __str__(self):
        return self.name

    
##Employer

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=200)
    phone = models.BigIntegerField()
    about = models.TextField()
    position= models.CharField(max_length=50, choices=(
        ('Manager','manager'),
        ('Software Developer','sd'),
        ("Project Leader",'pl')
    ))
    company = models.ForeignKey(Company, on_delete =models.CASCADE)

    def __str__(self) -> str:
        return self.name
