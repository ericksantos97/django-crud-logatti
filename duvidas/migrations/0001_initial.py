# Generated by Django 3.0.7 on 2020-06-18 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Duvidas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=100)),
                ('nivel', models.CharField(max_length=20)),
                ('data', models.CharField(max_length=20)),
                ('nome_aluno', models.CharField(max_length=100)),
                ('nome_professor', models.CharField(max_length=100)),
                ('tipo', models.CharField(max_length=20)),
            ],
        ),
    ]
