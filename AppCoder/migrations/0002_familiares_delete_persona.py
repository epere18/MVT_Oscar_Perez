# Generated by Django 4.1.2 on 2022-10-14 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Familiares',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('apellido', models.CharField(max_length=40)),
                ('edad', models.IntegerField()),
                ('fecha_de_nacimiento', models.DateField(null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Persona',
        ),
    ]
