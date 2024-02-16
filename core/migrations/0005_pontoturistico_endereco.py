# Generated by Django 5.0.2 on 2024-02-16 03:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_pontoturistico_avaliacoes_pontoturistico_comentarios'),
        ('enderecos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pontoturistico',
            name='endereco',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='enderecos.endereco'),
            preserve_default=False,
        ),
    ]