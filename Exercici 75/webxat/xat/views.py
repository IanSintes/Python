from django.shortcuts import render, redirect
from .models import Missatge
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    if request.method == "POST":
        text = request.POST.get("text")
        if text:
            Missatge.objects.create(usuari=request.user, text=text)
        return redirect("index")
    missatges = Missatge.objects.all().order_by("data")
    return render(request, "xat/index.html", {"missatges": missatges})


# Create your views here.
