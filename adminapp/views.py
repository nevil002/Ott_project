from django.shortcuts import render,redirect
from adminapp.models import *
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from projectapp.models import *

# Create your views here.
def admin(request):

    return render(request,'admintemp.html')

def addmovies(request):
    genre_id=Genre.objects.all()
    if request.method=='POST':
        name=request.POST['moviename']
        genre=request.POST['genre']
        year=request.POST['year']
        rating=request.POST['rating']
        discription=request.POST['discription']
        Poster=request.FILES['poster']
        File=request.FILES['file']
        Movies.objects.create(
            name=name,
            genre_id=Genre.objects.get(id=genre),
            year=year,
            rating=rating,
            discription=discription,
            Poster=Poster,
            File=File
        )
    context={
            'genre':genre_id
        }
    return render(request,'addmovies.html',context)
def viewmovies(request):
    viewmovies=Movies.objects.all()
    context={
        'viewmovies':viewmovies
    }

    return render(request,"viewmovies.html",context)

def editmovies(request):
    genre=Genre.objects.all()
    editmovies=Movies.objects.all()
    context={
        'genre':genre,
        'editmovies':editmovies
    }
    return render(request,'editmovies.html',context)

def edit_movies2(request,movie_id):
    genre=Genre.objects.all()
    edit_movies=Movies.objects.filter(id=movie_id)
    context={
        'edit_movies':edit_movies,
        'genre':genre
    }
    return render(request,"updatemovies.html",context)
def updatemovies(request,update_id):
    if request.method=="POST":
        name=request.POST['moviename']
        genre=request.POST['genre']
        year=request.POST['year']
        rating=request.POST['rating']
        discription=request.POST['discription']
        try:
            img_c=request.FILES['poster']
            fs=FileSystemStorage()
            file=fs.save(img_c.name,img_c)
        except MultiValueDictKeyError:
            file=Movies.objects.get(id=update_id).Poster

        try:
            video=request.FILES['file']
            f=FileSystemStorage()
            vfile=f.save(video.name,video)
        except MultiValueDictKeyError:
            vfile=Movies.objects.get(id=update_id).File


        Movies.objects.filter(id=update_id).update(
            name=name,
            genre_id=Genre.objects.get(id=genre),
            year=year,
            rating=rating,
            discription=discription,
            Poster=file,
            File=vfile
        )
    return render(request,'updatemovies.html')

def sign_in(request):
    details=Signup.objects.all()
    context={
        'details':details
    }
    return render(request,'signindetails.html',context)

def genre(request):
    if request.method=="POST":
        name=request.POST['genrename']
        Genre.objects.create(
            genrename=name
        )

    return render(request,'genre.html')


def delete(request):
    delete=Movies.objects.all()
    genre=Genre.objects.all()
    context={
        'delete':delete,
        'genre':genre
    }
    return render(request,'deleteselection.html',context)

def deleteselected(request,del_id):
    deleteselected=Movies.objects.filter(id=del_id).delete()
    genre=Genre.objects.all()
    context={
        'deleteselected':deleteselected,
        'genre':genre
    }
    return redirect('delete')