# Generated by Django 3.2.8 on 2021-10-26 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0003_rename_students_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='isbn',
            field=models.CharField(blank=True, max_length=42, null=True),
        ),
    ]