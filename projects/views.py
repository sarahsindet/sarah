from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm,PostForm,RatingsForm
from django.contrib.auth.models import User
from .models import Profile,Countries,Post,Technologies,Rating
from django.core.exceptions import ObjectDoesNotExist
import datetime as dt
from django.db.models import Q
from .serializers import PostSerializer,ProfileSerializer
from rest_framework import viewsets




# Create your views here.
def index(request):
    try:
        posts = Post.objects.all()
        posts = posts[::-1]
    except ObjectDoesNotExist:
        posts = None
    return render(request, 'index.html', {'posts': posts})




@login_required(login_url='/accounts/login/')
def create_profile(request):
    current_user = request.user
    if request.method=='POST':
        form = ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.username = current_user

            profile.save()
        return redirect('index')
    else:
        form=ProfileForm()

    return render(request,'create_profile.html',{"form":form})


@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    profile =Profile.objects.get(username=current_user)
    posts=Post.objects.filter(username=current_user)

    return render(request,'profile.html',{"posts":posts,"profile":profile})


@login_required(login_url='/accounts/login/')
def new_project(request):
    current_user = request.user
    # profile =Profile.objects.get(username=current_user)
    # post =Post.objects.get(title=post)
    if request.method =='POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.username = current_user
            post.save()
    else:
        form = PostForm()

    return render(request,'new_project.html',{"form":form})

@login_required(login_url='/accounts/login/')
def user_profile(request,username):
    user = User.objects.get(username=username)
    profile =Profile.objects.get(username=user)
    posts=Post.objects.filter(username=user)

    return render(request,'user-profile.html',{"posts":posts,"profile":profile})


def directory(request):
    date = dt.date.today()
    current_user = request.user
    profile =Profile.objects.get(username=current_user)
    posts=Post.objects.all()
    

    return render(request,'directory.html',{"posts":posts,"profile":profile,"date":date})


@login_required(login_url='/accounts/login/')
def search_results(request):
    current_user = request.user
    profile =Profile.objects.get(username=current_user)
    if 'post' in request.GET and request.GET["post"]:
        search_term = request.GET.get("post")
        searched_posts = Post.search_post(search_term)
        message=f"{search_term}"

        print(searched_posts)

        return render(request,'search.html',{"message":message,"posts":searched_posts,"profile":profile})

    else:
        message="You haven't searched for any term"
        return render(request,'search.html',{"message":message})


@login_required(login_url='/accounts/login/')
def site(request,site_id):
    current_user = request.user
    profile =Profile.objects.get(username=current_user)

    try:
        post= Post.objects.get(id=site_id)
    except:
        raise ObjectDoesNotExist()

    try:
        ratings = Rating.objects.filter(post_id=site_id)
        design = Rating.objects.filter(post_id=site_id).values_list('design',flat=True)
        usability = Rating.objects.filter(post_id=site_id).values_list('usability',flat=True)
        creativity = Rating.objects.filter(post_id=site_id).values_list('creativity',flat=True)
        content = Rating.objects.filter(post_id=site_id).values_list('content',flat=True)
        total_design=0
        total_usability=0
        total_creativity=0
        total_content = 0
        print(design)
        for rate in design:
            total_design+=rate
        print(total_design)

        for rate in usability:
            total_usability+=rate
        print(total_usability)

        for rate in creativity:
            total_creativity+=rate
        print(total_creativity)

        for rate in content:
            total_content+=rate
        print(total_content)

        overall_score=(total_design+total_content+total_usability+total_creativity)/4

        print(overall_score)

        post.design = total_design
        post.usability = total_usability
        post.creativity = total_creativity
        post.content = total_content
        post.overall_score = overall_score

        post.save()

    except:
        return None

    if request.method =='POST':
        form = RatingsForm(request.POST,request.FILES)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.post= post
            rating.profile = profile
            rating.overall_score = (rating.design+rating.usability+rating.creativity+rating.content)/2
            rating.save()
    else:
        form = RatingsForm()

    return render(request,"site.html",{"post":post,"profile":profile,"ratings":ratings,"form":form})


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
