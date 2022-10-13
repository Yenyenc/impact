# Generated by Django 4.1.2 on 2022-10-13 08:51

from django.db import migrations, models
import django.forms.fields
import public.models


class Migration(migrations.Migration):

    dependencies = [
        ("public", "0015_bdese_accidents_femme_bdese_accidents_homme_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="bdese",
            name="experiences_transformation_organisation_travail",
            field=models.TextField(
                blank=True,
                help_text="Pour l'explication de ces expériences d'amélioration du contenu du travail, donner le nombre de salariés concernés.",
                null=True,
                verbose_name="Expériences de transformation de l'organisation du travail en vue d'en améliorer le contenu",
            ),
        ),
        migrations.AddField(
            model_name="bdese",
            name="montant_depenses_amelioration_conditions_travail",
            field=models.IntegerField(
                blank=True,
                help_text="Non compris l'évaluation des dépenses en matière de santé et de sécurité.",
                null=True,
                verbose_name="Montant des dépenses consacrées à l'amélioration des conditions de travail dans l'entreprise",
            ),
        ),
        migrations.AddField(
            model_name="bdese",
            name="nombre_examens_medicaux",
            field=public.models.CategoryField(
                base_field=django.forms.fields.IntegerField,
                blank=True,
                categories=["soumis à surveillance", "autres"],
                null=True,
                verbose_name="Nombre d'examens médicaux des travailleurs",
            ),
        ),
        migrations.AddField(
            model_name="bdese",
            name="nombre_salaries_inaptes",
            field=models.IntegerField(
                blank=True,
                help_text="Nombre de salariés déclarés définitivement inaptes à leur emploi par le médecin du travail",
                null=True,
                verbose_name="Nombre de salariés inaptes",
            ),
        ),
        migrations.AddField(
            model_name="bdese",
            name="nombre_salaries_reclasses",
            field=models.IntegerField(
                blank=True,
                help_text="Nombre de salariés reclassés dans l'entreprise à la suite d'une inaptitude",
                null=True,
                verbose_name="Nombre de salariés reclassés",
            ),
        ),
        migrations.AddField(
            model_name="bdese",
            name="nombre_visites_medicales",
            field=public.models.CategoryField(
                base_field=django.forms.fields.IntegerField,
                blank=True,
                categories=["droit commun", "individuel renforcé"],
                help_text="selon le type de suivi",
                null=True,
                verbose_name="Nombre de visites d'information et de prévention des travailleurs",
            ),
        ),
        migrations.AddField(
            model_name="bdese",
            name="pourcentage_temps_medecin_du_travail",
            field=public.models.CategoryField(
                base_field=django.forms.fields.IntegerField,
                blank=True,
                categories=["analyse", "intervention"],
                null=True,
                verbose_name="Part du temps consacré par le médecin du travail en milieu de travail",
            ),
        ),
        migrations.AddField(
            model_name="bdese",
            name="taux_realisation_programme_amelioration_conditions_travail",
            field=models.IntegerField(
                blank=True,
                null=True,
                verbose_name="Taux de réalisation du programme d'amélioration des conditions de travail dans l'entreprise l'année précédente",
            ),
        ),
    ]
