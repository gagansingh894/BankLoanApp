# Generated by Django 3.0.7 on 2020-06-10 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='home_ownership',
            field=models.CharField(choices=[('Home Mortgage', 'Home Mortgage'), ('Own Home', 'Own Home'), ('Rent', 'Rent'), ('HaveMortgage', 'HaveMortgage')], max_length=30),
        ),
    ]
