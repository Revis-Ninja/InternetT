from django.urls import path
from rango import views
from rango.views import about

app_name = 'rango'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', about, name="about"),
    path('category/<slug:category_name_slug>/',
           views.show_category, name='show_category')
]


