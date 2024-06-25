# Generated by Django 5.0.6 on 2024-06-24 06:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaign', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('start_time', models.TimeField(blank=True, null=True)),
                ('end_time', models.TimeField(blank=True, null=True)),
                ('max_capacity', models.IntegerField(blank=True, default=0, null=True)),
                ('campaign', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='campaign.campaign')),
            ],
        ),
    ]