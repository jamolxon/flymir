# Generated by Django 5.1.3 on 2024-12-13 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consulting', '0007_program_alter_student_university_delete_programs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='program',
            name='slug',
            field=models.SlugField(blank=True, max_length=256, null=True, unique=True, verbose_name='slug'),
        ),
    ]
