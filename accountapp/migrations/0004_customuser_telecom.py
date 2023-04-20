# Generated by Django 3.2.18 on 2023-04-20 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accountapp', '0003_auto_20230420_0130'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='telecom',
            field=models.CharField(choices=[('SKT', 'SKT'), ('KT', 'KT'), ('LG', 'LG')], default='', max_length=15),
            preserve_default=False,
        ),
    ]