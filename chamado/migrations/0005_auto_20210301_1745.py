# Generated by Django 3.1.7 on 2021-03-01 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chamado', '0004_auto_20210301_1741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chamado',
            name='tecnico_chamado',
            field=models.CharField(choices=[('', '-'), ('Rafael W.', 'Rafael W'), ('Fernando M.', 'Fernando M'), ('André C.', 'André C')], default='', max_length=50),
        ),
    ]
