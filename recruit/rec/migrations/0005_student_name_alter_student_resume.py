# Generated by Django 5.0.4 on 2024-06-04 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rec', '0004_remove_facilitator_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='name',
            field=models.CharField(default='abc', max_length=254),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='student',
            name='resume',
            field=models.FileField(blank=True, null=True, upload_to='resumes/'),
        ),
    ]
