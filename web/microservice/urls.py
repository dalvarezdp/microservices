from django.conf.urls import url

from microservice.views import PostsListView

urlpatterns = [
    url("^$", PostsListView.as_view(), name="posts_list")
]