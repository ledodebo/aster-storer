# Generated by Django 4.2.7 on 2024-06-09 10:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0083_kind_size_delete_test_alter_productvariation_kind_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='catagory',
            new_name='Category',
        ),
       
        migrations.RenameField(
            model_name='productvariation',
            old_name='catagory',
            new_name='Category',
        ),
        migrations.RenameField(
            model_name='productvariation',
            old_name='kind',
            new_name='type',
        ),
        migrations.RemoveField(
            model_name='product',
            name='catagory',
        ),
    ]