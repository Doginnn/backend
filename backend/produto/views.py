from rest_framework import generics
from rest_framework.response import Response
from .models import Produto
from .serializers import ProdutoSerializer
from django.shortcuts import get_object_or_404


class ProdutoList(generics.ListAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer


class ProdutoListCreate(generics.ListCreateAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer


class ProdutoRetrieveUpdate(generics.RetrieveUpdateAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer


class ProdutoDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

    def delete(self, request, pk=None, format=None):
        product = get_object_or_404(Produto, id=pk)
        product.delete()
        return Response({'message':'product deleted'})
