# Generated by Django 4.1.2 on 2022-12-06 17:53

from django.db import migrations
import reglementations.models


def erase_fields(apps, schema_editor):
    BDESE_300 = apps.get_model("reglementations", "BDESE_300")
    for bdese in BDESE_300.objects.all():
        bdese.nombre_heures_stage_non_remunerees = None
        bdese.nombre_heures_stage_remunerees = None
        bdese.part_primes_non_mensuelle = None
        bdese.rapport_masse_salariale_effectif_mensuel = None
        bdese.remuneration_mensuelle_moyenne = None
        bdese.remuneration_moyenne_decembre = None
        bdese.save()


class Migration(migrations.Migration):

    dependencies = [
        (
            "reglementations",
            "0017_alter_bdese_300_categories_professionnelles_and_more",
        ),
    ]

    operations = [
        migrations.RunPython(erase_fields),
        migrations.AlterField(
            model_name="bdese_300",
            name="nombre_heures_stage_non_remunerees",
            field=reglementations.models.CategoryField(
                blank=True,
                category_type=reglementations.models.CategoryType[
                    "PROFESSIONNELLE_DETAILLEE"
                ],
                null=True,
                verbose_name="Nombre d'heures de stage non rémunérées",
            ),
        ),
        migrations.AlterField(
            model_name="bdese_300",
            name="nombre_heures_stage_remunerees",
            field=reglementations.models.CategoryField(
                blank=True,
                category_type=reglementations.models.CategoryType[
                    "PROFESSIONNELLE_DETAILLEE"
                ],
                null=True,
                verbose_name="Nombre d'heures de stage rémunérées",
            ),
        ),
        migrations.AlterField(
            model_name="bdese_300",
            name="part_primes_non_mensuelle",
            field=reglementations.models.CategoryField(
                blank=True,
                category_type=reglementations.models.CategoryType[
                    "PROFESSIONNELLE_DETAILLEE"
                ],
                null=True,
                verbose_name="Part des primes à périodicité non mensuelle dans la déclaration de salaire",
            ),
        ),
        migrations.AlterField(
            model_name="bdese_300",
            name="rapport_masse_salariale_effectif_mensuel",
            field=reglementations.models.CategoryField(
                blank=True,
                category_type=reglementations.models.CategoryType[
                    "PROFESSIONNELLE_DETAILLEE"
                ],
                help_text="Masse salariale annuelle totale, au sens de la déclaration annuelle de salaire",
                null=True,
                verbose_name="Rapport entre la masse salariale annuelle et l'effectif mensuel moyen",
            ),
        ),
        migrations.AlterField(
            model_name="bdese_300",
            name="remuneration_mensuelle_moyenne",
            field=reglementations.models.CategoryField(
                blank=True,
                category_type=reglementations.models.CategoryType[
                    "PROFESSIONNELLE_DETAILLEE"
                ],
                null=True,
                verbose_name="Rémunération mensuelle moyenne",
            ),
        ),
        migrations.AlterField(
            model_name="bdese_300",
            name="remuneration_moyenne_decembre",
            field=reglementations.models.CategoryField(
                blank=True,
                category_type=reglementations.models.CategoryType[
                    "PROFESSIONNELLE_DETAILLEE"
                ],
                help_text="base 35 heures",
                null=True,
                verbose_name="Rémunération moyenne du mois de décembre (effectif permanent) hors primes à périodicité non mensuelle",
            ),
        ),
    ]
