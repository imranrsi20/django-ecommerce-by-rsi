# Generated by Django 3.1.7 on 2021-03-31 03:12

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0008_auto_20210330_2359'),
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Order',
            new_name='ShopCart',
        ),
    ]
