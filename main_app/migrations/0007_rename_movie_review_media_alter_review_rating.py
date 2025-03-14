# Generated by Django 4.2.19 on 2025-03-06 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_review'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='movie',
            new_name='media',
        ),
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.IntegerField(blank=True, choices=[(1, '1 - Poor'), (2, '2 - Fair'), (3, '3 - Good'), (4, '4 - Very Good'), (5, '5 - Excellent')], null=True),
        ),
    ]
