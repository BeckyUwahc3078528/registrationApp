# Generated by Django 5.0.2 on 2024-08-29 15:33

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_alter_module_course'),
        ('users', '0003_profile_registered_modules'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enrollment_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.module')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.profile')),
            ],
        ),
    ]
