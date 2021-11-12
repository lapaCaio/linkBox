# Generated by Django 3.2.9 on 2021-11-12 00:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20211112_0041'),
        ('links', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='page',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='pages.page'),
            preserve_default=False,
        ),
    ]