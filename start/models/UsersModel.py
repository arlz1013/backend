from django.db import models
# ? This is like a table in SQL

class Users(models.Model):

    state = {
        "Onl" : "Online",
        "Ofl" : "Ofline",
        "Ban" : "Banned"
    }

    # * Values
    # todo: Django make a Primary Key Automatic with this values
    # ?  id = models.BigAutoField(primary_key=True) 
    name = models.CharField(max_length = 50)
    pasw = models.CharField(max_length = 50)
    status = models.CharField(max_length =  3, choices = state)