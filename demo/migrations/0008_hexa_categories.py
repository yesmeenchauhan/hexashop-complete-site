# Generated by Django 4.2.4 on 2023-09-02 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0007_subscribe'),
    ]

    operations = [
        migrations.AddField(
            model_name='hexa',
            name='categories',
            field=models.CharField(default=1, max_length=390),
            preserve_default=False,
        ),
    ]
