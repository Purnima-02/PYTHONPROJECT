# Generated by Django 5.0.7 on 2024-11-11 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0004_businessloan_expiry_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='busbasicdetailform',
            name='expiry_at',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='busbasicdetailform',
            name='phone_number',
            field=models.BigIntegerField(),
        ),
    ]
