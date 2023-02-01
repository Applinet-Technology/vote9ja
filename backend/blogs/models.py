from django.db import models


from django.db.models import Model, CharField, ForeignKey, TextField, IntegerField,OneToOneField, DateTimeField, CASCADE

from accounts.models.users import User

class Category(Model):
    name = CharField('Blog Category', max_length=50, unique=True) 
    def __str__(self):
        return self.name


class Blog(Model):
    category = ForeignKey(Category, on_delete = CASCADE)
    title= CharField('Blog title', max_length=50, default='blog title', unique=True)
    body = TextField('Blog body', unique=True)
    #blog_reference = 
    date= DateTimeField(auto_now=True)
    num_stars=IntegerField(default=0)
    blogger= ForeignKey(User, on_delete=CASCADE, related_name='blogger')
    @property
    def username(self):
        return self.blogger.username
    
    class Meta:
        ordering=['date',]
    
    
    def __str__(self):
        return f'{self.title} {self.date}'

class Comment(Model):
    blog = OneToOneField(Blog, on_delete=CASCADE, related_name='bloga')