from django.shortcuts import render
import random
import string

def index(request):
    return render(request, 'generador/index.html')

def generadorContrasena(request):
    if request.method == 'POST':
        # ? Manda a pedir los campos del formulario
        length = int(request.POST.get('length'))
        include_lowercase = request.POST.get('include_lowercase')
        include_uppercase = request.POST.get('include_uppercase')
        include_numbers = request.POST.get('include_numbers')
        include_special_chars = request.POST.get('include_special_chars')

        # ? Crea una variable con los caracteres que se van a usar
        characters = ''
        if include_lowercase:
            characters += string.ascii_lowercase
        if include_uppercase:
            characters += string.ascii_uppercase
        if include_numbers:
            characters += string.digits
        if include_special_chars:
            characters += string.punctuation
        
        # ? Genera la contraseña aleatoria con los parametros dados
        password = ''.join(random.choice(characters) for i in range(length))

        return render(request, 'index.html', {'password': password})
    
    return render(request, 'index.html')