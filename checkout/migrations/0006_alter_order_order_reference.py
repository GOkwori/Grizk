# Generated by Django 5.1.1 on 2024-10-15 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0005_alter_order_order_reference'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_reference',
            field=models.CharField(editable=False, max_length=38),
        ),
    ]