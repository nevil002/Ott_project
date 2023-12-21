from django.urls import path
from adminapp import views
urlpatterns = [
    path('',views.admin,name="adminapp"),
    path('addmovies',views.addmovies,name="addmovies"),
    path('viewmovies',views.viewmovies,name="viewmovies"),
    path('editmovies',views.editmovies,name='editmovies'),
    path('edit_movies2/<int:movie_id>',views.edit_movies2,name='edit_movies2'),
    path('updatemovies/<int:update_id>',views.updatemovies,name='updatemovies'),
    path('sign_in',views.sign_in,name='sign_in'),
    path('genre',views.genre,name="genre"),
    path('delete',views.delete,name='delete'),
    path('deleteselected/<int:del_id>',views.deleteselected,name='deleteselected')
    
    
]
