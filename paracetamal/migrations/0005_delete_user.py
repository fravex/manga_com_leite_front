# Generated by Django 4.0.4 on 2022-04-26 22:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('paracetamal', '0004_user_date_joined_user_email_user_is_active_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
