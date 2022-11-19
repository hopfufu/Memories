from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name="index"),
    path("newpost", NewPost, name="newpost"),
    path("post/<uuid:post_id>", PostDetail, name="post-details"),
    path("tag/<slug:tag_slug>", Tags, name="tags"),
    path("<uuid:post_id>/like", like, name="like"),
    path("<uuid:post_id>/favourite", favourite, name="favourite"),
    path("<pk>/delete/", PostDeleteView.as_view(), name="post-delete"),
    path("delete-success/", success_post_delete, name="success-post-delete"),
]
