from rest_framework import serializers
from .models import departments,categories,SubCategories,Attributes,AttributeValues,ProductNatures,CustomerClasses,Seasons,products,ProductImages,ProductAttributes,ProductAttributeValues,ProductReferences

class departmentsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = departments
        fields = ('id','url','DepartmentName','logo','description','active')

class categoriesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = categories
        fields = ('id','url','departments','CategoryName','logo','description','active')

class SubCategoriesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SubCategories
        fields = ('id','url','categories','SubCategoryName','logo','description','active')

class AttributesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Attributes
        fields = ('id','url','AttributeName','description')

class AttributeValuesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AttributeValues
        fields = ('id','url','Attributes','AttributeValues','logo','description')

class ProductNaturesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProductNatures
        fields = ('id','url','ProductNature','logo','description')

class CustomerClassesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomerClasses
        fields = ('id','url','CustomerClass','logo','description','active')

class SeasonsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Seasons
        fields = ('id','url','SeasonName','CalendarYear','CalendarDate','description','active')

class productsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = products
        fields = ('id','url','Seasons','SubCategories','ProductNatures','CustomerClasses','ProductName','description','ProductImage','ProductPrice','SalePrice','rating','caption','tag','active','CreateDBy','ModifiedBy','CreatedDate','ModifiedDate','ProductCode')

class ProductImagesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProductImages
        fields = ('id','url','products','SmallImage','LargeImage')

class ProductAttributesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProductAttributes
        fields = ('id','url','products','Attributes','active')

class ProductAttributeValuesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProductAttributeValues
        fields = ('id','url','ProductAttributes','AttributeValues','active')

class ProductReferencesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProductReferences
        fields = ('id','url','products','RefProductId')


