from django.urls import include, path
from rest_framework.routers import DefaultRouter, Route, SimpleRouter

from .views import (CategoryViewSet, CommentViewSet, GenreViewSet,
                    ReviewViewSet, TitleViewSet, Token, UserRegView,
                    UsersViewSet)


class CustomCategoryGenreRouter(DefaultRouter):
    routes = [
        Route(
            url=r'^{prefix}/$',
            mapping={
                'get': 'list',
                'post': 'create',
            },
            name='{basename}-list',
            detail=False,
            initkwargs={'suffix': 'List'}
        ),
        Route(
            url=r'^{prefix}/{lookup}/$',
            mapping={
                'delete': 'destroy',
            },
            name='{basename}-detail',
            detail=True,
            initkwargs={'suffix': 'Detail'}
        ),
    ]


router = SimpleRouter()
router.register('users', UsersViewSet, basename='users')
router_titles_v1 = DefaultRouter()
router_category_genre_v1 = CustomCategoryGenreRouter()
router_category_genre_v1.register(
    r'categories', CategoryViewSet, basename='category'
)
router_category_genre_v1.register(r'genres', GenreViewSet, basename='genre')
router_titles_v1.register(r'titles', TitleViewSet, basename='title')
router_titles_v1.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet,
    basename='review')
router_titles_v1.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet,
    basename='comment')


urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include(router_titles_v1.urls)),
    path('v1/', include(router_category_genre_v1.urls)),
    path('v1/auth/signup/', UserRegView.as_view()),
    path('v1/auth/token/', Token.as_view()),
]
