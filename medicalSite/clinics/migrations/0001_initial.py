# Generated by Django 4.0 on 2022-05-07 13:20

import django.core.validators
from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Certificates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('created', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Certificates',
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='Clinic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=256)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('city', models.CharField(max_length=256)),
                ('score', models.FloatField(default=2, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('about', tinymce.models.HTMLField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('publish', 'Publish')], default='pending', max_length=30)),
            ],
            options={
                'verbose_name_plural': 'Clinics',
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='ClinicAdd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clinic_name', models.CharField(max_length=256)),
                ('address_1', models.CharField(max_length=256)),
                ('address_2', models.CharField(blank=True, max_length=256, null=True)),
                ('city', models.CharField(max_length=256)),
                ('state', models.CharField(max_length=256)),
                ('country', models.CharField(max_length=256)),
                ('postal_code', models.CharField(max_length=256)),
                ('website', models.CharField(default='NA', max_length=256)),
                ('email', models.CharField(max_length=256)),
                ('phone_code', models.CharField(blank=True, max_length=256, null=True)),
                ('phone_no', models.CharField(max_length=256)),
                ('year_established', models.CharField(max_length=256)),
                ('message', models.CharField(max_length=256)),
                ('created', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('new_lead', 'New Lead'), ('reviewd', 'Reviewed')], default='new_lead', max_length=20)),
                ('is_seen', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'New Clinic Leads',
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='ClinicBeforeAfterImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('afterImage', models.ImageField(upload_to='clinic/after/')),
                ('beforeImage', models.ImageField(upload_to='clinic/before/')),
                ('created', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Clinic Before/After Images',
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='ClinicCertficates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Clinic Certificate',
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='ClinicImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='clinic/')),
                ('is_cover_image', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Clinic Images',
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='ClinicReviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, null=True)),
                ('email', models.CharField(max_length=256)),
                ('review', models.TextField(blank=True, null=True)),
                ('service_rating', models.FloatField(default=4, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('cleanliness_rating', models.FloatField(default=4, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('comfort_rating', models.FloatField(default=4, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('quality_rating', models.FloatField(default=4, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('communication_rating', models.FloatField(default=4, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('created', models.DateTimeField(auto_now=True)),
                ('status_choice', models.CharField(choices=[('accept', 'Accept'), ('delete', 'Delete')], default='delete', max_length=30)),
                ('is_seen', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'Clinic Reviews C',
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='ClinicTreatmentLeads',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_code', models.CharField(blank=True, max_length=256, null=True)),
                ('phone_no', models.CharField(blank=True, max_length=256, null=True)),
                ('email', models.CharField(max_length=256)),
                ('username', models.CharField(max_length=256)),
                ('comment', models.TextField(blank=True, null=True)),
                ('treatment_detail', models.CharField(blank=True, max_length=256, null=True)),
                ('created', models.DateTimeField(auto_now=True)),
                ('is_seen', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'Clinic Treatment Leads',
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(choices=[('mr', 'Mr'), ('mrs', 'Mrs')], default='mr', max_length=10)),
                ('name', models.CharField(max_length=256)),
                ('address_1', models.CharField(blank=True, max_length=556, null=True)),
                ('address_2', models.CharField(blank=True, max_length=556, null=True)),
                ('city', models.CharField(blank=True, max_length=256, null=True)),
                ('state', models.CharField(blank=True, max_length=256, null=True)),
                ('country', models.CharField(blank=True, max_length=256, null=True)),
                ('postal_code', models.CharField(blank=True, max_length=256, null=True)),
                ('email', models.CharField(max_length=256)),
                ('phone_code', models.CharField(blank=True, max_length=256, null=True)),
                ('phone_no', models.CharField(blank=True, max_length=256, null=True)),
                ('msg', models.TextField()),
                ('created', models.DateTimeField(auto_now=True)),
                ('is_seen', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'Contact Leads',
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('img', models.ImageField(blank=True, upload_to='country_img')),
                ('phone_code', models.CharField(max_length=256)),
                ('created', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Country',
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=256)),
                ('symbol', models.CharField(blank=True, max_length=256)),
                ('created', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Currency',
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('code', models.CharField(max_length=50, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Languages',
                'ordering': ('-created',),
            },
        ),
    ]
