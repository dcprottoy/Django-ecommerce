from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()

router.register('departments',views.departmentView)
router.register('categories',views.categorieView)
router.register('SubCategories',views.SubCategorieView)
router.register('Attributes',views.AttributeView)
router.register('AttributeValues',views.AttributeValueView)
router.register('ProductNatures',views.ProductNatureView)
router.register('CustomerClasses',views.CustomerClassView)
router.register('Seasons',views.SeasonView)
router.register('products',views.productView)
router.register('ProductImages',views.ProductImageView)
router.register('ProductAttributes',views.ProductAttributeView)
router.register('ProductAttributeValues',views.ProductAttributeValueView)
router.register('ProductReferences',views.ProductReferenceView)


urlpatterns = [
    path('',include(router.urls))
]
