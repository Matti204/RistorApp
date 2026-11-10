from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError, transaction
from django.shortcuts import redirect, render
from .forms import RegistrationForm

@login_required
def home(request):
    return render(request, "home.html")

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            try:
                with transaction.atomic():
                    user = form.save()
            except IntegrityError:
                form.add_error("email", "Questa email ? gi? registrata.")
            else:
                login(request, user)
                return redirect("home")
    else:
        form = RegistrationForm()
    return render(request, "registration/register.html", {"form": form})
