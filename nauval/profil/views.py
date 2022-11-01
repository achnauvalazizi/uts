from django.shortcuts import render


def profil(request):
    context = {
        'judul' : 'Ini Adalah Profil'
    }
    return render(request,'profil.html',context)