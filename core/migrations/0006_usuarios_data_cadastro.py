# Generated by Django 4.2.5 on 2023-10-01 05:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_clientes_alter_usuarios_permissao'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuarios',
            name='data_cadastro',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
