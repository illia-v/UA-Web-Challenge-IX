from django.conf.urls import url
import statistics_app.views


urlpatterns = [
    url(r'^$', statistics_app.views.index, name='index'),
    url(r'^repositories/(?P<login>.+)/(?P<repo>.+)/$',
        statistics_app.views.repo_details, name='repo_details'),
    url(r'^top_25_repositories_by_stars/$', statistics_app.views.top_repo,
        name='repos_by_stars')
]
