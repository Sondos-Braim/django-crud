from django.urls import path,include
from .views import movies_view,details_view,add_view,update_view,delete_view

urlpatterns = [
    path('', movies_view.as_view(),name='home'),
    path('<int:pk>/',details_view.as_view(),name='details'),
    path('add/',add_view.as_view(),name='add'),
    path('<int:pk>/update/',update_view.as_view(),name='update'),
    path('<int:pk>/delete/',delete_view.as_view(),name='delete')
]