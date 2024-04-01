from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=300)
    email = models.EmailField()
    phone_num = models.CharField(max_lehgth=20)
    addres = models.TextField()
    registration_data = models.DateField(auto_now_add = True)

class Product(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=10)
    quantity = models.PositiveIntegerField()
    added_data = models.DateField(auto_now_add = True)

    def _str_(self):
        return self.name
    
class Buy(models.Model):
    client = models.ForeignKey(Client, on_delete= models.CASCADE)
    products = models.ManyToManyField(Product)
    total_amount = models.DecimalField(decimal_places=2, max_digits=10)
    buy_data = models.DateField(auto_now_add = True)

    def calculate_total_amount(self):
        total = sum(product.price * product.quantity for product in self.products.all())
        self.total_amount = total
        self.save()

    def _str_(self):
        return f'Buy {self.id} by {self.client.name}'