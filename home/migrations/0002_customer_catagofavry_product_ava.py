# Generated by Django 4.2.7 on 2023-11-14 20:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='catagofavry',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='home.product'),
        ),
        migrations.AddField(
            model_name='product',
            name='ava',
            field=models.BooleanField(default=True),
        ),
    ]