# Generated by Django 4.0.2 on 2022-11-11 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlineapp', '0006_auto_20221108_1438'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='check',
            new_name='checkans',
        ),
        migrations.AlterField(
            model_name='assignment',
            name='subject',
            field=models.CharField(choices=[('MATHS', 'MATHS'), ('CHEMISTRY', 'CHEMISTRY'), ('PHYSICS', 'PHISICS')], max_length=50),
        ),
        migrations.AlterField(
            model_name='teacherdata',
            name='subject',
            field=models.CharField(choices=[('MATHS', 'MATHS'), ('CHEMISTRY', 'CHEMISTRY'), ('PHYSICS', 'PHISICS')], max_length=20),
        ),
    ]
