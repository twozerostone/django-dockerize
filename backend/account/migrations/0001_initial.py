# Generated by Django 3.1.3 on 2020-12-10 09:03

import account.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('user_id', models.CharField(max_length=15, unique=True, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='이름')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='이메일')),
                ('nickname', models.CharField(max_length=20, unique=True, verbose_name='닉네임')),
                ('profile_image', models.ImageField(default='static/image/profile/user_testman_test', upload_to=account.models.profile_directory_path, verbose_name='프로필사진')),
                ('is_active', models.BooleanField(default=True, verbose_name='활성화')),
                ('is_admin', models.BooleanField(default=False, verbose_name='관리자')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='가입일자')),
                ('last_login', models.DateField(auto_now_add=True, verbose_name='마지막 로그인일자')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': '유저',
                'verbose_name_plural': '유저들',
                'db_table': 'account_custom_user',
            },
            managers=[
                ('objects', account.models.UserManager()),
            ],
        ),
    ]