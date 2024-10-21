# Generated by Django 5.1.1 on 2024-10-04 13:41

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_reference',
            field=models.UUIDField(
                default=uuid.uuid4, editable=False, unique=True),
        ),
    ]
