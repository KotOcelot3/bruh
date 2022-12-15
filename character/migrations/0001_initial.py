# Generated by Django 3.2.16 on 2022-12-15 11:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Constellation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20, unique=True, verbose_name='Созвездие')),
            ],
            options={
                'verbose_name': 'Созвездие',
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20, unique=True, verbose_name='Страна')),
            ],
            options={
                'verbose_name': 'Страна',
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20, unique=True, verbose_name='Регион')),
            ],
            options={
                'verbose_name': 'Регион',
            },
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20, unique=True, verbose_name='Тип персонажа')),
            ],
            options={
                'verbose_name': 'Тип',
            },
        ),
        migrations.CreateModel(
            name='Weapon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20, unique=True, verbose_name='Оружие')),
            ],
            options={
                'verbose_name': 'Оружие',
            },
        ),
        migrations.CreateModel(
            name='VoiceActor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20, verbose_name='Имя')),
                ('SurName', models.CharField(max_length=20, verbose_name='Фамилия')),
                ('Country', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='character.country')),
            ],
            options={
                'verbose_name': 'Тип',
            },
        ),
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20, unique=True, verbose_name='Имя')),
                ('Description', models.CharField(max_length=200, verbose_name='Описание')),
                ('Date', models.DateField(verbose_name='Дата рождения')),
                ('Title', models.CharField(max_length=20, unique=True, verbose_name='Титул')),
                ('Image', models.ImageField(blank=True, upload_to='characters/', verbose_name='Картиночка')),
                ('Constellation', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='character.constellation')),
                ('Region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='character.region')),
                ('Type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='character.type')),
                ('Weapon', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='character.weapon')),
            ],
            options={
                'verbose_name': 'Персонаж',
                'verbose_name_plural': 'Персонажи',
            },
        ),
    ]