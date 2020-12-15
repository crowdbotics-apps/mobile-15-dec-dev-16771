# Generated by Django 2.2.17 on 2020-12-15 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_load_initial_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='first_name_of_student',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='last_name_of_student',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='long_title_with_input_field',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=models.TextField(blank=True),
        ),
    ]