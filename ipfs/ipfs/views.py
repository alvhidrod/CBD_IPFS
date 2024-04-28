from django.shortcuts import render
from ipfshttpclient import connect
from .models import File

def pagina_principal(request):
    return render(request, 'home.html')


def lista_archivos(request):
    archivos = File.objects.all()
    return render(request,'listado.html', {
        'archivos': archivos
    } )

def upload_file(request):
    if request.method == 'POST' and request.FILES['file']:
        file = request.FILES['file']
        client = connect()
        res = client.add(file)
        client.close()
        nombre = request.POST.get('nombre')
        print(nombre)
        key= res["Hash"]
        archivo= res["Name"]
        File.objects.create(creador = nombre, clave = key,nombre_archivo= archivo)
        return render(request,'confirmacion.html',{'key':key})
    
    return render(request, 'upload_file.html')