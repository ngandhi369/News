# Generated by Django 3.2.3 on 2021-06-09 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NewsApp', '0006_auto_20210610_0034'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='customer',
            name='location',
        ),
        migrations.AddField(
            model_name='customer',
            name='location',
            field=models.ManyToManyField(to='NewsApp.Location'),
        ),
    ]
