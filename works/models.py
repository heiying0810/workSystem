from django.db import models
class Worklist(models.Model):
    status = (
        ('0', '完成'),
        ('1', '待处理'),
        ('2', '异常'),
        ('3', '暂停'),
        ('4', '放弃'),
    )
    gdType = (
        ('0', '代考'),
        ('1', '挂靠'),
        ('2', '私活'),
        ('3', '其他'),
    )

    name=models.CharField('工单名称',max_length=100,)
    kehuName = models.CharField('客户名称', max_length=100,blank=False)
    phone=models.IntegerField('联系方式',default='13300000000')
    numRmb = models.CharField('总金额', max_length=100,default='None' )
    lir = models.CharField('利润', max_length=100,default='None' )
    type = models.CharField('业务类型', choices=gdType,max_length=20,default='1' )
    content=models.CharField('工单内容',max_length=500,)
    text = models.CharField('备注', max_length=100, default='无')
    name_status=models.CharField('是否完结',choices=status,max_length=20,default='1')
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    modified_time = models.DateTimeField('修改时间', auto_now=True)
    class Meta:
        verbose_name = '工单列表'
        verbose_name_plural=verbose_name
    def __str__(self):
        return self.name

class Jiazhikehu(models.Model):
    gdType = (
        ('0', '代考'),
        ('1', '挂靠'),
        ('2', '私活'),
        ('3', '其他'),
    )
    name = models.CharField('客户名称', max_length=100,blank=False )
    phone = models.IntegerField('联系方式',  default='13300000000')
    type = models.CharField('合作类型', choices=gdType,max_length=20,default='1' )
    text = models.CharField('备注', max_length=100, default='无')
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    modified_time = models.DateTimeField('修改时间', auto_now=True)
    class Meta:
        verbose_name = '价值客户列表'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name