## URLconf to map a view to URL

#====================================================================================
# from django.conf.urls import url
# from . import views

# app_name='polls'

# urlpatterns = [
#     url(r'^$', views.index, name='index'),
#     url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
#     url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
#     url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
# ]
#====================================================================================


#====================================================================================
## Use generic views: Less code is better: Amend URLconf
from django.conf.urls import url
from . import views

app_name='polls'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
## Note that the name of the matched pattern in the regexes of the second and third patterns has changed from <question_id> to <pk>.
#====================================================================================