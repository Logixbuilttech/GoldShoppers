# Generated by Django 4.1.7 on 2023-03-07 06:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_vendors_username_alter_vendors_company_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vendors',
            name='contact',
        ),
        migrations.RemoveField(
            model_name='vendors',
            name='email',
        ),
    ]
