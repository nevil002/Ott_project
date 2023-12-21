from django.urls import path
from projectapp import views
urlpatterns = [
    path('user_home',views.user_home,name='user_home'),
    path('signin',views.signin,name='signin'),
    path('signup',views.signup,name='signup'),
    path('playmovie/<int:movie_id>',views.playmovie,name="playmovie"),
    path('plans',views.plans,name='plans'),
    path('view_movies_based_on_genre/<int:genre_id>',views.view_movies_based_on_genre,name='view_movies_based_on_genre'),
    path('review',views.review,name='review'),
    path('comment/<int:movie_id>/',views.comment,name='comment'),
    path('like/<int:comment_id>',views.like,name='like'),
    path('dislike/<int:comment_id>',views.dislike,name='dislike'),
    path('wishlist/<int:liked_id>',views.wishlist,name='wishlist'),
    path('viewwishlist',views.viewwishlist,name='viewwishlist'),
    path('deletewishlist/<int:delid>',views.deletewishlist,name='deletewishlist'),
    
    # path('view_comment',views.viewcomment,name="viewcomment")
]
