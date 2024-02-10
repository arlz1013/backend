from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
import json

from start.models.UsersModel import Users

from start.syntax.UsersSerial import  UserSerializer

class API:
    # * This is API 
    @api_view(['GET', 'POST'])
    def user(req):
        # * GET
        # ! Aque pide la Informacion del MODELo
        if req.method == 'GET':
            users = Users.objects.all()
            # * Lo convierte a Json con el Serial
            users_serial = UserSerializer(users, many = True)
            found = True
            resMen = "With Data"

            print(users_serial)

            # ? Este If es para Ver si hay informacion para q no saque error si no tiene pos va a decir no tengo y sale
            if not users:
                found = False
                resMen = "Without Data"
                users_serial = None
            
            # * Y aqui envia los datos como Un Get

            return JsonResponse(
                {
                    
                    'message': resMen, 
                    'content': users_serial.data
                })
        
        # * POST
        if req.method == 'POST':

            # * Este req es el JSON que Obtiene del Post y lo convierte en Algo legible para Python es decir una Lista
            user_req = JSONParser().parse(req)
            print(f"""
                    GetData ====> {user_req}
                """)

            # * Aca el UserSerilizer a ser el Intermedirio entre Modelo y la Api es el controlador el CRUD
            # todo Tons aqui manda a la Base de datos la Informacion solo con este comando
            # ! Perdon aca lo que hace es Obtener la Informacion
            user_serial = UserSerializer(data = user_req)
            # ! Aqui la valida para saber si esta estrucuturada como en La Base de Datos Pide
            if user_serial.is_valid():
                # ! Y aqui la Manda Y ya
                user_serial.save()
                return JsonResponse(
                    {
                        "SendDatas" : True,
                    })
            return JsonResponse(
                    {
                        "SendDatas" : False,
                    })
        
    @api_view(['GET', 'POST'])
    def Pass(req):
        if req.method == 'GET':
            pass


# * Por esto no entendia DJANGO por el Crud re Loco pero simplific la Vida