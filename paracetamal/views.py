from django.shortcuts import redirect, render

from . models import BigtableNomes
from django.http import  JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import connection

def index(request):
    return render (request, 'paracetamal/index.html')

def consulta_interacoes(request):

    if request.user.username == 'admin':
        if request.method == 'POST':
            componente_1 = str(request.POST["componente_1"])
            componente_2 = str(request.POST["componente_2"])
            print('Componente 1: ' + componente_1,'\nComponente 2: ' + componente_2)

            print(componente_2)

            resultado_interacao = '0'

            cursor = connection.cursor()

            try: 
                cursor.execute("CALL VerificaInteracao("+'"'+componente_1+'"'+','+'"'+componente_2+'")')

            except:
                print('except')
                resultado_interacao = '-1'

                return render(request, 'paracetamal/consulta_interacoes.html', { 'resultado_interacao':resultado_interacao, 'componente_1':componente_1, 'componente_2':componente_2})

            else:
                cursor.execute("CALL VerificaInteracao("+'"'+componente_1+'"'+','+'"'+componente_2+'")')
                results = cursor.fetchall()

                print(results)
                
                if results != ():
                    resultado_interacao = '1'
                print(resultado_interacao)
                return render(request, 'paracetamal/consulta_interacoes.html', { 'resultado_interacao':resultado_interacao, 'componente_1':componente_1, 'componente_2':componente_2})

    return render(request, 'paracetamal/consulta_interacoes.html')

@login_required
def autocomplete_busca_componente(request):
    
    if request.user is not None:
        componente = request.GET.get('componente')
        payload = []
        if componente:
            componente_obj = BigtableNomes.objects.filter(nome__icontains = componente)
            for item in componente_obj:
                payload.append({'id':item.id_principal, 'nome':item.nome})
            return JsonResponse({'status':200, 'data':payload})
        else:
            return JsonResponse({'status':404, 'data':""})


def login_view(request):
    if request.method == 'POST':
        usuario = request.POST['usuario']
        senha = request.POST['senha']
        user = authenticate(request, username=usuario, password=senha)
        if user is not None:
            login(request, user)
            return redirect('consulta_interacoes')
        else:
            return render(request, 'paracetamal/login.html')
    return render(request, 'paracetamal/login.html')

def logout_view(request):
    logout(request)
    return redirect('login_view')

def integrantes_grupo(request):
    return render(request, 'paracetamal/integrantes_grupo.html')


    