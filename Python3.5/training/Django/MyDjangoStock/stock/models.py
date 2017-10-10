from django.db import models


class Info(models.Model):
    id = models.AutoField(primary_key=True, max_length=10)
    code = models.CharField(max_length=6, help_text='股票代码',)
    short = models.CharField(max_length=10, help_text='股票简称',)
    chg = models.CharField(max_length=10, help_text='涨跌幅',)
    turnover = models.CharField(max_length=255, help_text='换手率',)
    price = models.DecimalField(max_digits=10, decimal_places=2, help_text='最新价',)
    highs = models.DecimalField(max_digits=10, decimal_places=2, help_text='前期高点',)
    time = models.DateTimeField()

    class Meta:
        db_table = 'info'


class Focus(models.Model):
    id = models.AutoField(primary_key=True, max_length=10)
    note_info = models.CharField(max_length=200, default='', blank=True, null=False,)
    focus_info = models.ForeignKey(Info, db_column='info_id', max_length=10)

    class Meta:
        db_table = 'focus'
