from django.shortcuts import render
from rest_framework import viewsets,permissions
from .models import departments,categories,SubCategories,Attributes,AttributeValues,ProductNatures,CustomerClasses,Seasons,products,ProductImages,ProductAttributes,ProductAttributeValues,ProductReferences
from .serializers import departmentsSerializer,categoriesSerializer,SubCategoriesSerializer,AttributesSerializer,AttributeValuesSerializer,ProductNaturesSerializer,CustomerClassesSerializer,SeasonsSerializer,productsSerializer,ProductImagesSerializer,ProductAttributesSerializer,ProductAttributeValuesSerializer,ProductReferencesSerializer
# Create your views here.

class departmentView(viewsets.ModelViewSet):
    queryset = departments.objects.all()
    serializer_class = departmentsSerializer
    
class categorieView(viewsets.ModelViewSet):
    queryset = categories.objects.all()
    serializer_class = categoriesSerializer

class SubCategorieView(viewsets.ModelViewSet):
    queryset = SubCategories.objects.all()
    serializer_class = SubCategoriesSerializer

class AttributeView(viewsets.ModelViewSet):
    queryset = Attributes.objects.all()
    serializer_class = AttributesSerializer

class AttributeValueView(viewsets.ModelViewSet):
    queryset = AttributeValues.objects.all()
    serializer_class = AttributeValuesSerializer

class ProductNatureView(viewsets.ModelViewSet):
    queryset = ProductNatures.objects.all()
    serializer_class = ProductNaturesSerializer

class CustomerClassView(viewsets.ModelViewSet):
    queryset = CustomerClasses.objects.all()
    serializer_class = CustomerClassesSerializer

class SeasonView(viewsets.ModelViewSet):
    queryset = Seasons.objects.all()
    serializer_class = SeasonsSerializer

class productView(viewsets.ModelViewSet):
    queryset = products.objects.all()
    serializer_class = productsSerializer

class ProductImageView(viewsets.ModelViewSet):
    queryset = ProductImages.objects.all()
    serializer_class = ProductImagesSerializer

class ProductAttributeView(viewsets.ModelViewSet):
    queryset = ProductAttributes.objects.all()
    serializer_class = ProductAttributesSerializer

class ProductAttributeValueView(viewsets.ModelViewSet):
    queryset = ProductAttributeValues.objects.all()
    serializer_class = ProductAttributeValuesSerializer

class ProductReferenceView(viewsets.ModelViewSet):
    queryset = ProductReferences.objects.all()
    serializer_class = ProductReferencesSerializer

