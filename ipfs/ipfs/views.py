from django.shortcuts import render
from django.http import HttpResponse
from ipfshttpclient import connect

def upload_file(request):
    if request.method == 'POST' and request.FILES['file']:
        file = request.FILES['file']
        
        # Conexión al nodo IPFS local
        client = connect()
        
        # Subir el archivo a IPFS
        res = client.add(file)
        
        # Cerrar la conexión al nodo IPFS
        client.close()
        
        # Mostrar el CID del archivo subido
        return HttpResponse(f'Archivo subido a IPFS. CID: {res["Hash"]}')
    
    return render(request, 'upload_file.html')