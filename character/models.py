from django.db import models


class Character(models.Model):
    name = models.CharField(max_length=20, unique=True, verbose_name="Имя")
    description = models.CharField(max_length=200, verbose_name="Описание")
    date = models.DateField(verbose_name="Дата рождения")
    title = models.CharField(max_length=20, unique=True, verbose_name="Титул")
    region = models.ForeignKey('Region', on_delete=models.CASCADE, verbose_name="Регион")
    type = models.ForeignKey('Type', on_delete=models.SET_NULL, null=True, verbose_name="Тип")
    weapon = models.ForeignKey('Weapon', on_delete=models.SET_NULL, null=True, verbose_name="Оружия")
    constellation = models.ForeignKey('Constellation', on_delete=models.SET_NULL, null=True, verbose_name="Созвездие")
    voice_actor = models.ManyToManyField('VoiceActor', null=True, verbose_name="Актер озвучки")

    image = models.ImageField(upload_to="media/characters/", blank=True, verbose_name="Картиночка")

    class Meta:
        verbose_name = "Персонаж"
        verbose_name_plural = "Персонажи"

    def __str__(self):
        return self.name


class Region(models.Model):
    name = models.CharField(max_length=20, unique=True, verbose_name="Регион")

    class Meta:
        verbose_name = "Регион"
        verbose_name_plural = "Регионы"

    def __str__(self):
        return self.name


class Type(models.Model):
    name = models.CharField(max_length=20, unique=True, verbose_name="Тип персонажа")

    class Meta:
        verbose_name = "Тип"
        verbose_name_plural = "Типы"

    def __str__(self):
        return self.name


class Weapon(models.Model):
    name = models.CharField(max_length=20, unique=True, verbose_name="Оружие")

    class Meta:
        verbose_name = "Оружие"
        verbose_name_plural = "Оружие"

    def __str__(self):
        return self.name


class Constellation(models.Model):
    name = models.CharField(max_length=20, unique=True, verbose_name="Созвездие")

    class Meta:
        verbose_name = "Созвездие"
        verbose_name_plural = "Созвездия"

    def __str__(self):
        return self.name


class VoiceActor(models.Model):
    name = models.CharField(max_length=20, verbose_name="Имя")
    SurName = models.CharField(max_length=20, verbose_name="Фамилия")
    Country = models.ForeignKey('Country', on_delete=models.SET_NULL, null=True, verbose_name="Страна")

    class Meta:
        verbose_name = "Актер озвучки"
        verbose_name_plural = "Актеры озвучки"

    def __str__(self):
        return self.name


class Country(models.Model):
    Name = models.CharField(max_length=20, unique=True, verbose_name="Страна")

    class Meta:
        verbose_name = "Страна"
        verbose_name_plural = "Страны"

    def __str__(self):
        return self.Name
