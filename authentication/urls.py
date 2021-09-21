from authentication import views
from django.urls import path
from .views import Home
from django.conf.urls import url
urlpatterns = [
    path('home',views.Home,name="home"),
    path('list',views.tablelist,name="list"),
    url(r'^transactions$',views.transactionsApi),
    url(r'^transactions/([0-9]+)$',views.transactionsApi),
    # path('login/', login_view, name="login"),
    # path('business/', business_details, name="business_details"),
    # path('login', mobile_login, name="login"),
    # path('register/', register_user, name="register"),

    # path("logout/", LogoutView.as_view(), name="logout")
]

