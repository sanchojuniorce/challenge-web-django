from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from products.models import Product
from .serializers import ProductSerializer

class ProductsViewSet(ModelViewSet):
    #queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.all()

    def list(self, request, *args, **kwargs):
        return super(ProductsViewSet, self).list(request, *args, **kwargs)

    def show(self, request, *args, **kwargs):
        return super(ProductsViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super(ProductsViewSet, self).create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(ProductsViewSet, self).destroy(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super(ProductsViewSet, self).retrieve(request, *args, **kwargs)
         
    def update(self, request, *args, **kwargs):
        return super(ProductsViewSet, self).update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super(ProductsViewSet, self).partial_update(request, *args, **kwargs)
