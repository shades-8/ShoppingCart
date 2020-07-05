from django.db import models


class Product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=30)
    product_category=models.CharField(max_length=50, default="")
    product_sub_category=models.CharField(max_length=50, default="")
    product_price=models.IntegerField(default=0)

    desc=models.CharField(max_length=1000)
    prod_date=models.DateField( auto_now=True )
    image=models.ImageField(upload_to="shop/images", default="")

    def __str__(self):
        return self.product_name


