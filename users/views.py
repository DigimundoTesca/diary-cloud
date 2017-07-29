from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth import login as login_django
from django.contrib.auth import logout as logout_django
from django.contrib.auth import authenticate


def login(request):
    if request.user.is_authenticated():
        return redirect('contactos:contactos')

    mensaje = ''
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login_django(request, user)
            return redirect('contactos:contactos')
        else:
            mensaje = 'Revisa tus credenciales'

    template = 'login.html'
    context = {
        'mensaje': mensaje,
    }
    return render(request,template, context)


@login_required()
def logout(request):
    logout_django(request)
    return redirect('users:login')
