# Generated by Django 4.1.2 on 2022-11-22 11:13

from django.db import migrations, models
import django.db.models.fields
import reglementations.models


class Migration(migrations.Migration):

    dependencies = [
        ("reglementations", "0005_alter_bdese_300_completion_steps"),
    ]

    operations = [
        migrations.AddField(
            model_name="bdese_300",
            name="categories_professionnelles",
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="bdese_50_300",
            name="categories_professionnelles",
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="bdese_300",
            name="completion_steps",
            field=reglementations.models.CategoryField(
                base_field=django.db.models.fields.BooleanField,
                categories=(
                    "Investissement social",
                    "Investissement matériel et immatériel",
                    "Egalité professionnelle homme/femme",
                    "Fonds propres, endettement et impôts",
                    "Rémunérations",
                    "Représentation du personnel et Activités sociales et culturelles",
                    "Rémunération des financeurs",
                    "Flux financiers",
                    "Partenariats",
                    "Transferts commerciaux et financiers",
                    "Environnement",
                ),
                default=reglementations.models.bdese_300_completion_steps_default,
            ),
        ),
    ]