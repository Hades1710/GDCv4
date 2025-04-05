# Generated by Django 3.0.5 on 2025-03-26 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0003_patient_student_background'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='student_background',
            field=models.CharField(blank=True, choices=[('orphaned', 'Orphaned or abandoned children'), ('single_parent', 'Children from single-parent households'), ('low_income', 'Students from low-income families'), ('disabilities', 'Students with disabilities'), ('first_gen', 'First-generation learners'), ('refugee', 'Refugee or displaced students'), ('rural_tribal', 'Students from rural or tribal areas'), ('female', 'Female students'), ('disaster', 'Affected by natural disasters or conflicts')], max_length=20, null=True),
        ),
    ]
