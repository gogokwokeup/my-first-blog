from django.contrib import admin
from .models import Post
from .models import Product
from .models import Categories

admin.site.register(Post)
admin.site.register(Product)
admin.site.register(Categories)