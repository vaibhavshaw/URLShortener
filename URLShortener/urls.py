from django.urls import path, re_path
from .views import Home, URLRedirectView

#app_name = 'URLShortener'
urlpatterns = [
    path('', Home.as_view(), name='Home'),
    re_path(r'^(?P<shortcode>[\w-]+)/$',
            URLRedirectView.as_view(), name='scode'),

]
