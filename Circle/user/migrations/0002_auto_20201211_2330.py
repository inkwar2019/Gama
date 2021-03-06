# Generated by Django 3.1.4 on 2020-12-12 05:30

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='department',
            field=models.CharField(choices=[('1', 'CSE'), ('2', 'EEE'), ('3', 'ECE'), ('4', 'ETE'), ('5', 'ME'), ('6', 'CE'), ('7', 'CFPE'), ('8', 'MTE'), ('9', 'GCE'), ('10', 'BMCSE'), ('11', 'Architecture')], default='1', max_length=2),
        ),
        migrations.AddField(
            model_name='profile',
            name='p_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None),
        ),
        migrations.AddField(
            model_name='profile',
            name='semister',
            field=models.CharField(choices=[('1', 'odd'), ('2', 'even')], default='1', max_length=1),
        ),
        migrations.AddField(
            model_name='profile',
            name='year',
            field=models.CharField(choices=[('1', 'first'), ('2', 'second'), ('3', 'third'), ('4', 'fourth')], default='1', max_length=1),
        ),
    ]
