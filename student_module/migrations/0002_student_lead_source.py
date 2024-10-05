# Generated by Django 4.2.16 on 2024-10-02 03:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('setting_module', '0001_initial'),
        ('student_module', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='lead_source',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='students', to='setting_module.leadsource'),
        ),
    ]
