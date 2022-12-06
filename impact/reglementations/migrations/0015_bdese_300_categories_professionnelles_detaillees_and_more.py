# Generated by Django 4.1.2 on 2022-12-01 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("reglementations", "0014_alter_bdese_300_part_primes_non_mensuelle"),
    ]

    operations = [
        migrations.AddField(
            model_name="bdese_300",
            name="categories_professionnelles_detaillees",
            field=models.JSONField(
                blank=True,
                help_text="Une structure de qualification détaillée en cinq postes minimum",
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="bdese_300",
            name="categories_professionnelles",
            field=models.JSONField(
                blank=True,
                help_text="Une structure de qualification détaillée en trois postes minimum",
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="bdese_50_300",
            name="categories_professionnelles",
            field=models.JSONField(
                blank=True,
                help_text="Une structure de qualification détaillée en trois postes minimum",
                null=True,
            ),
        ),
    ]