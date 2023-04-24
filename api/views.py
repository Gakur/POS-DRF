from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Store, Inventory, Debts, Sales, Receipts, ReceiptVAT, Profits
from .serializers import StoreSerializer


# Create your views here.

class StoreAPIView(APIView):
    def get(self, request):
        store = Store.objects.all()
        serializer = StoreSerializer(store, many=True)
        return Response({"store": serializer.data})
