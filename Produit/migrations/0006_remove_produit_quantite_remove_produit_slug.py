# Generated by Django 4.1 on 2022-08-26 16:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Produit', '0005_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produit',
            name='quantite',
        ),
        migrations.RemoveField(
            model_name='produit',
            name='slug',
        ),
    ]