from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer


# Class 1 - Product - Create

class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # during lesson #14 - added the 'or None' line 23-25 and the code breaks
    # not sure why but left out for now

    def perform_create(self, serializer):
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content')
        serializer.save(content=content)

product_create_view = ProductListCreateAPIView.as_view()

# Class 2 - Product - Detail

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

product_detail_view = ProductDetailAPIView.as_view()

# Class 3 - Product - List

class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

product_list_view = ProductListAPIView.as_view()
