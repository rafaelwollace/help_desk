# Generated by Django 3.1.7 on 2021-03-01 20:19

from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('tipo_chamado', '0001_initial'),
        ('chamado', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chamado',
            name='sistema',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tipo_chamado.sistema'),
        ),
        migrations.AlterField(
            model_name='chamado',
            name='tipochamado',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='sistema', chained_model_field='sistema', on_delete=django.db.models.deletion.CASCADE, to='tipo_chamado.tipochamado'),
        ),
    ]
