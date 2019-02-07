from django.db import models

# Create your models here.
category_choices=(
	('M', 'Meat'),
	('V','Vegetable')
)
class Product(models.Model):
	name = models.CharField(max_length=20)
	price = models.DecimalField(max_digits=5, decimal_places=2)

	category = models.CharField(
		max_length=10,
		choices=category_choices,
	default='M'
	
	)
	image = models.ImageField(blank=True)

	def __str__(self):
	 return self.name#, self.price