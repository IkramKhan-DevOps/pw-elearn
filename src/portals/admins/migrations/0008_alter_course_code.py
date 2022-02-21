# Generated by Django 3.2.9 on 2022-02-20 17:49

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0007_course_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='code',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]
