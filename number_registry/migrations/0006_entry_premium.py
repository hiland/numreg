# Generated by Django 2.0.7 on 2018-07-12 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('number_registry', '0005_entry_famous'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='premium',
            field=models.BooleanField(default=False),
        ),
    ]
