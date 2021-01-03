from django.contrib import admin
from .models import Question,Question_Type
from import_export.admin import ImportExportModelAdmin
from import_export import resources

# Register your models here.
    
    
class QuestionResource(resources.ModelResource):

    class Meta:
        model = Question

class QuestionAdmin(ImportExportModelAdmin):
    resource_class = QuestionResource

class QuestionTypeResource(resources.ModelResource):
    class Meta:
    	model=Question_Type
class QuestionTypeAdmin(ImportExportModelAdmin):
    resource_class=QuestionTypeResource
            
admin.site.register(Question,QuestionAdmin)
admin.site.register(Question_Type,QuestionTypeAdmin)

