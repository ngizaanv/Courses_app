# Generated by Django 4.0.3 on 2022-06-12 16:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('itcourse', '0002_remove_course_contacts_course_contacts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='type',
            field=models.IntegerField(choices=[(1, 'Phone'), (2, 'Facebook'), (3, 'Email')]),
        ),
        migrations.RemoveField(
            model_name='course',
            name='contacts',
        ),
        migrations.AddField(
            model_name='course',
            name='contacts',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='itcourse.contact'),
        ),
    ]
