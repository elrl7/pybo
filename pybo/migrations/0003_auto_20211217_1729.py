# Generated by Django 3.1.3 on 2021-12-17 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0002_auto_20211215_1743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='update_date',
            field=models.DateTimeField(null=True),
        ),
    ]
