# Generated by Django 4.1.7 on 2023-03-09 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_company_information_company_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='description',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
