# Generated by Django 2.0.1 on 2018-02-26 01:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0002_auto_20180226_0133'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companyId', models.IntegerField(unique=True)),
                ('compName', models.CharField(max_length=500)),
                ('compSize', models.CharField(max_length=200)),
                ('compIndustry', models.CharField(max_length=500)),
                ('companyLabels', models.CharField(max_length=500)),
                ('compLink', models.CharField(max_length=500)),
                ('compIntroduce', models.TextField()),
                ('contactInfo', models.CharField(max_length=500)),
                ('longitude', models.FloatField()),
                ('latitude', models.FloatField()),
                ('businessZones', models.CharField(max_length=500)),
                ('compHome', models.CharField(max_length=2000)),
                ('companyLogo', models.CharField(max_length=500)),
                ('financeStage', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='DigitizedJob',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('compSize', models.IntegerField(default=50)),
                ('skill', models.IntegerField(default=5)),
                ('experience', models.IntegerField(default=0)),
                ('education', models.IntegerField(default=0)),
                ('salary', models.FloatField(default=5)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jobId', models.IntegerField(unique=True)),
                ('JobName', models.CharField(max_length=200)),
                ('JobPlace', models.CharField(max_length=200)),
                ('JobSalary', models.CharField(max_length=100)),
                ('JobAdvantage', models.CharField(max_length=300)),
                ('releaseTime', models.CharField(max_length=300)),
                ('jobNeed', models.CharField(max_length=300)),
                ('educationRequire', models.CharField(max_length=300)),
                ('experienceRequire', models.CharField(max_length=300)),
                ('skillRequire', models.CharField(max_length=300)),
                ('jobLink', models.CharField(max_length=500)),
                ('jobInfo', models.TextField()),
                ('jobNature', models.CharField(max_length=200)),
                ('jobLabels', models.CharField(max_length=300)),
                ('company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='analysis.Company')),
            ],
        ),
        migrations.AddField(
            model_name='digitizedjob',
            name='Job',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='analysis.Job'),
        ),
    ]