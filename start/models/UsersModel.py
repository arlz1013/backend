from django.db import models
# ? This is like a table in SQL
# todo Esto genera y interaciioona con la  base de datos pra le creacion de tablas

# todo Se organiza por Nombre de la tabla la Clase y sus atributos un dato randmon es que no es necesario crear la primary key Por que la Genera automaticamente
# ? Este Modelo Pasa a los Serial para Cambiar la estrucuturaciond e datos pra ser mas legible por nosotros
# * Con solo la creacion de esta MODELO se hace el CRUD Con solo jhacer esto
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