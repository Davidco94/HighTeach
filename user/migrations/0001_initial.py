# Generated by Django 4.1.7 on 2023-04-13 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(max_length=60, unique=True, verbose_name='email')),
                ('username', models.CharField(max_length=30, unique=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='last login')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('user_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('phone_number', models.IntegerField()),
                ('city', models.CharField(max_length=30)),
                ('account_type', models.CharField(choices=[('T', 'Teacher'), ('S', 'Student'),
                                                           ('B', 'Teacher and Student')], default='S', max_length=1)),
                ('meeting_method', models.CharField(choices=[('L', 'Live'), ('O', 'Online'),
                                                             ('B', 'Live and Online')], default='B', max_length=1)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
