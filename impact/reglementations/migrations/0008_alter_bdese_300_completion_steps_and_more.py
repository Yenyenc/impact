# Generated by Django 4.1.2 on 2022-12-01 09:23

from django.db import migrations, models
import django.db.models.fields
import reglementations.models


class Migration(migrations.Migration):

    dependencies = [
        ("reglementations", "0007_remove_bdese_300_complement_salaire_conge_and_more"),
    ]

    operations = [
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
        migrations.AlterField(
            model_name="bdese_300",
            name="existence_orga_facilitant_vie_familiale_et_professionnelle",
            field=models.TextField(
                blank=True,
                null=True,
                verbose_name="Existence de formules d'organisation du travail facilitant l'articulation de la vie familiale et de la vie professionnelle",
            ),
        ),
    ]