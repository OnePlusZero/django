# Generated by Django 2.2.4 on 2019-08-13 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bboard', '0003_auto_20190813_2119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rubric',
            name='name',
            field=models.CharField(db_index=True, max_length=120, verbose_name='Название'),
        ),
    ]