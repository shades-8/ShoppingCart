# Generated by Django 3.0.5 on 2020-05-11 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='prod_date',
            field=models.DateField(auto_now=True),
        ),
    ]
