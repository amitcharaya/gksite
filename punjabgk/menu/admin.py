from django.contrib import admin
from .models import Message, Menus, Categories,Postdetail,SubCategories
from import_export.admin import ImportExportModelAdmin
from import_export import resources

# Register your models here.
class PostDetailResource(resources.ModelResource):
    class Meta:
        model=Postdetail
class PostAdmin(ImportExportModelAdmin):
    resource_class = PostDetailResource

admin.site.register(Message)
admin.site.register(Menus)
admin.site.register(Categories)
admin.site.register(Postdetail,PostAdmin)
admin.site.register(SubCategories)