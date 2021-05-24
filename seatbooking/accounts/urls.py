from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from . import views

urlpatterns = [
    # ex: /5/movies/
    path('login/', LoginView.as_view(template_name='accounts/login.html', redirect_authenticated_user=True), name='signin'),
    # ex: /5/movies/
    path('logout/', LogoutView.as_view(), name='signout'),
    # ex: /5/movies/2
    path('register/', views.signup, name='signup'),
]