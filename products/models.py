from django.db import models

# Create your models here.
class Product(models.Model):
    code = models.CharField(max_length=100)
    status = models.TextField()
    imported_t = models.TextField()
    url = models.TextField()
    creator = models.TextField()
    created_t = models.TextField()
    last_modified_t = models.TextField()
    url = models.TextField()
    product_name = models.TextField()
    quantity = models.TextField()
    brands = models.TextField()
    categories = models.TextField()
    labels = models.TextField()
    cities = models.TextField()
    purchase_places = models.TextField()
    stores = models.TextField()
    ingredients_text = models.TextField()
    traces = models.TextField()
    serving_size = models.TextField()
    serving_quantity = models.TextField()
    nutriscore_score = models.TextField()
    nutriscore_grade = models.TextField()
    main_category = models.TextField()
    image_url = models.TextField()
    
    class Meta:
        managed = True
        db_table = "products"

    def __str__(self):
        return self.nome
