# Generated by Django 2.2.4 on 2019-08-26 20:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('complain', '0002_auto_20190826_1925'),
    ]

    operations = [
        migrations.RenameField(
            model_name='complain',
            old_name='manager',
            new_name='customer',
        ),
    ]
