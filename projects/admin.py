from django.contrib import admin
from .models import Profile,Countries,Post,Technologies,Rating

class PostAdmin(admin.ModelAdmin):
    filter_horizontal =['technologies']

# Register your models here.
admin.site.register(Profile)
admin.site.register(Countries)
admin.site.register(Technologies)
admin.site.register(Post,PostAdmin)
admin.site.register(Rating)


