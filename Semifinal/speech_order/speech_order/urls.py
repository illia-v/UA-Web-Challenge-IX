from django.conf.urls import include, url
from django.contrib import admin
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from pizza import urls as pizza_urls
from our_pizzeria import urls as our_pizzeria_urls


def redirect_to_pizza_url(request):
    """
    Redirecting to the pizza app main page.
    It is very useful if the project is growing. Because users will
    be able to use their saved urls and a status code of the project
    main page is not 404.
    """
    return HttpResponseRedirect(reverse('pizza:index'))


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', redirect_to_pizza_url),
    url(r'^pizza/', include(pizza_urls, namespace='pizza')),
    url(
        r'^our_pizzeria/',
        include(our_pizzeria_urls, namespace='our_pizzeria')
    )
]
