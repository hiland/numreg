# Generated by Django 2.0.7 on 2018-07-12 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('number_registry', '0004_auto_20180711_2107'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='famous',
            field=models.BooleanField(default=False),
        ),
    ]
