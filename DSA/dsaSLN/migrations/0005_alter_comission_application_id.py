# Generated by Django 5.0.7 on 2024-08-26 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dsaSLN', '0004_comission'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comission',
            name='application_id',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
