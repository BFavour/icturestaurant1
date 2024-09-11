# Generated by Django 5.1 on 2024-08-23 15:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurant', '0007_commande_statut_alter_plat_disponible'),
    ]

    operations = [
        migrations.AddField(
            model_name='commande',
            name='heure_disponibilite',
            field=models.TimeField(default=datetime.time(15, 52, 14, 251541)),
        ),
        migrations.AddField(
            model_name='commande',
            name='mode_paiement',
            field=models.CharField(blank=True, choices=[('orange_money', 'Orange Money'), ('mobile_money', 'Mobile Money')], max_length=20, null=True),
        ),
    ]
