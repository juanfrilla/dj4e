# Generated by Django 2.2.12 on 2021-05-11 08:21

from django.db import migrations
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0014_auto_20210511_0816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='picture',
            field=stdimage.models.StdImageField(blank=True, default='anuncios/image.jpg', null=True, upload_to='anuncios'),
        ),
    ]
