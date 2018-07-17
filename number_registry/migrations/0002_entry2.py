# Generated by Django 2.0.7 on 2018-07-12 04:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import number_registry.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('number_registry', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entry2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('number', models.BigIntegerField(validators=[number_registry.models.validate_div3])),
                ('comment', models.TextField(blank=True)),
                ('dedicaition', models.CharField(blank=True, max_length=100)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]