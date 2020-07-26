
from django.db import models
from django.contrib.auth.models import User


           
class artwork1(models.Model):
    user1=models.ForeignKey(User,on_delete=models.CASCADE)
    art=models.ImageField(upload_to='artworks',blank=True)   
    def __str__(self):
        return str(self.user1)
        
class more(models.Model):
    user1=models.OneToOneField(User,on_delete=models.CASCADE)
    ppic=models.ImageField(upload_to='profile_pics' ,blank=True)
    
    def __str__(self):
        return str(self.user1)
 
 
class more2(models.Model):
    user1=models.OneToOneField(User,on_delete=models.CASCADE)
    coverphoto=models.ImageField(upload_to='cover_pics' ,blank=True)
    
    def __str__(self):
        return str(self.user1)
        
        
class details(models.Model):
    user1=models.OneToOneField(User,on_delete=models.CASCADE)
    age=models.IntegerField(blank=False)
    Dob=models.DateField(blank=True,null=True)
    about=models.TextField(blank=True)
    link=models.URLField(blank=True)
    link1=models.URLField(blank=True)
    def __str__(self):
        return str(self.user1)
        
    