from rest_framework.routers import DefaultRouter
from rest_framework import generics, status, viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .permissions import IsAuthorOrReadOnly
from .serializers import ReplySerializer, PostSerializer
from codes.models import Reply, Post


class CommentListAPIView(generics.ListAPIView):
    serializer_class = ReplySerializer

    def get_queryset(self):
        kwarg_id = self.kwargs.get("pk")
        return Reply.objects.filter(post_id=kwarg_id)


class CommentCreateAPIView(generics.CreateAPIView):
    queryset = Reply.objects.all()
    serializer_class = ReplySerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        request_user = self.request.user
        kwarg_pk = self.kwargs.get("pk")
        post = get_object_or_404(Post, id=kwarg_pk)

        serializer.save(author=request_user, post=post)



class CommentLikeAPIView(APIView):
    serializer_class = ReplySerializer

    def delete(self, request, pk):
        answer = get_object_or_404(Reply, pk=pk)
        user = request.user

        answer.loves.remove(user)
        answer.save()

        serializer_context = {"request": request}
        serializer = self.serializer_class(answer, context=serializer_context)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, pk):
        answer = get_object_or_404(Reply, pk=pk)
        user = request.user

        answer.loves.add(user)
        answer.save()

        serializer_context = {"request": request}
        serializer = self.serializer_class(answer, context=serializer_context)

        return Response(serializer.data, status=status.HTTP_200_OK)



class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by("-created_at")
    lookup_field = "id"
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostLikeAPIView(APIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        answer = get_object_or_404(Post, pk=pk)
        user = request.user

        answer.loves.remove(user)
        answer.save()

        serializer_context = {"request": request}
        serializer = self.serializer_class(answer, context=serializer_context)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, pk):
        answer = get_object_or_404(Post, pk=pk)
        user = request.user

        answer.loves.add(user)
        answer.save()

        serializer_context = {"request": request}
        serializer = self.serializer_class(answer, context=serializer_context)

        return Response(serializer.data, status=status.HTTP_200_OK)

from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"posts", PostViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path('posts/<pk>/replies/', CommentListAPIView.as_view()),
    path('posts/<pk>/new/', CommentCreateAPIView.as_view()),
    path('posts/<pk>/like/', PostLikeAPIView.as_view()),
    path("replies/<int:pk>/like/", CommentLikeAPIView.as_view()),
]

