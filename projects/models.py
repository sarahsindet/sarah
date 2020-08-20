from django.db import models
from django.contrib.auth.models import User
import datetime as dt
from django.db.models import Q


# Create your models here.
class Profile(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profile')
    profile_pic = models.ImageField(upload_to='images/', default='default.png')
    bio = models.TextField(max_length=500, default="", blank=True)
    name = models.CharField(blank=True, max_length=120)
    country = models.ForeignKey('Countries',on_delete=models.CASCADE)
    email = models.EmailField(max_length=100, blank=True)

    def __str__(self):
        return f'{self.username} profile'


class Countries(models.Model):
    countries = models.CharField(max_length=100)

    def __str__(self):
        return self.countries

    class Meta:
        ordering = ['countries']


    def save_country(self):
        self.save()

    @classmethod
    def delete_country(cls,countries):
        cls.objects.filter(countries=countries).delete()


class Post(models.Model):
    title = models.CharField(max_length=150)
    photo = models.ImageField(upload_to='landingpage/')
    link = models.URLField(max_length=255)
    description = models.TextField(max_length=255)
    technologies = models.ManyToManyField('Technologies', max_length=255)
    username = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.title
    
    @classmethod
    def all_posts(cls):
        return cls.objects.all()
        
    @classmethod
    def search_post(cls,search_term):
        posts = cls.objects.filter(Q(username__username=search_term) | Q(title__icontains=search_term))
        return posts

    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()


class Technologies(models.Model):
    technologies = models.CharField(max_length=100)

    def __str__(self):
        return self.technologies

    def save_technology(self):
        self.save()

    @classmethod
    def delete_technology(cls,technologies):
        cls.objects.filter(technologies=technologies).delete()

class Rating(models.Model):
    rating = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10'),
    )
    design = models.IntegerField(choices=rating,blank=True,default=0)
    usability = models.IntegerField(choices=rating,blank=True,default=0)
    creativity = models.IntegerField(choices=rating,blank=True,default=0)
    content = models.IntegerField(choices=rating,blank=True,default=0)
    overall_score = models.IntegerField(blank=True,default=0)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)

    def save_rating(self):
        self.save()

    def __str__(self):
        return f'{self.post} Rating'

