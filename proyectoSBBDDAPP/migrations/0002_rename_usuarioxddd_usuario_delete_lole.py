# Generated by Django 4.1.5 on 2023-02-25 00:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proyectoSBBDDAPP', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='usuarioXDDD',
            new_name='usuario',
        ),
        migrations.DeleteModel(
            name='lole',
        ),
    ]