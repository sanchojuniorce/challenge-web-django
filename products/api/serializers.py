from rest_framework.serializers import ModelSerializer
from products.models import Product

class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = (
                    'code', 'status', 'imported_t', 'url', 'creator',
                    'created_t', 'last_modified_t', 'url', 'product_name',
                    'quantity', 'brands', 'categories', 'labels', 'cities',
                    'purchase_places', 'stores', 'ingredients_text', 'traces', 
                    'serving_size', 'serving_quantity', 'nutriscore_score', 
                    'nutriscore_grade', 'main_category', 'image_url'
                )