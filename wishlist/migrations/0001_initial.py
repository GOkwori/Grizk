# Generated by Django 5.0.6 on 2024-09-13 23:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0002_alter_category_options'),
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
                ('user_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_wishlist', to='profiles.userprofile')),
            ],
            options={
                'unique_together': {('user_profile', 'product')},
            },
        ),
    ]