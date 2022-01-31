"""Main url project file"""
from django.urls import path

from accounts.views.auth import Signup, Login  # , Logout, UpdateToken
from accounts.views.users import UserCredentialsView, UserAvatarView

app_name = "accounts"

urlpatterns = [

    path('auth/signup/', Signup.as_view()),
    path('auth/login/', Login.as_view()),
    # path(ROOT_API_PATH + 'auth/update_token/', UpdateToken.as_view()),
    # path(ROOT_API_PATH + 'auth/logout/', Logout.as_view()),

    path('profile/user/', UserCredentialsView.as_view()),
    path('profile/user/avatar/', UserAvatarView.as_view())
]
