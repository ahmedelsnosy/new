# Generated by Django 4.2 on 2024-05-24 00:29

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(choices=[('Sedan', 'Sedan'), ('SUV', 'SUV'), ('Wagon', 'Wagon')], default='Sedan', max_length=10)),
                ('year', models.IntegerField(validators=[django.core.validators.MinValueValidator(2015), django.core.validators.MaxValueValidator(2023)])),
                ('car_make', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='models', to='djangoapp.carmake')),
            ],
        ),
    ]
