from django.db import models


# Create your models here.
BALANCE_TYPE = ((u'收入', u'收入'), (u'支出', u'支出'))

class Category(models.Model):
    category = models.CharField(max_length=20)

    # 將後台呈現的名稱為 category
    def __str__(self):
        return self.category

class Record(models.Model):
    date = models.DateField()
    description = models.CharField(max_length=300)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    cash = models.IntegerField()
    balance_type = models.CharField(max_length=2, choices=BALANCE_TYPE)

    def __str__(self):
        return self.description
