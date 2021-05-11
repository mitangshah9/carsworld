from django.shortcuts import get_object_or_404, render
from rest_framework import generics, serializers,viewsets,status
from rest_framework import permissions,filters
from .serializers import PostSerializer
from blog.models import Post  
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser,FormParser
from rest_framework.permissions import DjangoModelPermissions, IsAdminUser, DjangoModelPermissions, BasePermission, IsAuthenticated, SAFE_METHODS

# Create your views here.
class PostUserWritePermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        
        if request.method in SAFE_METHODS:
            return True
        
        return obj.author == request.user


class PostList(generics.ListCreateAPIView):
    permission_classes= [IsAuthenticated]
    queryset= Post.postobjects.all()
    serializer_class=PostSerializer




class PostDetail(generics.RetrieveUpdateDestroyAPIView,PostUserWritePermission):
    permission_classes=[PostUserWritePermission]
    queryset= Post.objects.all()
    serializer_class=PostSerializer



class PostListDetailFilter(generics.ListAPIView):
    queryset=Post.objects.all()
    serializer_class=PostSerializer
    filter_backends=[filters.SearchFilter]
    search_fields = ['^excerpt', 'content']


# class PostList(viewsets.ViewSet):
#     permission_classes= [permissions.IsAuthenticated]
#     queryset = Post.objects.all()

#     def list(self,request):
#         serializer_class=PostSerializer(self.queryset,many=True)
#         return Response(serializer_class.data)

#     def retrieve(self,request,pk=None):
#         post=get_object_or_404(self.queryset,pk=pk)
#         serializer_class=PostSerializer(post)
#         return Response(serializer_class.data)


# class PostList(viewsets.ModelViewSet):
#     permission_classes= [permissions.IsAuthenticated]
#     serializer_class=PostSerializer

#     def get_object(self, queryset=None, **kwargs):
#         item = self.kwargs.get('pk')
#         return get_object_or_404(Post, title=item)

#     def get_queryset(self):
#         return Post.objects.all()





###############
#CRUD
###############


#This class is only used for handling non-file fields.

# class CreatePost(generics.CreateAPIView):  
#     #permission_classes = [permissions.IsAuthenticated]
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

#The class below is the class for handling both file and Text Fields.

class CreatePost(APIView):
    parser_classes = [MultiPartParser , FormParser]
    
    def post(self, request , format=None):
        print(request.data)
        serializer = PostSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)







class AdminPostDetail(generics.RetrieveAPIView):
    #permission_classes = [permissions.IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class EditPost(generics.UpdateAPIView):
    #permission_classes = [permissions.IsAuthenticated]
    serializer_class = PostSerializer
    queryset = Post.objects.all()

class DeletePost(generics.RetrieveDestroyAPIView):
    #permission_classes = [permissions.IsAuthenticated]
    serializer_class = PostSerializer
    queryset = Post.objects.all()
