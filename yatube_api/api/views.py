from django.shortcuts import get_object_or_404
from posts.models import Group, Post, User, Follow
from rest_framework import permissions, viewsets, status, filters
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from api.permissions import IsAuthorOrReadOnlyPermission
from api.serializers import (
    CommentSerializer, FollowSerializer, GroupSerializer, PostSerializer)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [
        IsAuthenticatedOrReadOnly,
        IsAuthorOrReadOnlyPermission
    ]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [
        IsAuthenticatedOrReadOnly,
        IsAuthorOrReadOnlyPermission
    ]

    def perform_create(self, serializer):
        post = get_object_or_404(
            Post,
            id=self.kwargs.get('post_id')
        )
        serializer.save(
            author=self.request.user,
            post=post
        )

    def get_queryset(self):
        return get_object_or_404(
            Post,
            id=self.kwargs.get('post_id')
        ).comments


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthorOrReadOnlyPermission]

    def create(self, request):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


class FollowViewSet(viewsets.ModelViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['following__username']

    def get_queryset(self):
        user = get_object_or_404(User, username=self.request.user.username)
        return user.follower

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
