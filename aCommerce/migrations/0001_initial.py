# Generated by Django 3.1.1 on 2020-11-17 17:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200)),
                ('couleur', models.CharField(max_length=7)),
                ('prix', models.IntegerField(default=500)),
                ('description', models.TextField()),
                ('plus_info', models.TextField()),
                ('categorie', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='aCommerce.categorie')),
            ],
        ),
    ]