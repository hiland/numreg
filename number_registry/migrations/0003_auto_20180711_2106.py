# Generated by Django 2.0.7 on 2018-07-12 04:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('number_registry', '0002_entry2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry2',
            name='owner',
        ),
        migrations.DeleteModel(
            name='Entry2',
        ),
    ]