# Generated by Django 3.2.12 on 2022-03-02 04:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(help_text='enter first name', max_length=100)),
                ('middle_name', models.CharField(blank=True, help_text='enter middle name', max_length=100)),
                ('last_name', models.CharField(help_text='enter last name', max_length=100)),
                ('email', models.EmailField(help_text='enter email', max_length=100)),
                ('phone', models.CharField(help_text='enter phone number', max_length=20)),
                ('type', models.CharField(choices=[('Doctor', 'Doctor'), ('Nurse', 'Nurse')], default='Doctor', max_length=10)),
                ('license_number', models.CharField(blank=True, help_text='enter license numbers', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(help_text='enter first name', max_length=100)),
                ('last_name', models.CharField(help_text='enter last name', max_length=100)),
                ('email', models.EmailField(help_text='enter email', max_length=100)),
                ('phone', models.CharField(help_text='enter phone number', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Credentialing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Intial', 'Intial'), ('Reappointment', 'Reappointment')], default='Reappointment', max_length=20)),
                ('start_date', models.DateField(help_text='enter start date')),
                ('end_date', models.DateField(blank=True, help_text='enter completed date')),
                ('year', models.IntegerField(help_text='enter year of Credentialing')),
                ('status', models.CharField(choices=[('backlog', 'backlog'), ('assigned', 'assigned'), ('in_progress', 'in_progress'), ('in_review', 'in_review'), ('completed', 'completed')], default='backlog', max_length=20)),
                ('license_duedate', models.DateField(blank=True, help_text='enter start date')),
                ('remarks', models.TextField(blank=True, help_text='remarks/comments', max_length=600)),
                ('provider', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.provider')),
            ],
        ),
        migrations.CreateModel(
            name='Activities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='activity name', max_length=100)),
                ('description', models.TextField(help_text='activity description', max_length=600)),
                ('status', models.CharField(choices=[('backlog', 'backlog'), ('assigned', 'assigned'), ('in_progress', 'in_progress'), ('in_review', 'in_review'), ('completed', 'completed')], default='backlog', max_length=20)),
                ('assigned_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.volunteer')),
            ],
        ),
    ]
