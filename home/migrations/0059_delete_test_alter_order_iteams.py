# Generated by Django 4.2.7 on 2024-05-07 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0058_delete_test'),
    ]

    operations = [
       
        migrations.AlterField(
            model_name='order',
            name='iteams',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
    ]