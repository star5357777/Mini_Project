"""miniProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
# 2개의 앱을 할 때는 이렇게 as로 별명짓듯이 함
from accountapp import views as account
from boardapp import views as board

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', account.main, name = 'main-page'),
    path('sign/', account.signup, name = 'sign-up'),
    path('board/', board.board_main, name = 'board-main'),
]
