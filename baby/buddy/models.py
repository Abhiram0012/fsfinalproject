from django.db import models

# Create your models here.



class Booking(models.Model):
    name=models.CharField(max_length=25,null=False)
    phone=models.BigIntegerField(null=False)
    email=models.CharField(max_length=30,null=False)
    # datecheckin=models.DateField(max_length=10,null=False)
    # datecheckout=models.DateField(max_length=10,null=False)
    # utext=models.CharField(max_length=50,null=True)


    class Meta:
        db_table='Booking'


    # class products (models.Model):

    #     name=models.CharField(max_length=50,null=False)
    #     price=models.IntegerField(max_length=50,null=False)
    #     description=models.CharField(max_length=200,null=False)
    #     category=models.CharField(max_length=50,null=False)


    #     image=models.ImageField(upload_to='uplodes/products')

    #     class Meta:
    #         db_table='products'
        
        
