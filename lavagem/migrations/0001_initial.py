# Generated by Django 4.1.7 on 2023-02-24 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lavagem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('tel', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=50)),
            ],
        ),
    ]
