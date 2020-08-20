from rest_framework import serializers
from .models import Post,Profile

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ('name', 'profile_pic', 'bio', 'email')


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'photo', 'link','date')