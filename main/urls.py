from . import views
from django.urls import path

urlpatterns = [
    path('', views.main, name='main'),
    path('parts/', views.parts, name='parts'),
    path('parts/details/<int:id>', views.parts_details, name='parts_details'),
    path('softwares/', views.softwares, name='softwares'),
    path('softwares/details/<int:id>', views.softwares_details, name='softwares_details'),
    path('prebuilds/', views.prebuilds, name='prebuilds'),
    path('prebuilds/details/<int:id>', views.prebuilds_details, name='prebuilds_details'),

]