from django.shortcuts import render
from django.core.mail import EmailMessage
from .forms import ContactForm

# Create your views here.

def contact(request):
    send = False

    form = ContactForm(request.POST or None)
    if form.is_valid():
        #enviar e-mail
        nome = request.POST.get('nome','')
        email = request.POST.get('email','')
        mensagem = request.POST.get('mensagem','')
        email = EmailMessage(
            "Mensagem do Blog do André",
            "De {} <{}> Escreveu: \n\n{}".format(nome, email, mensagem),
            "não-responder@inbox.mailtrap.io",
            ["andreleocadio4@gmail.com"],
            reply_to=[email]
        )
        try:
            email.send()
            send = True
        except:
            send = False

    context = {
        'form':form,
        'sucess':send
    }
    return render(request,'contact/contact.html',context)


