# Generated by Django 5.0 on 2023-12-16 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppBlog', '0004_alter_knit_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='knit',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='tejidos'),
        ),
    ]
