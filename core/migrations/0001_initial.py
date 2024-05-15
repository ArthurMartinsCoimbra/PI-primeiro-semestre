# Generated by Django 5.0.3 on 2024-03-28 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lote',
            fields=[
                ('Nome', models.CharField(max_length=100, verbose_name='Nome do produto')),
                ('Quantidade', models.DecimalField(decimal_places=0, max_digits=8, verbose_name='Quantidade no Lote')),
                ('Nlote', models.CharField(max_length=40, primary_key=True, serialize=False, verbose_name='Numero do Lote')),
                ('Validade', models.DateField(verbose_name='Validade')),
            ],
        ),
    ]