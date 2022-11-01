from django.shortcuts import render


def about(request):
    context = {
        'judul' : 'Ini Adalah about'
    }
    return render(request,'about.html',context)