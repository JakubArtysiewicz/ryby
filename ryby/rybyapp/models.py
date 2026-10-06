from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

styl_zycia_list = ["rzeczna","jeziorna","morska"]


class Ryba(models.Model):
    nazwa = models.TextField(max_length=500)
    wystepowanie = models.TextField(max_length=500)
    styl_zycia = models.TextField(choices=[(x,x) for x in styl_zycia_list])
    def __str__(self):
        return f"{self.nazwa} występowanie - {self.wystepowanie} styl_zycia - {self.styl_zycia} "

class OkresOchronny(models.Model):
    od_miesiaca = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(12)])
    do_miesiaca = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(12)])
    wymiar_ochronny = models.IntegerField()
    ryba = models.ForeignKey(Ryba, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.ryba} chroniona od {self.od_miesiaca} do {self.do_miesiaca} wymiar ochronny - {self.wymiar_ochronny} "