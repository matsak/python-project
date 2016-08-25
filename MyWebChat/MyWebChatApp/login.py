from django.shortcuts import redirect

def login_in(request):
    login = request.POST.get('inputLogin')
    password = request.POST.get('inputPassword')
    return redirect("/login")