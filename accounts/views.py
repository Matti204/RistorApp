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


from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_POST
from .forms import DishForm
from .models import Dish

def _dish_page(request, invalid_form=None, invalid_id=None):
    dishes = list(Dish.objects.filter(owner=request.user))
    create_form = invalid_form if invalid_id == "create" else DishForm(prefix="create")
    rows = [(dish, invalid_form if invalid_id == dish.pk else DishForm(instance=dish, prefix=f"edit-{dish.pk}")) for dish in dishes]
    return render(request, "dishes.html", {"rows": rows, "create_form": create_form, "open_modal": "createModal" if invalid_id == "create" else f"editModal{invalid_id}" if invalid_id else ""})

@login_required
def dishes(request):
    if request.method == "POST":
        form = DishForm(request.POST, prefix="create")
        if form.is_valid():
            dish = form.save(commit=False)
            dish.owner = request.user
            dish.save()
            return redirect("dishes")
        return _dish_page(request, form, "create")
    return _dish_page(request)

@login_required
@require_POST
def dish_edit(request, pk):
    dish = get_object_or_404(Dish, pk=pk, owner=request.user)
    form = DishForm(request.POST, instance=dish, prefix=f"edit-{pk}")
    if form.is_valid():
        form.save()
        return redirect("dishes")
    return _dish_page(request, form, pk)

@login_required
@require_POST
def dish_delete(request, pk):
    dish = get_object_or_404(Dish, pk=pk, owner=request.user)
    dish.delete()
    return redirect("dishes")
