# Generated by Django 3.1.7 on 2021-10-01 18:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0013_auto_20211001_2358'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orders',
            old_name='Order_id',
            new_name='order_id',
        ),
    ]