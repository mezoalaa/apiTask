
# from django.http.response import JsonResponse
# from rest_framework.views import APIView
# from rest_framework import generics
# from django.shortcuts import render
# from rest_framework.decorators import api_view
# from rest_framework import status,filters
# from rest_framework.response import Response
# from .models import CoffeeShop
# from .serializers import CoffeeShopSerializer


# # #Function get views get post
# @api_view(['GET', 'POST'])
# def FBV_List(request):
#     #GET
#     if request.method == 'GET':
#         serializer = CoffeeShop.objects.all()
#         serializer_class = CoffeeShopSerializer
#         # serializer = CoffeeShopSerializer(, many=True)
#         return Response(serializer.data)
  
#     # POST
#     elif request.method == 'POST':
#         serializer = CoffeeShopSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             serializer.isAvailable = False
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#          #IF ISNT VALID
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# views.py
from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework import generics
from rest_framework.response import Response
from .models import CoffeeShop
from .serializers import CoffeeShopSerializer
from ticketTask import views


#read

class CoffeShopRead(generics.RetrieveAPIView):
    queryset= CoffeeShop.objects.all()
    serializer_class=CoffeeShopSerializer




class CoffeeShopList(generics.ListAPIView):
    queryset = CoffeeShop.objects.all()
    serializer_class = CoffeeShopSerializer

#update
class UpdateCoffee(generics.RetrieveUpdateAPIView):
    queryset = CoffeeShop.objects.all()
    serializer_class = CoffeeShopSerializer


#add

class addCoffeeShop(generics.CreateAPIView):
    serializer_class = CoffeeShopSerializer


#read

class readCoffeeShop(generics.RetrieveAPIView):
    queryset=CoffeeShop.objects.all()
    serializer_class = CoffeeShopSerializer



