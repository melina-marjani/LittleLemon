from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

app_name = 'restaurant'

urlpatterns = [
    path('menu-items/', views.MenuItemsView.as_view(), name='menuitems-list'),    path('menu-items/<int:pk>', views.SingleMenuItemView.as_view()),
    path('message/', views.msg),
    path('api-token-auth/', obtain_auth_token),
]