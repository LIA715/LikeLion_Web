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

def classdetail1(request):
    return render(
        request,
        'one_pages/classdetail1.html'
    )

def classdetail2(request):
    return render(
        request,
        'one_pages/classdetail2.html'
    )
# Create your views here.
