# Generated by Django 3.2.9 on 2022-02-20 17:50

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0008_alter_course_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='code',
            field=models.CharField(blank=True, default=uuid.uuid4, max_length=100, unique=True),
        ),
    ]
