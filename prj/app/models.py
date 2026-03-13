from django.db import models
from django.contrib.auth.models import User

class Epocha(models.Model):
    nazev = models.CharField(max_length=100, unique=True, verbose_name="Název epochy")
    obdobi = models.CharField(max_length=100, blank=True, null=True, verbose_name="Časové vymezení (např. 5. stol. př. n. l.)")
    charakteristika = models.TextField(verbose_name="Základní charakteristika a duch doby")

    class Meta:
        verbose_name = "Epocha"
        verbose_name_plural = "Epochy"
        ordering = ['nazev']

    def __str__(self):
        return self.nazev


class Smer(models.Model):
    nazev = models.CharField(max_length=100, unique=True, verbose_name="Název směru")
    definice = models.TextField(verbose_name="Definice a hlavní principy")

    class Meta:
        verbose_name = "Myšlenkový směr"
        verbose_name_plural = "Myšlenkové směry"
        ordering = ['nazev']

    def __str__(self):
        return self.nazev


class Myslitel(models.Model):
    jmeno = models.CharField(max_length=150, verbose_name="Jméno myslitele")
    roky_zivota = models.CharField(max_length=100, blank=True, null=True, verbose_name="Roky života (např. 1844–1900)")
    zivotopis = models.TextField(verbose_name="Životopis a intelektuální vývoj")

    epocha = models.ForeignKey(Epocha, on_delete=models.SET_NULL, null=True, blank=True, related_name='myslitele', verbose_name="Historická epocha")
    smery = models.ManyToManyField(Smer, blank=True, related_name='myslitele', verbose_name="Myšlenkové směry")

    class Meta:
        verbose_name = "Myslitel"
        verbose_name_plural = "Myslitelé"
        ordering = ['jmeno']

    def __str__(self):
        return self.jmeno


class Dilo(models.Model):
    nazev = models.CharField(max_length=200, verbose_name="Název díla")
    rok_vydani = models.CharField(max_length=50, blank=True, null=True, verbose_name="Rok prvního vydání")
    popis = models.TextField(blank=True, null=True, verbose_name="Stručný obsah či význam díla")

    autor = models.ForeignKey(Myslitel, on_delete=models.CASCADE, related_name='dila', verbose_name="Autor díla")

    class Meta:
        verbose_name = "Dílo"
        verbose_name_plural = "Díla"
        ordering = ['nazev']

    def __str__(self):
        return f"{self.nazev} ({self.autor.jmeno})"


class Myslenka(models.Model):
    text = models.TextField(verbose_name="Znění myšlenky či citátu")
    
    autor = models.ForeignKey(Myslitel, on_delete=models.CASCADE, related_name='myslenky', verbose_name="Autor myšlenky")
    dilo = models.ForeignKey(Dilo, on_delete=models.CASCADE, related_name='myslenky', null=True, blank=True, verbose_name="Zdrojové dílo")
    
    ulozili_uzivatele = models.ManyToManyField(User, blank=True, related_name='ulozene_myslenky', verbose_name="Uživatelé, kteří si uložili")

    class Meta:
        verbose_name = "Myšlenka"
        verbose_name_plural = "Myšlenky"

    def __str__(self):
        return f"{self.autor.jmeno}: {self.text[:30]}..."


class Komentar(models.Model):
    text = models.TextField(verbose_name="Text komentáře")
    vytvoreno = models.DateTimeField(auto_now_add=True, verbose_name="Čas vytvoření")
    
    uzivatel = models.ForeignKey(User, on_delete=models.CASCADE, related_name='komentare', verbose_name="Autor komentáře")

    myslenka = models.ForeignKey(Myslenka, on_delete=models.CASCADE, related_name='komentare', null=True, blank=True)
    myslitel = models.ForeignKey(Myslitel, on_delete=models.CASCADE, related_name='komentare', null=True, blank=True)
    dilo = models.ForeignKey(Dilo, on_delete=models.CASCADE, related_name='komentare', null=True, blank=True)
    smer = models.ForeignKey(Smer, on_delete=models.CASCADE, related_name='komentare', null=True, blank=True)

    class Meta:
        verbose_name = "Komentář"
        verbose_name_plural = "Komentáře"
        ordering = ['-vytvoreno']

    def __str__(self):
        return f"Reflexe od {self.uzivatel.username} ({self.vytvoreno.strftime('%d.%m.%Y')})"