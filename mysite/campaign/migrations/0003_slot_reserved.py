# Generated by Django 5.0.6 on 2024-06-24 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaign', '0002_slot'),
    ]

    operations = [
        migrations.AddField(
            model_name='slot',
            name='reserved',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
