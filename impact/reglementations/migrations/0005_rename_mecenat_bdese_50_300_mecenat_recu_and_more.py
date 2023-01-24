# Generated by Django 4.1.5 on 2023-01-23 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reglementations', '0004_bdese_50_300_completion_steps'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bdese_50_300',
            old_name='mecenat',
            new_name='mecenat_recu',
        ),
        migrations.AddField(
            model_name='bdese_50_300',
            name='mecenat_verse',
            field=models.IntegerField(blank=True, null=True, verbose_name='Mécénat'),
        ),
    ]