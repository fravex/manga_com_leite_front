# Generated by Django 4.0.4 on 2022-04-22 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BigtableNomes',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('id_principal', models.IntegerField()),
                ('nome', models.CharField(max_length=250)),
                ('tipo_origem', models.IntegerField()),
            ],
            options={
                'db_table': 'bigtable_nomes',
                'managed': True,
            },
        ),
    ]
