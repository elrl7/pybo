# Generated by Django 3.1.3 on 2021-12-15 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='company_address',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='company',
            name='company_note',
            field=models.TextField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='company_telno',
            field=models.CharField(max_length=50),
        ),
    ]
