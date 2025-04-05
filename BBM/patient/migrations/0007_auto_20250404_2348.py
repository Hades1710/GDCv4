# Generated by Django 3.0.5 on 2025-04-04 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0006_remove_patient_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='latitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='location_name',
            field=models.CharField(blank=True, help_text='Name of the location', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='longitude',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
