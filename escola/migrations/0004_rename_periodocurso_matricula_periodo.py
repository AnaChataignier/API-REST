# Generated by Django 4.2.3 on 2023-08-16 18:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0003_rename_periodo_matricula_periodocurso'),
    ]

    operations = [
        migrations.RenameField(
            model_name='matricula',
            old_name='periodocurso',
            new_name='periodo',
        ),
    ]
