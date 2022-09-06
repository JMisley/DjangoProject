from django.shortcuts import render
import random


# Create your views here.
def index(request):
    return render(request, 'dg/index.html')


def results(request):
    user_choice = int(request.GET.get('userChoice'))
    my_result = []

    for x in range(5):
        my_result.append(random.randint(1, 6) + random.randint(1, 6))

    return render(request, 'dg/results.html', {'userChoice': user_choice, 'my_result': my_result})
