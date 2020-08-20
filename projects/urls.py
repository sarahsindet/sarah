from django.conf.urls import url
from django.conf.urls.static import static
from . import views
from django.conf import settings


urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^create/profile$',views.create_profile, name='create-profile'),
    url(r'^new/project$',views.new_project, name='new-project'),
    url(r'^directory/',views.directory, name='directory'),
    url(r'^profile/',views.profile, name='profile'),
    url(r'^user/(?P<username>\w{0,50})',views.user_profile,name='user-profile'),
    url(r'^site/(\d+)',views.site,name='site'),
    url(r'^search/',views.search_results, name='search_results'),
    

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)