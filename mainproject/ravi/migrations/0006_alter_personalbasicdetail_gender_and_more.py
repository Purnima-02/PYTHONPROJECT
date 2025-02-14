# Generated by Django 5.0.7 on 2024-11-06 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ravi', '0005_alter_homeapplication_applicant_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personalbasicdetail',
            name='gender',
            field=models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='personalbasicdetail',
            name='marital_status',
            field=models.CharField(blank=True, choices=[('Single', 'Single'), ('Married', 'Married'), ('Divorced', 'Divorced')], max_length=10, null=True),
        ),
    ]
