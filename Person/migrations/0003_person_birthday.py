# Generated by Django 4.0.4 on 2022-05-02 03:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Person', '0002_person_date_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='birthday',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
