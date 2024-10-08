# Generated by Django 5.1.1 on 2024-09-04 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.CharField(editable=False, max_length=12, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('role', models.IntegerField(choices=[(0, 'Researcher'), (1, 'Entrepreneur'), (2, 'Company'), (3, 'Accelerator')])),
                ('phone_no', models.CharField(max_length=15)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('last_logged_in_at', models.DateTimeField(blank=True, null=True)),
                ('address', models.TextField()),
                ('citizenship', models.CharField(max_length=100)),
            ],
        ),
    ]
