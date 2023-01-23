# Generated by Django 4.1.5 on 2023-01-24 11:06

from django.db import migrations, models
import reglementations.models


class Migration(migrations.Migration):

    dependencies = [
        ("reglementations", "0002_alter_bdese_300_annee_alter_bdese_50_300_annee"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bdese_300",
            name="nombre_unites_absence",
            field=reglementations.models.CategoryField(
                blank=True,
                category_type=reglementations.models.CategoryType["PROFESSIONNELLE"],
                help_text="Ne sont pas comptés parmi les absences : les diverses sortes de congés, les conflits et le service national.",
                null=True,
                verbose_name="Nombre d'unités d'absence",
            ),
        ),
        migrations.AlterField(
            model_name="bdese_300",
            name="nombre_unites_absence_accidents",
            field=reglementations.models.CategoryField(
                blank=True,
                category_type=reglementations.models.CategoryType["PROFESSIONNELLE"],
                null=True,
                verbose_name="Nombre d'unités d'absence pour accidents du travail et de trajet ou maladies professionnelles",
            ),
        ),
        migrations.AlterField(
            model_name="bdese_300",
            name="nombre_unites_absence_autres",
            field=reglementations.models.CategoryField(
                blank=True,
                category_type=reglementations.models.CategoryType["PROFESSIONNELLE"],
                null=True,
                verbose_name="Nombre d'unités d'absence imputables à d'autres causes",
            ),
        ),
        migrations.AlterField(
            model_name="bdese_300",
            name="nombre_unites_absence_conges_autorises",
            field=reglementations.models.CategoryField(
                blank=True,
                category_type=reglementations.models.CategoryType["PROFESSIONNELLE"],
                help_text="(événements familiaux, congés spéciaux pour les femmes …)",
                null=True,
                verbose_name="Nombre d'unités d'absence pour congés autorisés",
            ),
        ),
        migrations.AlterField(
            model_name="bdese_300",
            name="nombre_unites_absence_maladie",
            field=reglementations.models.CategoryField(
                blank=True,
                category_type=reglementations.models.CategoryType["PROFESSIONNELLE"],
                null=True,
                verbose_name="Nombre d'unités d'absence pour maladie",
            ),
        ),
        migrations.AlterField(
            model_name="bdese_300",
            name="nombre_unites_absence_maternite",
            field=reglementations.models.CategoryField(
                blank=True,
                category_type=reglementations.models.CategoryType["PROFESSIONNELLE"],
                null=True,
                verbose_name="Nombre d'unités d'absence pour maternité",
            ),
        ),
        migrations.AlterField(
            model_name="bdese_300",
            name="nombre_unites_theoriques_travaillees",
            field=models.IntegerField(
                blank=True,
                null=True,
                verbose_name="Nombre d'unités théoriques travaillées",
            ),
        ),
        migrations.AlterField(
            model_name="bdese_300",
            name="unite_absenteisme",
            field=models.CharField(
                choices=[("J", "Journées"), ("1/2J", "1/2 journées"), ("H", "Heures")],
                default="J",
                help_text="Possibilité de comptabiliser tous les indicateurs de la rubrique absentéisme, au choix, en journées, 1/2 journées ou heures.",
                max_length=10,
                verbose_name="Unité choisie pour la catégorie absentéisme",
            ),
        ),
    ]