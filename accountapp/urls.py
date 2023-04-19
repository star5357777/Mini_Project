from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path


from accountapp.views import UserCreateView, UserDetailView

app_name = 'accountapp'

urlpatterns = [
    path('login/', LoginView.as_view(template_name='accountapp/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('create/', UserCreateView.as_view(), name='create'),
    path('detail/<int:pk>', UserDetailView.as_view(), name='detail'),
]