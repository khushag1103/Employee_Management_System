# Generated by Django 4.2 on 2023-04-15 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='id',
            field=models.UUIDField(primary_key=True, serialize=False),
        ),
    ]