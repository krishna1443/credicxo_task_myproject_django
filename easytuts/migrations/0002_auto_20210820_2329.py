# Generated by Django 3.2.6 on 2021-08-20 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('easytuts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='created_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='updated_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='created_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='updated_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]