"""
URL configuration for Tourism project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
#from django.views.generic.base import RedirectView
#from wagtail import urls as wagtail_urls
#from wagtail.admin import urls as wagtailadmin_urls
#from wagtail.documents import urls as wagtaildocs_urls
#import os.path



urlpatterns = [
    path('admin/', admin.site.urls),
    # URLs for client
    path('', include('client.urls')),
    # URLs for authentication
    path('authentication/', include('authentication.urls')),
    #path('admin/', include(wagtailadmin_urls)),
    #path('documents/', include(wagtaildocs_urls)),
    #path('cms/', include(wagtailadmin_urls)),
    
    #path('pages/', include(wagtail_urls)),

    # Optional URL for including your own vanilla Django urls/views
    #re_path(r'', include('client.urls')),

    # For anything not caught by a more specific rule above, hand over to
    # Wagtail's serving mechanism
    #re_path(r'', include(wagtail_urls)),
    
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


