# Generated by Django 3.1.12 on 2021-09-29 07:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('category', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('rating', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('instructorName', models.CharField(blank=True, max_length=200, null=True)),
                ('duration', models.CharField(blank=True, max_length=200, null=True)),
                ('price', models.CharField(blank=True, max_length=200, null=True)),
                ('lectureNum', models.CharField(blank=True, max_length=200, null=True)),
                ('salePrice', models.CharField(blank=True, max_length=200, null=True)),
                ('level', models.CharField(blank=True, max_length=200, null=True)),
                ('language', models.CharField(blank=True, max_length=200, null=True)),
                ('certificate', models.BooleanField(blank=True, default=True, null=True)),
                ('promoVideoLink', models.CharField(blank=True, max_length=200, null=True)),
                ('instructorDesignation', models.CharField(blank=True, max_length=200, null=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
