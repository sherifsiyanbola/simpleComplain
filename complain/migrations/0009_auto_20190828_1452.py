# Generated by Django 2.2.4 on 2019-08-28 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complain', '0008_auto_20190826_2134'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='complain',
            name='title',
        ),
        migrations.AlterField(
            model_name='complain',
            name='complaintitle',
            field=models.CharField(max_length=100),
        ),
    ]
