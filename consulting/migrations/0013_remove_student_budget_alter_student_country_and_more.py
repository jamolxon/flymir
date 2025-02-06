# Generated by Django 5.1.3 on 2025-02-06 00:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consulting', '0012_alter_studentcomment_student'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='budget',
        ),
        migrations.AlterField(
            model_name='student',
            name='country',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='students', to='consulting.subcategory', verbose_name='country'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='student',
            name='university',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='students', to='consulting.program', verbose_name='university'),
            preserve_default=False,
        ),
    ]
