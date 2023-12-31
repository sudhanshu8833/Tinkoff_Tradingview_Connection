# Generated by Django 4.2.7 on 2023-12-16 04:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datamanagement', '0021_admin_live'),
    ]

    operations = [
        migrations.RenameField(
            model_name='admin',
            old_name='oanda_account_id',
            new_name='tinkoff_token',
        ),
        migrations.RemoveField(
            model_name='admin',
            name='oanda_api_keys',
        ),
        migrations.RemoveField(
            model_name='admin',
            name='precision',
        ),
        migrations.RemoveField(
            model_name='admin',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='admin',
            name='stoploss_pips',
        ),
        migrations.RemoveField(
            model_name='admin',
            name='symbol',
        ),
    ]
