# Generated by Django 4.2.3 on 2023-07-07 04:55

import app.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_author_book_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.IntegerField(validators=[app.validators.validate_integer]),
        ),
    ]