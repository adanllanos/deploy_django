# Generated by Django 4.1.1 on 2023-05-22 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyecto', '0009_alter_vender_laptop_modelo'),
    ]

    operations = [
        migrations.CreateModel(
            name='crear_factura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('modelo', models.CharField(max_length=20)),
                ('cantidad', models.IntegerField()),
                ('precio', models.IntegerField()),
                ('fecha', models.DateField()),
                ('ci', models.IntegerField()),
                ('nroDeFact', models.IntegerField()),
            ],
        ),
    ]