# Generated by Django 3.2.4 on 2021-07-31 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('investments', '0002_auto_20210414_0952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investmentinfo',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='schemerates',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='schemes',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
