from django.db import models

# Create your models here.
class ProductDetails(models.Model):

    name=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    size=models.CharField(max_length=100)
    weight=models.FloatField(max_length=100)
    material=models.CharField(max_length=100)
    color=models.CharField(max_length=100)
    price=models.FloatField(null=False)
    date=models.DateField(auto_now=False,auto_now_add=False)
    image=models.ImageField(upload_to="product/agriculture",default="default.jpg")
    protectFeature=models.CharField(max_length=100,default="s")
    description=models.CharField(max_length=300,default="s")

    def __str__(self):
        return self.name

    class Meta:
        db_table='product'
        verbose_name='Detail'
        verbose_name_plural='Detail'