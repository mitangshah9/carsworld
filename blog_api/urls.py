from django.urls import path
from .views import PostList,PostDetail,CreatePost,AdminPostDetail,EditPost,DeletePost,PostListDetailFilter
from rest_framework.routers import DefaultRouter

app_name = 'blog_api'

urlpatterns = [
    path('<int:pk>/', PostDetail.as_view(), name='detailcreate'),
    path('', PostList.as_view(), name='listcreate'),
    path('search/custom/', PostListDetailFilter.as_view(),name='postsearch'),
   # Post Admin URLs
    path('admin/create/', CreatePost.as_view(), name='createpost'),
    path('admin/read/postdetail/<int:pk>/', AdminPostDetail.as_view(), name='admindetailpost'),
    path('admin/edit/<int:pk>/', EditPost.as_view(), name='editpost'),
    path('admin/delete/<int:pk>/', DeletePost.as_view(), name='deletepost'),
]

# router=DefaultRouter()   #same thing is working for the viewsets and modelviewsets
# router.register('',PostList,basename='post')
# urlpatterns+=router.urls