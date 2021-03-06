# Generated by Django 2.2.7 on 2019-11-15 01:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SocialPlatform',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('platform_name', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'social_platforms',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=200, unique=True)),
                ('social_login_id', models.CharField(blank=True, max_length=100)),
                ('social_platform', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.SocialPlatform')),
            ],
        ),
    ]
