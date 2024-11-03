from django.shortcuts import render

# Create your views here.

def platform(request):
    return render(request,'fourth_task/platform.html')


def games(request):
    game_1 = 'Atomic Heart'
    game_2 = 'Cyberpunk 2077'
    game_3 = 'PayDay2'
    context = {
        'games':[game_1, game_2, game_3,]
    }
    return render(request, 'fourth_task/games.html', context)


def cart(request):
    return render(request, 'fourth_task/cart.html')