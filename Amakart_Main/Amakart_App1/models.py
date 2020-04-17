from django.db import models
from multiselectfield import MultiSelectField
# Create your models here.


class ModelClass(models.Model):
    CHOOSE_SELLING_SITES = (
        ('Amazon', 'Amazon'),
        ('Flipkart', 'Flipkart'),
    )

    range_from = models.IntegerField()
    range_to = models.IntegerField()
    choosing_selling_sites = MultiSelectField(choices=CHOOSE_SELLING_SITES)