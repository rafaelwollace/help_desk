# Generated by Django 3.1.7 on 2021-03-01 18:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import smart_selects.db_fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tipo_chamado', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chamado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao_chamado', models.TextField()),
                ('data_chamado', models.DateField(auto_now_add=True)),
                ('hora_chamado', models.TimeField(auto_now_add=True)),
                ('arquivo_chamado', models.FileField(blank=True, null=True, upload_to='arquivos/%Y/%m/')),
                ('tecnico_chamado', models.CharField(choices=[('Rafael W.', 'Rafael W'), ('Fernando M.', 'Fernando M'), ('André C.', 'André C')], default='', max_length=50)),
                ('sistema', smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='tipochamado', chained_model_field='tipochamado', on_delete=django.db.models.deletion.CASCADE, to='tipo_chamado.sistema')),
                ('tipochamado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tipo_chamado.tipochamado')),
                ('usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RespostaChamado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resposta_descricao', models.TextField()),
                ('resposta_data', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('resposta_arquivo', models.FileField(blank=True, null=True, upload_to='arquivos/%Y/%m/')),
                ('chamado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chamado.chamado')),
                ('resposta_autor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
