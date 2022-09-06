from django.shortcuts import render

from movie.models import Movie


def index(request):
    movies = Movie.objects.all()

    return render(request, 'tu/index.html', {'movies': movies})


def addMovie(request):
    if request.method == 'POST':
        movie_title = request.POST['title']
        movie_year = request.POST['year']
        movie_rating = request.POST['rating']
        movie_director = request.POST['director']
        movie_poster = request.FILES['movie_poster']

        movie_info = Movie(title=movie_title,
                           year=movie_year,
                           rating=movie_rating,
                           director=movie_director,
                           movie_poster=movie_poster)
        movie_info.save()

    return render(request, 'tu/add_movie.html')
