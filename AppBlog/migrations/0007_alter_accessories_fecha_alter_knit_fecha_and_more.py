# Generated by Django 5.0 on 2023-12-17 01:38

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppBlog', '0006_alter_accessories_fecha_alter_knit_fecha_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='accessories',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 16, 22, 38, 1, 1553)),
        ),
        migrations.AlterField(
            model_name='knit',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 16, 22, 38, 0, 998380)),
        ),
        migrations.AlterField(
            model_name='yarn',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 16, 22, 38, 0, 999412)),
        ),
        migrations.CreateModel(
            name='AccessoriesComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comentario', models.CharField(max_length=500)),
                ('fecha', models.DateTimeField(default=datetime.datetime(2023, 12, 16, 22, 38, 1, 2552))),
                ('accesorio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppBlog.accessories')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='KnitComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comentario', models.CharField(max_length=500)),
                ('fecha', models.DateTimeField(default=datetime.datetime(2023, 12, 16, 22, 38, 0, 999412))),
                ('tejido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppBlog.knit')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='YarnComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comentario', models.CharField(max_length=500)),
                ('fecha', models.DateTimeField(default=datetime.datetime(2023, 12, 16, 22, 38, 1, 555))),
                ('hilado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppBlog.yarn')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
