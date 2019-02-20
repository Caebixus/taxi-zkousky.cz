from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Feedback
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def hodnoceni(request):
    if request.method == 'POST':
        if request.POST['message']:
            feedback = Feedback()
            feedback.message = request.POST['message']
            feedback.feedbackUser = request.user
            feedback.save()
            return render(request, 'hodnoceni/hodnoceni.html', {'error':'Hodnoceni odesláno!'})
        else:
            return render(request, 'hodnoceni/hodnoceni.html', {'error':'Prosím o napsání Vašeho komentáře do políčka!'})
    else:
        return render(request, 'hodnoceni/hodnoceni.html', {})
