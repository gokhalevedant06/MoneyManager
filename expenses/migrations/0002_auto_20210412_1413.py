# Generated by Django 3.1.7 on 2021-04-12 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExpenseData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expense_name', models.CharField(max_length=100)),
                ('expense_amount', models.IntegerField()),
                ('remaining_amount', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='ExpenseChoices',
        ),
    ]