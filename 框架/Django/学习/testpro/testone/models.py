from django.db import models


class Student(models.Model):
    FRESHMAN = 'FR'
    SOPHOMORE = 'SO'
    JUNIOR = 'JR'
    SENIOR = 'SR'
    GRADUATE = 'GR'
    YEAR_IN_SCHOOL_CHOICES = [
        (FRESHMAN, 'Freshman'),
        (SOPHOMORE, 'Sophomore'),
        (JUNIOR, 'Junior'),
        (SENIOR, 'Senior'),
        (GRADUATE, 'Graduate'),
    ]

    # 二元组的使用方法
    year_in_school = models.CharField(
        max_length=2,
        choices=YEAR_IN_SCHOOL_CHOICES,
        default=FRESHMAN,
    )

    def is_upperclass(self):
        return self.year_in_school in {self.JUNIOR, self.SENIOR}


class Teacher(models.Model):
    first_name=models.CharField('老师的姓',max_length=40,default='f')
    last_name=models.CharField('老师的名',max_length=40,default='ls')
    age=models.IntegerField()

    # 模型方法
    @property
    def full_name(self):
        return '%s%s' %(self.first_name,self.last_name)

    # meta  元数据的使用方法
    class Meta:
        ordering = ['age']
        db_table = 'ter'



# 应用抽象基类
class Car(models.Model):
    name=models.CharField(max_length=10)
    age=models.IntegerField()

    class Meta:
        abstract = True

class Bieke(Car):
    address=models.CharField(max_length=40)

















