# Generated by Django 4.2.7 on 2024-06-08 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0076_delete_test'),
    ]

    operations = [
        
        migrations.AddField(
            model_name='productvariation',
            name='ava',
            field=models.BooleanField(default=False),
        ),
    ]
