# Generated by Django 3.2.7 on 2021-10-28 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kutipan_penyemangat', '0002_alter_quotes_quotes_form'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quotes',
            name='name',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='quotes',
            name='quotes_form',
            field=models.TextField(),
        ),
    ]
