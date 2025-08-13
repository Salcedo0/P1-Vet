from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Message
from .forms import VeterinaryServiceRequestForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')


def chat_view(request):
    if request.method == "POST":
        sender = request.POST.get("sender")
        text = request.POST.get("text")
        if sender and text:
            Message.objects.create(sender=sender, text=text)
        return redirect("chat")  # Redirige para limpiar el formulario

    messages = Message.objects.order_by("timestamp")
    return render(request, "chat.html", {"messages": messages})

def request_veterinary_service(request):
    if request.method == "POST":
        form = VeterinaryServiceRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('service_success')
    else:
        form = VeterinaryServiceRequestForm()

    return render(request, 'request_service.html', {'form': form})

def service_success(request):
    return render(request, 'service_success.html')