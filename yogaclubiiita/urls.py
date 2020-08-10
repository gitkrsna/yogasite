
from django.urls import path
from .views import *

urlpatterns = [
    path('', home),
    path('classes/', classes),
    path('about-us/', aboutus),
    path('elements/', shop),
    path('contact/', contact),
    path('blog/', blog),

]