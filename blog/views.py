from django.shortcuts import render
from .models import User, Category, Post, Comment
from .serialisers import UserSerializer, CategorySerializer, PostSerializer, CommentSerializer
from rest_framework import viewsets, filters
from django.utils.text import slugify
from django.contrib.auth.hashers import make_password
from rest_framework.permissions import IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
from .permissions import IsAuthorOrReadOnly, IsStaffOrAdminOrReadOnly
from drf_spectacular.utils import extend_schema
from django_filters.rest_framework import DjangoFilterBackend
from .filters import PostFilter
from .pagination import StandardResultsSetPagination




# Create your views here.
@extend_schema(tags=["Users"])
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def perform_create(self, serializer):
        # Hash the password before saving the user
        password = serializer.validated_data.get('password')
        if password:
            serializer.validated_data['password'] = make_password(password)
        serializer.save()

    def perform_update(self, serializer):
        # Hash the password if it's being updated
        password = serializer.validated_data.get('password')
        if password:
            serializer.validated_data['password'] = make_password(password)
        serializer.save()
    
    def get_queryset(self):
        queryset = super().get_queryset()
        username = self.request.query_params.get('username')
        if username:
            queryset = queryset.filter(username=username)
        return queryset
    

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context

    def perform_destroy(self, instance):
        # Delete all posts and comments associated with the user
        instance.posts.all().delete()
        instance.comments.all().delete()
        instance.delete()



@extend_schema(tags=["Categories"])
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action in ['list', 'retrieve']:
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        # Your filter logic is perfect here
        queryset = super().get_queryset()
        name = self.request.query_params.get('name')
        if name:
            queryset = queryset.filter(name__icontains=name)
        return queryset



@extend_schema(tags=["Posts"])
class PostViewSet(viewsets.ModelViewSet):
    # select_related avoids the "N+1" problem when fetching 140+ comments later
    queryset = Post.objects.select_related('author', 'category').prefetch_related('comments').all()
    serializer_class = PostSerializer
    lookup_field = "slug"
    
    # This ensures:
    # 1. Anyone can GET (ReadOnly)
    # 2. Only Authenticated Staff/Admins can POST/PUT/DELETE
    permission_classes = [IsStaffOrAdminOrReadOnly]
    
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_class = PostFilter # Ensure this handles 'category' and 'author'
    pagination_class = StandardResultsSetPagination


    def get_queryset(self):
        # Start with the optimized base queryset
        queryset = self.queryset              
        
        category = self.request.query_params.get('category')
        author = self.request.query_params.get('author')
        
        if category:
            # Filtering by category name
            queryset = queryset.filter(category__name__icontains=category)
        if author:
            # Filtering by author username
            queryset = queryset.filter(author__username__icontains=author)
        
        return queryset

    def perform_create(self, serializer):
        # Required to link the new post to the logged-in user
        serializer.save(author=self.request.user)


@extend_schema(tags=["Comments"])
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.select_related('author', 'post').all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        
        # 2. Filter by post ID (The user should only see comments for a specific post)
        post_id = self.request.query_params.get('post')
        if post_id:
            queryset = queryset.filter(post_id=post_id)
            
        return queryset

    def perform_create(self, serializer):
        # 3. Automatically assign the logged-in user as the author
        serializer.save(author=self.request.user)