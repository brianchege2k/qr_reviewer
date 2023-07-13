from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
class Review(models.Model):
    class Meta:
        db_table = 'review_table'

    name = models.CharField(max_length=100)
    email = models.EmailField(default='')
    review_text = models.TextField()
    rating = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(10)])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
