from django.db import models

# Create your models here.

class User(models.Model):
    fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    email=models.EmailField()
    mobile=models.PositiveIntegerField()
    address=models.TextField()
    gender=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    profile_pic=models.ImageField(upload_to="profile_pic/",default="")
    usertype=models.CharField(max_length=100,default="buyer")

    def __str__(self):
        return self.fname+" "+self.lname
    
class Pizza(models.Model):
    seller=models.ForeignKey(User,on_delete=models.CASCADE)
    category=(
        ("Veg","Veg"),
        ("Burger","Burger"),
        ("Paratha","Paratha"),
        ("Pizza_mania","Pizza_mania"),

     )
    pizza_category=models.CharField(max_length=100,choices=category,default=0)

    types=(
            ("Farmhouse_pizza","Farmhouse_pizza"),
            ("Peppy_paneer_pizza","Peppy_paneer_pizza"),
            ("Mexican_green_wave_pizza","Mexican_green_wave_pizza"),
            ("Deluxe_veggie_pizza","Deluxe_veggie_pizza"),
            ("Classic_burger_pizza","Classic_burger_pizza"),
            ("Premium_burger_pizza","Premium_burger_pizza"),
            ("Corn_n_cheese_paratha_pizza","Corn_n_cheese_paratha_pizza"),
            ("Paneer_paratha_pizza","Paneer_paratha_pizza"),
            ("Cheesy_pizza","Cheesy_pizza"),
            ("Paneer_&_onion_pizza","Paneer_&_onion_pizza"),
            ("Golden_corn_pizza","Golden_corn_pizza"),
            ("Cheese_n_tomato_pizza","Cheese_n_tomato_pizza"),
            )
    pizza_types=models.CharField(max_length=100,choices=types,default=0)
    pizza_price = models.IntegerField(default=0)
    
    size=(
        ("7","7"),
        ("8","8"),
        ("9","9"),
        ("10","10"),

    )
    pizza_size=models.CharField(max_length=100,choices=size,default=0)
    pizza_pic=models.ImageField(upload_to="pizza_pic",default="")



    def __str__(self):
        return self.seller.fname+" - "+self.pizza_types
    