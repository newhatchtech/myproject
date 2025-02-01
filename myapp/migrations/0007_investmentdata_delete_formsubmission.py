# Generated by Django 5.1.4 on 2025-01-29 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_remove_formsubmission_submitted_at_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='InvestmentData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('investment_amount', models.CharField(max_length=50)),
                ('payment_method', models.CharField(max_length=50)),
                ('additional_info', models.TextField(blank=True, null=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='FormSubmission',
        ),
    ]
