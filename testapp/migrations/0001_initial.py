# Generated by Django 4.1.2 on 2023-12-14 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='carModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carname', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
            ],
        ),
    ]
