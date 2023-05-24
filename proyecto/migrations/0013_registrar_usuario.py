# Generated by Django 4.1.1 on 2023-05-23 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyecto', '0012_delete_registrar_usuarios'),
    ]

    operations = [
        migrations.CreateModel(
            name='registrar_usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombemp', models.CharField(max_length=80, unique=True)),
                ('ciemp', models.IntegerField(unique=True)),
                ('usuario', models.CharField(max_length=10, unique=True)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
    ]