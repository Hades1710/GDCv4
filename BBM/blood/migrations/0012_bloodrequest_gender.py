# Generated by Django 5.1.7 on 2025-03-30 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blood', '0011_bloodrequest_specially_abled'),
    ]

    operations = [
        migrations.AddField(
            model_name='bloodrequest',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female')], default='male', max_length=6),
        ),
    ]
