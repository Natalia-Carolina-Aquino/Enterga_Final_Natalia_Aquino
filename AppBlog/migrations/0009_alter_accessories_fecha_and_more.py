# Generated by Django 5.0 on 2023-12-24 02:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppBlog', '0008_alter_accessories_fecha_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accessories',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 23, 23, 42, 38, 485646)),
        ),
        migrations.AlterField(
            model_name='accessoriescomment',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 23, 23, 42, 38, 490978)),
        ),
        migrations.AlterField(
            model_name='knit',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 23, 23, 42, 38, 459398)),
        ),
        migrations.AlterField(
            model_name='knit',
            name='instrucciones',
            field=models.TextField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='knitcomment',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 23, 23, 42, 38, 465723)),
        ),
        migrations.AlterField(
            model_name='yarn',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 23, 23, 42, 38, 473004)),
        ),
        migrations.AlterField(
            model_name='yarncomment',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 23, 23, 42, 38, 478339)),
        ),
    ]