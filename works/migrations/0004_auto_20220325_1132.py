# Generated by Django 3.2.12 on 2022-03-25 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0003_alter_jiazhikehu_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jiazhikehu',
            name='name',
            field=models.CharField(max_length=100, verbose_name='客户名称'),
        ),
        migrations.AlterField(
            model_name='worklist',
            name='kehuName',
            field=models.CharField(max_length=100, verbose_name='客户名称'),
        ),
    ]
