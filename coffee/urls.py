from django.urls import path
from django.views.generic import TemplateView

from .views import RoastListView, BeanListView, RoastDetailView, BeanDetailView, FileListView

urlpatterns = [
    path('', TemplateView.as_view(template_name="home.html")),
    path('roasts/', RoastListView.as_view(template_name="roast/list.html")),
    path('roasts/<slug:slug>/', RoastDetailView.as_view(template_name="roast/detail.html"), name="roast-detail"),
    path('beans/<slug:slug>/', BeanDetailView.as_view(template_name="bean/detail.html"), name="bean-detail"),
    path('beans/', BeanListView.as_view(template_name="bean/list.html")),
    path('signup/', TemplateView.as_view(template_name="auth/signup.html")),
    path('login/', TemplateView.as_view(template_name="auth/login.html")),
    path('files/', FileListView.as_view(template_name="files.html")),
]