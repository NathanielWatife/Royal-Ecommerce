# Generated by Django 5.0.1 on 2024-01-18 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_contactus_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='phone',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='subject',
            field=models.CharField(max_length=255),
        ),
    ]
