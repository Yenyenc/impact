# Generated by Django 4.1.2 on 2022-10-13 12:34

from django.db import migrations
import django.forms.fields
import public.models


class Migration(migrations.Migration):

    dependencies = [
        ("public", "0019_bdese_evolution_salariale_par_categorie_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bdese",
            name="salaire_base_minimum_par_categorie",
            field=public.models.CategoryField(
                base_field=django.forms.fields.IntegerField,
                blank=True,
                null=True,
                verbose_name="Salaire de base minimum par catégorie",
            ),
        ),
        migrations.AlterField(
            model_name="bdese",
            name="salaire_base_minimum_par_sexe",
            field=public.models.CategoryField(
                base_field=django.forms.fields.IntegerField,
                blank=True,
                categories=["homme", "femme"],
                null=True,
                verbose_name="Salaire de base minimum par sexe",
            ),
        ),
        migrations.AlterField(
            model_name="bdese",
            name="salaire_median_par_categorie",
            field=public.models.CategoryField(
                base_field=django.forms.fields.IntegerField,
                blank=True,
                null=True,
                verbose_name="Salaire médian par catégorie",
            ),
        ),
        migrations.AlterField(
            model_name="bdese",
            name="salaire_median_par_sexe",
            field=public.models.CategoryField(
                base_field=django.forms.fields.IntegerField,
                blank=True,
                categories=["homme", "femme"],
                null=True,
                verbose_name="Salaire médian par sexe",
            ),
        ),
        migrations.AlterField(
            model_name="bdese",
            name="salaire_moyen_par_categorie",
            field=public.models.CategoryField(
                base_field=django.forms.fields.IntegerField,
                blank=True,
                null=True,
                verbose_name="Salaire moyen par catégorie",
            ),
        ),
    ]