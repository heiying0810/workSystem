# Generated by Django 3.2.12 on 2022-03-25 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worklist',
            name='type',
            field=models.CharField(choices=[('0', '代考'), ('1', '挂靠'), ('2', '私活'), ('3', '其他')], default='1', max_length=20, verbose_name='业务类型'),
        ),
    ]