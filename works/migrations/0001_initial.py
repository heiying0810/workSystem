# Generated by Django 3.2.12 on 2022-03-25 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jiazhikehu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='None', max_length=100, verbose_name='客户名称')),
                ('phone', models.IntegerField(default='0', verbose_name='联系方式')),
                ('type', models.CharField(default='None', max_length=100, verbose_name='合作类型')),
                ('text', models.CharField(default='None', max_length=100, verbose_name='备注')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('modified_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
            ],
            options={
                'verbose_name': '价值客户列表',
                'verbose_name_plural': '价值客户列表',
            },
        ),
        migrations.CreateModel(
            name='Worklist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='工单名称')),
                ('kehuName', models.CharField(default='None', max_length=100, verbose_name='客户名称')),
                ('phone', models.IntegerField(default='0', verbose_name='联系方式')),
                ('numRmb', models.CharField(default='None', max_length=100, verbose_name='总金额')),
                ('lir', models.CharField(default='None', max_length=100, verbose_name='利润')),
                ('type', models.CharField(choices=[('0', '大客户'), ('1', '小客户'), ('2', '小微客户'), ('3', '战略客户')], default='1', max_length=20, verbose_name='业务类型')),
                ('content', models.CharField(max_length=500, verbose_name='工单内容')),
                ('text', models.CharField(default='None', max_length=100, verbose_name='备注')),
                ('name_status', models.CharField(choices=[('0', '完成'), ('1', '待处理'), ('2', '异常'), ('3', '暂停'), ('4', '放弃')], default='1', max_length=20, verbose_name='是否完结')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('modified_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
            ],
            options={
                'verbose_name': '工单列表',
                'verbose_name_plural': '工单列表',
            },
        ),
    ]
