from django.contrib import admin
from .models import Coffee

# Register your models here.
#the model create a database automaticaly

class CoffeeAdmin(admin.ModelAdmin):
    list_display = ('name','price','quantity')


admin.site.register(Coffee, CoffeeAdmin)
#after writing that i start to see coffe in my admin panel
#after adding class coffeeadmin and add coffeeadmin we get price and info instead of object we had
