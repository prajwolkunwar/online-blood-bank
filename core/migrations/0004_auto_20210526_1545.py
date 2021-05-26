# Generated by Django 3.1.7 on 2021-05-26 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20210525_2306'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.CharField(max_length=255)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.SlugField(max_length=255)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='LocalLevel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.SlugField(max_length=255)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='request',
            name='blood_group',
            field=models.CharField(choices=[('AP', 'A+'), ('AN', 'A-'), ('BP', 'B+'), ('BN', 'B-'), ('ABP', 'AB+'), ('ABN', 'AB+'), ('OP', 'O+'), ('ON', 'O-')], max_length=4),
        ),
        migrations.AlterField(
            model_name='request',
            name='requested_date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='request',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('verified', 'Verified'), ('completed', 'Completed')], default='pending', max_length=10),
        ),
    ]
