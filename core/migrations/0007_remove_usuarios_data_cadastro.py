# Generated by Django 4.2.5 on 2023-10-01 06:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_usuarios_data_cadastro'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuarios',
            name='data_cadastro',
        ),
    ]
