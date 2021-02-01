from django.db import models

# Create your models here.

class departments(models.Model):
    DepartmentName = models.CharField(max_length=80,unique=True,null=False)
    logo = models.TextField(max_length=255)
    description = models.CharField(max_length=400)
    active = models.CharField(max_length=1,default='Y')

    def __str__(self):
        return self.DepartmentName
    
class categories(models.Model):
    departments = models.ForeignKey(departments,on_delete=models.CASCADE)
    CategoryName = models.CharField(max_length=80,unique=True,null=False)
    logo = models.TextField(max_length=255)
    description = models.CharField(max_length=400)
    active = models.CharField(max_length=1,default='Y')

    def __str__(self):
        return self.CategoryName
    

class SubCategories(models.Model):
    categories = models.ForeignKey(categories,on_delete=models.CASCADE)
    SubCategoryName = models.CharField(max_length=80,unique=True,null=False)
    logo = models.TextField(max_length=255)
    description = models.CharField(max_length=400)
    active = models.CharField(max_length=1,default='Y')

    def __str__(self):
        return self.SubCategoryName
    

class Attributes(models.Model):
    AttributeName = models.CharField(max_length=80,unique=True,null=True)
    description = models.CharField(max_length=400)

    def __str__(self):
        return self.AttributeName
    

class AttributeValues(models.Model):
    Attributes = models.ForeignKey(Attributes,on_delete=models.CASCADE)
    AttributeValues = models.CharField(max_length=120,null=False)
    logo = models.TextField(max_length=255)
    description = models.CharField(max_length=400)

    def __str__(self):
        return self.AttributeValues
    

    
class ProductNatures(models.Model):
    ProductNature = models.CharField(max_length=80,unique=True,null=False)
    logo = models.TextField(max_length=255)
    description = models.CharField(max_length=400)

    def __str__(self):
        return self.ProductNature
    

class CustomerClasses(models.Model):
    CustomerClass = models.CharField(max_length=80,unique=True,null=False)
    logo = models.TextField(max_length=255)
    description = models.CharField(max_length=400)
    active	= models.CharField(max_length=1,default='Y')

    def __str__(self):
        return self.CustomerClass
    

class Seasons(models.Model):
    SeasonName = models.CharField(max_length=80,unique=True,null=False)
    CalendarYear = models.IntegerField()
    CalendarDate = models.DateTimeField()
    description = models.CharField(max_length=400)
    active = models.CharField(max_length=1,default='Y')

    def __str__(self):
        return self.SeasonName
    

class products(models.Model):
    Seasons = models.ForeignKey(Seasons,on_delete=models.CASCADE)
    SubCategories = models.ForeignKey(SubCategories,on_delete=models.CASCADE)
    ProductNatures = models.ForeignKey(ProductNatures,on_delete=models.CASCADE)
    CustomerClasses = models.ForeignKey(CustomerClasses,on_delete=models.CASCADE)
    ProductName = models.CharField(max_length=200,unique=True,null=False)
    description = models.CharField(max_length=800)
    ProductImage = models.TextField(max_length=255)
    ProductPrice = models.IntegerField()
    SalePrice = models.IntegerField()
    rating = models.IntegerField()
    caption = models.CharField(max_length=80)
    tag = models.CharField(max_length=1)
    active = models.CharField(max_length=1,default='Y')
    CreateDBy = models.CharField(max_length=80)
    ModifiedBy = models.CharField(max_length=80)
    CreatedDate = models.DateTimeField(auto_now_add=True)
    ModifiedDate = models.DateTimeField(auto_now_add=True)
    ProductCode = models.TextField(max_length=120)

    def __str__(self):
        return self.ProductName 
    

class ProductImages(models.Model):
    products = models.ForeignKey(products,on_delete=models.CASCADE)
    SmallImage = models.TextField(max_length=255)
    LargeImage = models.TextField(max_length=255)


class ProductAttributes(models.Model):
    products = models.ForeignKey(products,on_delete=models.CASCADE)
    Attributes = models.ForeignKey(Attributes,on_delete=models.CASCADE)
    active = models.CharField(max_length=1,default='Y')

    def __str__(self):
        return str(self.products)



class ProductAttributeValues(models.Model):
    ProductAttributes = models.ForeignKey(ProductAttributes,on_delete=models.CASCADE)
    AttributeValues = models.ForeignKey(AttributeValues,on_delete=models.CASCADE)
    active = models.CharField(max_length=1,default='N')

    def __str__(self):
        return self.AttributeValues

class ProductReferences(models.Model):
    products = models.ForeignKey(products,on_delete=models.CASCADE)
    RefProductId = models.IntegerField(null=False)
