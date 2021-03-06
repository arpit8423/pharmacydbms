# Generated by Django 3.1.2 on 2021-05-30 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('phone', models.CharField(default='', max_length=17)),
                ('years_of_exp', models.IntegerField(default='')),
                ('salary', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('phone', models.CharField(default='', max_length=17)),
                ('age', models.IntegerField(default='')),
                ('gender', models.CharField(max_length=20)),
                ('doctor_name', models.CharField(max_length=200)),
            ],
        ),
    ]
