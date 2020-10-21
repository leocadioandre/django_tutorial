from django.shortcuts import render

# Create your views here.

def about(request):
    send = False

    context = {
        'sucess': send
    }
    return render(request, 'about/about.html', context)
