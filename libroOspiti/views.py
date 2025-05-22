from django.shortcuts import render
from django.contrib import messages

# Create your views here.

from .models import Autore,Commento

def index(request):
    #Il post aggiunge il messaggio
    if request.method == 'POST':
        user = request.POST.get('username')
        text = request.POST.get('message')
        #Se ci sono effettivamente i dati desiderati
        if user and text:
            #Controllo se l'utente esiste già
            numero = Autore.objects.filter(username=user).count()
            if numero == 0: #Se l'utente non esiste, lo creo
                Autore.objects.create(username=user)

            #Prendo l'autore
            aut = Autore.objects.filter(username=user).first()

            #Creo il commento
            Commento.objects.create(testo=text,autore=aut)

            messages.success(request, 'Il tuo messaggio è stato inviato con successo!')
            print(id)
        else:
            messages.error(request, 'Errore nell\'invio del messaggio. Riprova.',extra_tags="danger")


    return render(request, 'libroOspiti/home.html')


def messaggi(request):
    autoreDaMostrare = ""
    if request.method == "POST":
        autoreDaMostrare = request.POST.get("username")
    messaggi = Commento.objects.all()
    autori = Autore.objects.all()
    return render(request,"libroOspiti/messaggi.html",{"messaggi":messaggi,"autori":autori,"autoreDaMostrare":autoreDaMostrare})