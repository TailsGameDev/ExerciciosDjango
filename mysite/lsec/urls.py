from django.urls import path, include
from .views import _1_resumoCriptografico, _1_webServiceUI

urlpatterns = [
   path('_1_webServiceUI', _1_webServiceUI, name='_1_webServiceUI'),
   path('_1_resumoCriptografico', _1_resumoCriptografico, name='_1_resumoCriptografico'),
]