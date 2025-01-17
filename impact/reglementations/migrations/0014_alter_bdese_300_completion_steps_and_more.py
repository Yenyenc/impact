# Generated by Django 4.1.6 on 2023-02-15 16:48
import django.db.models.fields
from django.db import migrations

import reglementations.models


def rename_categories_professionnelles_step_to_configuration(apps, schema_editor):
    BDESE_50_300 = apps.get_model("reglementations", "BDESE_50_300")
    for bdese in BDESE_50_300.objects.all():
        bdese.completion_steps["Configuration"] = bdese.completion_steps.pop(
            "Catégories professionnelles", False
        )
        bdese.save()
    BDESE_300 = apps.get_model("reglementations", "BDESE_300")
    for bdese in BDESE_300.objects.all():
        # La configuration n'est jamais terminée même si les catégories professionnelles l'étaient
        # car les niveaux ou coefficients hiérarchiques y ont été ajoutés
        bdese.completion_steps["Configuration"] = False
        bdese.completion_steps.pop("Catégories professionnelles", None)
        bdese.save()


class Migration(migrations.Migration):

    dependencies = [
        (
            "reglementations",
            "0013_bdese_300_age_moyen_par_niveau_hierarchique_femme_and_more",
        ),
    ]

    operations = [
        migrations.RunPython(
            rename_categories_professionnelles_step_to_configuration,
            reverse_code=migrations.RunPython.noop,
            hints={"db_migration": "default"},
        ),
        migrations.AlterField(
            model_name="bdese_300",
            name="completion_steps",
            field=reglementations.models.CategoryField(
                base_field=django.db.models.fields.BooleanField,
                categories=[
                    "Configuration",
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
                ],
                default=reglementations.models.bdese_300_completion_steps_default,
            ),
        ),
        migrations.AlterField(
            model_name="bdese_50_300",
            name="completion_steps",
            field=reglementations.models.CategoryField(
                base_field=django.db.models.fields.BooleanField,
                categories=[
                    "Configuration",
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
                ],
                default=reglementations.models.bdese_50_300_completion_steps_default,
            ),
        ),
    ]
