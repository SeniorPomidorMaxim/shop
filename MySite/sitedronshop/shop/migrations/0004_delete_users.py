# Generated by Django 4.2.6 on 2023-10-26 06:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_alter_users_email_alter_users_password'),
    ]

    operations = [
        migrations.DeleteModel(
            name='users',
        ),
    ]
