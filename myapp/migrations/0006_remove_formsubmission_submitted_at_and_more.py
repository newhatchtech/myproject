# Generated by Django 5.1.4 on 2025-01-29 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_formsubmission_delete_multistepformdata'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='formsubmission',
            name='submitted_at',
        ),
        migrations.AlterField(
            model_name='formsubmission',
            name='first_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='formsubmission',
            name='investment',
            field=models.CharField(choices=[('less_than_5000', 'Less than $5,000'), ('5000_10000', '$5,000 - $10,000'), ('10000_20000', '$10,000 - $20,000'), ('21000_40000', '$21,000 - $40,000'), ('40000_80000', '$40,000 - $80,000'), ('80000_100000', '$80,000 - $100,000'), ('100000_150000', '$100,000 - $150,000'), ('150000_up', '$150,000 and up')], max_length=20),
        ),
        migrations.AlterField(
            model_name='formsubmission',
            name='last_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='formsubmission',
            name='payment',
            field=models.CharField(choices=[('credit_debit_card', 'Credit Card/Debit Card'), ('btc_crypto', 'BTC/Crypto'), ('wire_transfer', 'Wire Transfer'), ('money_gram_wu', 'Money Gram/Western Union'), ('cash', 'Cash'), ('other', 'Other')], max_length=20),
        ),
    ]
