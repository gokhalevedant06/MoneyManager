# Generated by Django 3.1.7 on 2021-04-12 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExpenseChoices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Electricity Bill', 'Electricity Bill'), ('Groceries', 'Groceries'), ('Shopping', 'Shopping'), ('Rent', 'Rent'), ('Loan', 'Loan'), ('Fitness', 'Fitness'), ('Transport', 'Transport')], max_length=100)),
                ('percent', models.IntegerField()),
            ],
        ),
    ]
