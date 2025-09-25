from django.shortcuts import render, redirect
from .forms import SolicitudForm

def solicitud_create(request):
    if request.method == 'POST':
        form = SolicitudForm(request.POST, request.FILES)  # <<-- request.FILES para archivos
        if form.is_valid():
            form.save()
            return redirect('solicitud_success')
    else:
        form = SolicitudForm()
    return render(request, 'solicitudes/solicitud_form.html', {'form': form})

def solicitud_success(request):
    return render(request, 'solicitudes/solicitud_success.html')
