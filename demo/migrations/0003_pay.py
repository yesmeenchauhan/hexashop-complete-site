# Generated by Django 4.2.4 on 2023-08-24 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0002_alter_hexa_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='pay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('streetaddress', models.CharField(max_length=200)),
                ('streetaddressline2', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=10)),
                ('zipcode', models.CharField(max_length=10)),
            ],
        ),
    ]
