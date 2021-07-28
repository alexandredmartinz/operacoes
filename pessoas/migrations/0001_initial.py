# Generated by Django 3.2.5 on 2021-07-28 01:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Telefone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=13)),
            ],
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino')], default='M', max_length=1)),
                ('nome', models.CharField(max_length=255)),
                ('data_nascimento', models.DateField(blank=True)),
                ('cpf', models.CharField(max_length=13, unique=True)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='fotos_presos')),
                ('telefone', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pessoas.telefone')),
            ],
        ),
    ]