from django.shortcuts import redirect

def registration_in(request):
    last_name = request.POST.get('lastName')
    first_name = request.POST.get('firstName')
    father_name = request.POST.get('fatherName')
    birth_date = request.POST.get('preview_date')
    email = request.POST.get('inputEmail')
    login = request.POST.get('inputRegLogin')
    password = request.POST.get('inputRegPassword')
    sex = request.POST.get('genderRadios')
    return redirect("/registration")
