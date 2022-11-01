from django.shortcuts import render


def blog(request):
    context = {
        'judul' : 'Ini Adalah blog'
    }
    return render(request,'blog.html',context)