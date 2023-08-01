# Generated by Django 4.2.3 on 2023-07-21 13:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_user_profile_pic_user_usertype'),
    ]

    operations = [
        migrations.CreateModel(
            name='pizza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('Veg', 'Veg'), ('Burger', 'Burger'), ('Paratha', 'Paratha'), ('Pizza_mania', 'Pizza_mania')], max_length=100)),
                ('product_brand', models.CharField(choices=[('Farmhouse Pizza', 'Farmhouse Pizza'), ('Peppy Paneer Pizza', 'Peppy Paneer Pizza'), ('Mexican Green Wave Pizza', 'Mexican Green Wave Pizza'), ('Deluxe Veggie Pizza', 'Deluxe Veggie Pizza'), ('Classic Burger Pizza', 'Classic Burger Pizza'), ('Premium Burger Pizza', 'Premium Burger Pizza'), ('Corn n Cheese Paratha Pizza', 'Corn n Cheese Paratha Pizza'), ('Paneer Paratha Pizza', 'Paneer Paratha Pizza'), ('Cheesy Pizza', 'Cheesy Pizza'), ('Paneer & Onion Pizza', 'Paneer & Onion Pizza'), ('Golden Corn Pizza', 'Golden Corn Pizza'), ('Cheese n Tomato Pizza', 'Cheese n Tomato Pizza')], max_length=100)),
                ('product_price', models.IntegerField(default=0)),
                ('product_size', models.CharField(choices=[('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], max_length=100)),
                ('product_pic', models.ImageField(default='', upload_to='product_pic')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.user')),
            ],
        ),
    ]