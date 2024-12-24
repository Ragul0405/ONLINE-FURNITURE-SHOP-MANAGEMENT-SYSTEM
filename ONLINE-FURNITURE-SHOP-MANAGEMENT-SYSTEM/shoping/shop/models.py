from django.db import models
import datetime
import os

def getfilename(request,filename):
    now_time = datetime.datetime.now().strftime('%y%m%d%H:%M:%S')
    new_filename = '%s%s'%(now_time,filename)
    return os.path.join('uploads/',new_filename)

class Category(models.Model):
    name=models.CharField(max_length=150,null=False,blank=False)
    image = models.ImageField(upload_to=getfilename,null=True,blank=False)
    description=models.TextField(max_length=500,null=False,blank=False)
    status=models.BooleanField(default=False,help_text='0-show,1-hiidden')
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

class product(models.Model):
    Catagory=models.ForeignKey(Category,on_delete=models.CASCADE)
    name=models.CharField(max_length=150,null=False,blank=False)
    vender=models.CharField(max_length=150,null=False,blank=False)
    product_image = models.ImageField(upload_to=getfilename,null=True,blank=False)
    quentity=models.IntegerField(null=False,blank=False)
    orginal_price=models.FloatField(null=False,blank=False)
    selling_price=models.FloatField(null=False,blank=False)
    description=models.TextField(max_length=500,null=False,blank=False)
    state=models.BooleanField(default=False,help_text='0-show,1-hiidden')
    tranding=models.BooleanField(default=False,help_text='0-default,1-Trending')
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name