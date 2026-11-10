from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.core.validators import MinValueValidator

class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("L'email ? obbligatoria.")
        email = self.normalize_email(email).strip().lower()
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        if extra_fields.get("is_staff") is not True or extra_fields.get("is_superuser") is not True:
            raise ValueError("Il superutente deve avere is_staff e is_superuser attivi.")
        return self._create_user(email, password, **extra_fields)

class User(AbstractUser):
    username = None
    email = models.EmailField("email", unique=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = UserManager()

    def save(self, *args, **kwargs):
        self.email = self.email.strip().lower()
        super().save(*args, **kwargs)


class Dish(models.Model):
    owner = models.ForeignKey("accounts.User", on_delete=models.CASCADE, related_name="dishes")
    name = models.CharField("Nome", max_length=150)
    description = models.TextField("Descrizione", blank=True)
    ingredients = models.TextField("Ingredienti")
    allergens = models.TextField("Allergeni", blank=True)
    price = models.DecimalField("Prezzo (?)", max_digits=8, decimal_places=2, null=True, blank=True, validators=[MinValueValidator(0)])

    class Meta:
        ordering = ["name", "pk"]

    def __str__(self):
        return self.name
