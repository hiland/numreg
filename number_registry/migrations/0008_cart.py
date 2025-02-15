# Generated by Django 2.0.7 on 2018-07-17 20:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import number_registry.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('number_registry', '0007_auto_20180717_0954'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desiredname', models.CharField(max_length=100, validators=[number_registry.models.validateUniqueName])),
                ('desirednumber', models.BigIntegerField(validators=[number_registry.models.validate_div3, number_registry.models.validateUniqueNumber])),
                ('desiredcomment', models.TextField(blank=True)),
                ('desireddedication', models.CharField(blank=True, max_length=100)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
