# Generated by Django 3.1.7 on 2021-04-14 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('investments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='investmentinfo',
            name='intrest_payout',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='investmentinfo',
            name='maturity_date',
            field=models.DateField(auto_now=True),
        ),
    ]
