# Generated by Django 2.2.4 on 2019-08-26 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complain', '0003_auto_20190826_2022'),
    ]

    operations = [
        migrations.AddField(
            model_name='complain',
            name='treated',
            field=models.CharField(choices=[('y', 'Yes'), ('n', 'No')], max_length=50, null=True),
        ),
    ]
