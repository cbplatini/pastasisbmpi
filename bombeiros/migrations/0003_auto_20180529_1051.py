# Generated by Django 2.0.5 on 2018-05-29 13:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bombeiros', '0002_auto_20180512_2334'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='area_ocorrencia',
            options={'verbose_name_plural': 'Áreas de ocorrências'},
        ),
        migrations.AlterModelOptions(
            name='area_prevencao',
            options={'verbose_name_plural': 'Áreas de prevenção'},
        ),
        migrations.AlterModelOptions(
            name='bairro_ocorrencia',
            options={'verbose_name_plural': 'Bairros de ocorrências'},
        ),
        migrations.AlterModelOptions(
            name='bairro_prevencao',
            options={'verbose_name_plural': 'Bairros de prevenções'},
        ),
        migrations.AlterModelOptions(
            name='cargo_funcao',
            options={'verbose_name_plural': 'Cargos/funções'},
        ),
        migrations.AlterModelOptions(
            name='cidade_natal',
            options={'verbose_name_plural': 'Cidades onde residem militar(es)'},
        ),
        migrations.AlterModelOptions(
            name='cidade_prevencao',
            options={'verbose_name_plural': 'Cidades de prevenções'},
        ),
        migrations.AlterModelOptions(
            name='cidade_quartel',
            options={'verbose_name_plural': 'Cidades onde existe quartel'},
        ),
        migrations.AlterModelOptions(
            name='tipo_dispensa',
            options={'verbose_name_plural': 'Tipos de dispensa'},
        ),
        migrations.AlterModelOptions(
            name='tipo_prevencao',
            options={'verbose_name_plural': 'Tipos de prevenção'},
        ),
        migrations.AlterModelOptions(
            name='tipo_punicao',
            options={'verbose_name_plural': 'Tipos de punição'},
        ),
        migrations.AlterModelOptions(
            name='tipo_recompensa',
            options={'verbose_name_plural': 'Tipos de recompensa'},
        ),
    ]
