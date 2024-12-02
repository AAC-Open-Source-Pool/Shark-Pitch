from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import *


urlpatterns=[
    path('profile/', views.profile_view, name='profile_view'),
    path('login/',views.login_view,name='login_view'),
    path('Investor_landing/',views.Investor_landing,name='Investor_landing'),
    path('startup/<int:user_id>/', views.startup_home_view, name='startup_home'),
    path('verification1/',views.startup_register1_view,name='startup_register1_view'),
    path('verification2/',views.startup_register2_view,name='startup_register2_view'),
    path('verification3/',views.startup_register3_view,name='startup_register3_view'),
    path('verification4/',views.startup_register4_view,name='startup_register4_view'),
    path('verification5/',views.startup_register5_view,name='startup_register5_view'),
    path('verification6/',views.startup_register6_view,name='startup_register6_view'),
    path('verification7/',views.startup_register7_view,name='startup_register7_view'),
    path('verification8/',views.startup_register8_view,name='startup_register8_view'),
    path('verification9/',views.startup_register9_view,name='startup_register9_view'),
    path('verification10/',views.startup_register10_view,name='startup_register10_view'),
    path('signup/',views.signup_view,name='signup_view'),
    path('logout/', views.logout, name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

app_name='accounts'

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)