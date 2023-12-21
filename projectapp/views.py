from django.shortcuts import render, redirect
from projectapp.models import *
from adminapp.models import *

# Create your views here.
def user_home(request):
    movies = Movies.objects.all()
    context = {
        'movies':movies,
    }
    return render(request,'user.html', context)


def signin(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']

        if Signup.objects.filter(email = email, password = password).exists():
            data = Signup.objects.filter(email = email, password = password).values('name', 'id').first()
            request.session['u_name'] = data['name']
            request.session['u_id'] = data['id']
            request.session['u_email'] = email
            request.session['u_password'] = password
            return redirect('user_home')
        
        else:
            return redirect('signin')
    return render(request,'signinpage.html')

def playmovie(request,movie_id):
    request.session['redirect_mv_id'] = movie_id
    play=Movies.objects.filter(id=movie_id)
    movies = Movies.objects.all()

    viewcomment=Comments.objects.filter(movie_details=movie_id)
    userdetails=request.session.get('u_id')
    fav=Wishlist.objects.filter(user_details=userdetails,movie_details=movie_id)
   
    context={
        
        'play':play,
        'movies':movies,
        'viewcomment':viewcomment,
        'fav':fav

    }
    return render(request,'playmovies.html',context)
def signup(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']
        Signup.objects.create(
            name=name,
            email=email,
            password=password
        )
    return render(request,'signup.html')

def plans(request):
    return render(request,'plans.html')

def view_movies_based_on_genre(request, genre_id):
    movies_g = Movies.objects.filter(genre_id=genre_id)
    context = {
        'movies_g':movies_g,
    }
    return render(request,'genrepage.html', context)


def review(request):
    if request.method=="POST":
        review=request.POST['review']
        Review.objects.create(
            review=review
        )

    return render(request,'playmoviews.html')

def comment(request,movie_id):
    user_id = request.session.get('u_id')
    # comments=Comments.objects.filter(id=comment_id)
    if request.method=="POST":
        comment=request.POST['text']
        Comments.objects.create(
            user_details=Signup.objects.get(id=user_id),
            movie_details= Movies.objects.get(id=movie_id),
            comment=comment,
        )
    return render(request,'playmovies.html')
# def viewcomment(request):
#     viewcomment=Comments.objects.all()
#     context={
#         'viewcomment':viewcomment
#     }
#     render(request,'playmovies.html',context)

def like(request,comment_id):
    mv_id = request.session['redirect_mv_id']
    # like=Movies.objects.get()
    likes=Comments.objects.get(id=comment_id)
    if not likes.is_liked:
        likes.like += 1
        likes.is_liked=True
        likes.save()
   
    return redirect(f'/playmovie/{mv_id}')

def dislike(request,comment_id):
    
    dislike=Comments.objects.get(id=comment_id)
    mv_id=request.session['redirect_mv_id']
    if not dislike.is_disliked:
        dislike.dislike +=1
        dislike.is_disliked=True
        dislike.save()
    return redirect(f'/playmovie/{mv_id}')   

def wishlist(request,liked_id):
    Wishlist.objects.create(
        user_details=Signup.objects.get(id=request.session.get('u_id')),
        movie_details=Movies.objects.get(id=liked_id)
    )
    return redirect(f'/playmovie/{liked_id}')

def viewwishlist(request):
    user_id = request.session.get('u_id')
    wish_items=Wishlist.objects.filter(user_details=user_id)
    context={
        'wish_items':wish_items,
    }
    return render(request,'wishlist.html',context)

def deletewishlist(request,delid):
    user_id = request.session.get('u_id')
    Wishlist.objects.filter(user_details=user_id,movie_details=delid).delete()
    
    
    return redirect(f'/playmovie/{delid}')
    