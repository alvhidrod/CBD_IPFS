from django.shortcuts import render
from django.http import HttpResponse
from ipfshttpclient import connect
from .models import File

def pagina_principal(request):
    return render(request, 'home.html')


def upload_file(request):
    if request.method == 'POST' and request.FILES['file']:
        file = request.FILES['file']
        client = connect()
        res = client.add(file)
        client.close()
        nombre = request.nombre
        File.objects.create(creador = nombre, clave = res["Hash"])
        return HttpResponse(f'Archivo subido a IPFS. CID: {res["Hash"]}')
    
    return render(request, 'upload_file.html')