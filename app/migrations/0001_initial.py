# Generated by Django 4.2.2 on 2023-06-07 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('Ename', models.CharField(max_length=100)),
                ('Eid', models.IntegerField(primary_key=True, serialize=False)),
                ('Eage', models.IntegerField()),
            ],
        ),
    ]
