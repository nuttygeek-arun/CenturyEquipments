# Generated by Django 3.1.1 on 2020-09-25 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productmanage', '0005_auto_20200925_1707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productdetails',
            name='productId',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]