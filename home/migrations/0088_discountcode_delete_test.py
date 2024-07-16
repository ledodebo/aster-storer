# Generated by Django 4.2.7 on 2024-07-15 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0087_clintsemails_delete_test'),
    ]

    operations = [
        migrations.CreateModel(
            name='DiscountCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20, unique=True)),
                ('discount_percent', models.PositiveIntegerField()),
                ('valid_from', models.DateTimeField()),
                ('valid_to', models.DateTimeField()),
                ('active', models.BooleanField(default=True)),
            ],
        ),
       
    ]