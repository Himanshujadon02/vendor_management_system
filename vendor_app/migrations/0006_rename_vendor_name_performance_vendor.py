# Generated by Django 5.0.3 on 2024-05-01 10:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendor_app', '0005_rename_vendor_code_performance_vendor_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='performance',
            old_name='vendor_name',
            new_name='vendor',
        ),
    ]
