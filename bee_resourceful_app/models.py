from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=60)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=40)
    birthday = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.email

class Resource(models.Model):
    resource_name = models.CharField(max_length=255)
    resource_phone_number = models.CharField(max_length=10)
    resource_website = models.CharField(max_length=60)

    CATEGORY_CHOICES = (
    ("FA", "Financial Assistance"),
    ("FO", "Food"),
    ("HO", "Housing"),
    ("MD", "Medical & Dental"),
    ("MH", "Mental Health"),
    )

    category = models.CharField(max_length=21,
        choices=CATEGORY_CHOICES,
        default="Pick a Category")

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='resources')

    def __str__(self):
        return self.resource_name

