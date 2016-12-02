from django.conf.urls import include, url
from django.contrib import admin
from andelaGitUsers.views import HomepageView

urlpatterns = [
    # Examples:
    # url(r'^$', 'andelausers.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', HomepageView.as_view(), name="homepage"),
]
