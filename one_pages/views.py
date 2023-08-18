from django.shortcuts import render
def landing(request):
    return render(
        request,
        'one_pages/landing.html'

    )

def about_me(request):
    return render(
        request,
        'one_pages/class.html'
    )

def naver(request):
    return render(
        request,
        'one_pages/naverclass.html'
    )

def youtube(request):
    return render(
        request,
        'one_pages/youtube.html'
    )

def korea(request):
    return render(
        request,
        'one_pages/24class.html'
    )

def about(request):
    return render(
        request,
        'one_pages/about.html'
    )
# Create your views here.
