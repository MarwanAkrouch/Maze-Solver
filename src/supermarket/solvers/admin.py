from django.contrib import admin
from solvers.models import Product
from solvers.models import CheckedProduct


"""
	Models registred

	Product
	CheckedProduct

	Permission 
	-------
	To be stocked in the db

"""

admin.site.register(Product)
admin.site.register(CheckedProduct)