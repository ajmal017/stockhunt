# Generated by Django 2.0.2 on 2019-01-15 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_remove_product_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='icon',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
