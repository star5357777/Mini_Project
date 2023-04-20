from django.contrib.auth.views import LogoutView
from django.urls import path


from accountapp.views import UserCreateView, UserDetailView, CustomLoginView

app_name = 'accountapp'

urlpatterns = [
    path('login/', CustomLoginView.as_view(template_name='accountapp/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('create/', UserCreateView.as_view(), name='create'),
    path('detail/<int:pk>', UserDetailView.as_view(), name='detail'),
]