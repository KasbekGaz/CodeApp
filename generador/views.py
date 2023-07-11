from django.shortcuts import render
import random
import string


def index(request):
    return render(request, 'index.html')


def generadorContrasena(request):
    if request.method == 'POST':
        length = int(request.POST.get('length'))
        include_lowercase = request.POST.get('include_lowercase')
        include_uppercase = request.POST.get('include_uppercase')
        include_numbers = request.POST.get('include_numbers')
        include_special_chars = request.POST.get('include_special_chars')

        characters = ''

        if include_lowercase:
            characters += string.ascii_lowercase
        if include_uppercase:
            characters += string.ascii_uppercase
        if include_numbers:
            characters += string.digits
        if include_special_chars:
            characters += string.punctuation

        if len(characters) > 0:
            password = ''.join(random.choice(characters) for _ in range(length))
            
        else:
            password = "No se puede generar la contraseña. La secuencia de caracteres está vacía."
            
    return render(request, 'index.html', {'password': password})
        