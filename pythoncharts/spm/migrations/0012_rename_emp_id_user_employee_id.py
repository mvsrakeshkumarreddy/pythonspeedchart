# Generated by Django 4.0.5 on 2022-06-16 11:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spm', '0011_rename_crewid_user_crew_id_rename_empid_user_emp_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='emp_ID',
            new_name='employee_ID',
        ),
    ]