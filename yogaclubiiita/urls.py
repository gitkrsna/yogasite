
from django.urls import path
from .views import *

urlpatterns = [
    path('index/', home),
    path('classes/', classes),
    path('about-us/', aboutus),
    path('elements/', shop),
    path('contact/', contact),
    path('blog/', blog),

]