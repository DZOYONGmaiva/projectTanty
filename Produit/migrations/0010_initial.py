# Generated by Django 4.1 on 2022-09-07 14:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Gamme', '0004_remove_gamme_produits'),
        ('Produit', '0009_delete_produit'),
    ]

    operations = [
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('prix', models.FloatField(default=0.0)),
                ('description', models.TextField(blank=True)),
                ('image', models.ImageField(upload_to='produits')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('gamme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gamme.gamme')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]