# Generated by Django 5.0.2 on 2024-02-16 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_pontoturistico_atracao_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pontoturistico',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='pontos_turisticos'),
        ),
    ]
