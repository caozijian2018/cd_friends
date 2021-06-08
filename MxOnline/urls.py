"""MxOnline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url, include
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
from django.views.static import serve
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token

import xadmin

from apps.users.views import LoginView, LogoutView, SendSmsView, DynamicLoginView, RegisterView
from MxOnline.settings import MEDIA_ROOT
from apps.operations.views import IndexView
from rest_framework.documentation import include_docs_urls

from apps.courses.views import CoursesViewSet, CourseApiView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from users.jwt import MyTokenObtainPairView

router = routers.DefaultRouter()
router.register(r'test_course_restframework', CoursesViewSet)

urlpatterns = [
    # path('admin/', admin.site.urls),
    url(r'^backend/api/', include(router.urls)),
    path('xadmin/', xadmin.site.urls),
    path('', IndexView.as_view(), name="index"),
    path('login/', LoginView.as_view(), name="login"),
    path('register/', RegisterView.as_view(), name="register"),
    path('d_login/', DynamicLoginView.as_view(), name="d_login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^send_sms/', csrf_exempt(SendSmsView.as_view()), name="send_sms"),
    url(r'^test_111/', CourseApiView.as_view(), name="testcourse"),
    #配置上传文件的访问url
    url(r'^media/(?P<path>.*)$', serve, {"document_root":MEDIA_ROOT}),
    # url(r'^static/(?P<path>.*)$', serve, {"document_root":STATIC_ROOT}),

    #机构相关页面
    url(r'^org/', include(('apps.organizations.urls', "organizations"), namespace="org")),

    #机构相关页面
    url(r'^course/', include(('apps.courses.urls', "courses"), namespace="course")),

    #用户相关操作
    url(r'^op/', include(('apps.operations.urls', "operations"), namespace="op")),

    #个人中心
    url(r'^users/', include(('apps.users.urls', "users"), namespace="users")),

    #配置富文本相关的url
    url(r'^ueditor/',include('DjangoUeditor.urls')),

    path('api-auth/', include('rest_framework.urls')),
    url(r'^docs/',include_docs_urls(title='暮雪online')),
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),

    # CoursesViewSet TokenObtainPairView
    # url(r'^docs/', CoursesViewSet),

]

#1. CBV(class base view) FBV(function base view)

#编写一个view的几个步骤
"""
1. view代码
2. 配置url
3. 修改html页面中相关的地址
"""
