from django.contrib import admin
from .models import departments,categories,SubCategories,Attributes,AttributeValues,ProductNatures,CustomerClasses,Seasons,products,ProductImages,ProductAttributes,ProductAttributeValues,ProductReferences

admin.site.register(departments)
admin.site.register(categories)
admin.site.register(SubCategories)
admin.site.register(Attributes)
admin.site.register(AttributeValues)
admin.site.register(ProductNatures)
admin.site.register(CustomerClasses)
admin.site.register(Seasons)
admin.site.register(products)
admin.site.register(ProductImages)
admin.site.register(ProductAttributes)
admin.site.register(ProductAttributeValues)
admin.site.register(ProductReferences)




