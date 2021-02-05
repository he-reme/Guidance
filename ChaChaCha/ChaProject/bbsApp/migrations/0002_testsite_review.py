# Generated by Django 3.1.5 on 2021-02-05 01:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('searchApp', '0002_auto_20210204_1848'),
        ('bbsApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestSite_review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=8)),
                ('content', models.CharField(max_length=500)),
                ('academy_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='searchApp.testsite')),
            ],
        ),
    ]
