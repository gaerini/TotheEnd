"""
URL configuration for ddj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from ddjapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('detail/<int:article_id>', views.detail, name='detail'),

    path('registration/signup/', views.signup, name='signup'),
    path('registration/login/', views.login, name='login'),
    path('registration/logout/', views.logout, name='logout'),

    path('accounts/', include('allauth.urls')),
    path('deleteComment/<int:article_id>/<int:comment_id>', views.deleteComment, name='deleteComment'),
    path('recomment/<int:article_id>/<int:comment_id>', views.recomment, name='recomment'),
    path('deleteRecomment/<int:article_id>/<int:recomment_id>', views.deleteRecomment, name='deleteRecomment'),
    path('stoneDetail/<int:room_id>', views.stoneDetail, name='stoneDetail'),
    path('stoneRequest/<int:room_id>', views.stoneRequest, name='stoneRequest'),
    path('confirm/<int:room_id>', views.confirm, name='confirm'),
    path('stone/', views.stone, name='stone'),

]
