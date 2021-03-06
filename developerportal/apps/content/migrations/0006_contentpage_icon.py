# Generated by Django 2.2.11 on 2020-03-15 15:23

import developerportal.apps.common.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0005_add_social_image_field'),
    ]

    operations = [
        migrations.AddField(
            model_name='contentpage',
            name='icon',
            field=models.FileField(blank=True, default='', help_text='MUST be a black-on-transparent SVG icon ONLY, with no bitmap embedded in it.', upload_to='contentpage/icons', validators=[developerportal.apps.common.validators.check_for_svg_file]),
        ),
    ]
