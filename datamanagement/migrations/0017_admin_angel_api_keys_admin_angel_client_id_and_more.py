# Generated by Django 4.2.6 on 2023-10-31 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datamanagement', '0016_admin_expiry_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='admin',
            name='angel_api_keys',
            field=models.CharField(default='NONE', max_length=100),
        ),
        migrations.AddField(
            model_name='admin',
            name='angel_client_id',
            field=models.CharField(default='NONE', max_length=10),
        ),
        migrations.AddField(
            model_name='admin',
            name='angel_password',
            field=models.CharField(default='NONE', max_length=100),
        ),
        migrations.AddField(
            model_name='admin',
            name='angel_token',
            field=models.CharField(default='NONE', max_length=100),
        ),
    ]