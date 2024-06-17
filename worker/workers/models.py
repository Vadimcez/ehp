from django.db import models

# Create your models here.

class Vacancy(models.Model):
    vacancy_name = models.CharField(max_length=180, verbose_name="Должность", unique=True, blank=False)

class VacancyCategory(models.Model):
    category_name = models.CharField(max_length=100, verbose_name="Категория должности", unique=True, blank=False)
    id_vacancy = models.ForeignKey('Vacancy', on_delete=models.PROTECT)

class Human(models.Model):
    inn = models.IntegerField(verbose_name="ИНН", primary_key=True, unique=True)
    family_name = models.CharField(max_length=90, verbose_name="Фамилия")
    human_name = models.CharField(max_length=60, verbose_name="Имя")
    father_name = models.CharField(max_length=65, verbose_name="Отчество")
    gender = models.BooleanField(verbose_name="Пол", default=True)
    date_birth = models.DateField(verbose_name="Дата рождения")

