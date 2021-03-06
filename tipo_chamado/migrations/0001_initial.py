# Generated by Django 3.1.7 on 2021-03-01 17:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TipoChamado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_tipo', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Sistema',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sistema_nome', models.CharField(max_length=255)),
                ('tipochamado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tipo_chamado.tipochamado')),
            ],
        ),
    ]
