from django.urls import path, include
from .views import _1_resumoCriptografico, _1_webServiceUI, _2_rsaKeys, _2_webServiceUI

urlpatterns = [
   path('_1_webServiceUI', _1_webServiceUI, name='_1_webServiceUI'),
   path('_1_resumoCriptografico', _1_resumoCriptografico, name='_1_resumoCriptografico'),
   path('_2_rsaKeys', _2_rsaKeys, name='_2_rsaKeys'),
   path('_2_webServiceUI', _2_webServiceUI, name='_2_webServiceUI'),
]