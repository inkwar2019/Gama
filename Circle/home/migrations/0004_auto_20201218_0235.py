# Generated by Django 3.1.4 on 2020-12-18 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_notification_confirmed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='discount',
            field=models.DecimalField(decimal_places=2, default='0', max_digits=5),
        ),
        migrations.AlterField(
            model_name='post',
            name='price',
            field=models.DecimalField(decimal_places=2, default='0', max_digits=7),
        ),
    ]
