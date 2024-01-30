from django.shortcuts import render,redirect,Http404
from .forms import * # ContactoForm
from .models import Producto
from django.shortcuts import get_object_or_404


#from django.http import HttpResponse

# Create your views here.
def vista_about(request):
    return render(request, 'about.html')



def vista_contacto(request):
    Info_enviado = False
    email = ""
    title = ""
    text = ""

    if request.method == "POST":
        formulario = ContactoForm(request.POST)
        if formulario.is_valid():
            Info_enviado = True
            email = formulario.cleaned_data['correo']
            title = formulario.cleaned_data['titulo']
            text = formulario.cleaned_data['texto']
            # Aquí puedes realizar alguna acción con los datos del formulario, como guardarlos en la base de datos.
            # Después de procesar el formulario, puedes redirigir a otra página o mostrar un mensaje de éxito al usuario.

    else:  # Si es método GET u otro método
        formulario = ContactoForm()

    context = {
        'Info_enviado': Info_enviado,
        'email': email,
        'title': title,
        'text': text,
        'formulario': formulario,
    }

    return render(request, 'contacto.html', context)



def vista_lista_producto(request):
    lista = Producto.objects.filter()
    return render(request, 'lista_producto.html', locals())


def vista_agregar_producto(request):
    if request.method == 'POST':
        formulario = agregar_producto_form(request.POST,request.FILES)
        if formulario.is_valid():
            prod = formulario.save(commit= False)
            
            prod.save()
            #formulario.save_m2m()
            return redirect('/lista_producto/')
    else:
        formulario = agregar_producto_form()
    return render(request,'agregar_producto.html',locals())

def vista_ver_producto(request, id_prod):
   
    try:
        p = Producto.objects.get(id=id_prod)
    except Producto.DoesNotExist:
        raise Http404("Producto no encontrado")
    return render(request, 'ver_producto.html', locals())




def vista_editar_producto(request, id_prod):
    # Obtener el producto existente o mostrar un error 404 si no se encuentra
    producto = producto.objectos(Producto, id=id_prod)
    
    if request.method == "POST":
        # Si la solicitud es un POST, procesar el formulario con los datos enviados
        formulario = agregar_producto_form(request.POST, request.FILES, instance=producto)
        if formulario.is_valid():
            # Si el formulario es válido, guardar los cambios en el producto
            formulario.save()
            return redirect('/lista_producto/')
    else:
        # Si la solicitud es GET, crear un formulario prefilled con los datos del producto
        formulario = agregar_producto_form(instance=producto)

    # Renderizar el template con el formulario prefilled
    return render(request, 'vista_editar_producto.html', {'formulario': formulario, 'producto': producto})


def vista_eliminar_producto(request, id_prod):
    prod = Producto.objects.get(id=id_prod)
    prod.delete()
    return redirect ('/lista_producto/')

