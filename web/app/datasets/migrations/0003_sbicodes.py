# Generated by Django 2.0.2 on 2018-03-05 10:35

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datasets', '0002_handelsregister'),
    ]

    operations = [
        migrations.CreateModel(
            name='SBIcodes',
            fields=[
                ('code', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('title', models.TextField()),
                ('sbi_tree', django.contrib.postgres.fields.jsonb.JSONField()),
                ('qa_tree', django.contrib.postgres.fields.jsonb.JSONField(null=True)),
            ],
        ),
    ]
