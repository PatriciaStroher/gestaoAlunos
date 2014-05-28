from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required



from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gestaoAlunos.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^$', login_required(TemplateView.as_view(template_name = 'home.html')),
    #		name = 'home'),
    url(r'^admin/', include(admin.site.urls)),
)
