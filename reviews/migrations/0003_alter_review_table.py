# Generated by Django 4.2.3 on 2023-07-11 20:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_review_email_review_rating'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='review',
            table='review_table',
        ),
    ]
