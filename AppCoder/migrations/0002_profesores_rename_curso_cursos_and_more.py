# Generated by Django 4.0.5 on 2022-07-04 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profesores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('profesion', models.CharField(max_length=30)),
                ('salario', models.IntegerField()),
            ],
        ),
        migrations.RenameModel(
            old_name='Curso',
            new_name='cursos',
        ),
        migrations.RenameModel(
            old_name='Entregable',
            new_name='entregables',
        ),
        migrations.RenameModel(
            old_name='Estudiante',
            new_name='estudiantes',
        ),
        migrations.DeleteModel(
            name='Profesor',
        ),
    ]
