# Generated by Django 3.1.1 on 2020-09-25 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productmanage', '0004_auto_20200925_1702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productdetails',
            name='productId',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
        ),
    ]
