from django.db import models

# 类对象数据库的表
class UserInfo(models.Model):
    # 字段对应数据库中列
    id = models.AutoField(primary_key=True) # 创建id列，自增，int,主键
    user = models.CharField(max_length=32,null=False)  # varchar(32)
    pwd = models.CharField(max_length=64)
    # age = models.IntegerField() # int类型
    # UserInfo.objects.create(user=xxx,pwd=xxx,age=xx)


class Department(models.Model):
    """
    部门表
    """
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32)


class Host(models.Model):
    """
    主机表

      hostname    ip         部门_id
      c1.com   1.1.1.1        1
      c2.com   1.1.1.2        1
      c3.com   1.1.1.3        2
      c4.com   1.1.1.4        4
    """
    hostname = models.CharField(max_length=32)

    ip = models.CharField(max_length=32,default='1.1.1.1')

    # 让当前表Host和Department表中的id字段 做FK关联
    # 如果是FK，那么数据库字段：depart_id
    depart = models.ForeignKey(to='Department',to_field='id',default=1)

"""
1. 查看主机列表:QuerySet类型，类比特殊列表
    host_list = models.Host.objects.all()
    for obj in host_list:
        obj.id        obj.hostname      obj.ip       obj.depart_id     obj.depart.title
        
2. 添加主机页面：选择
    def host_add():
        depart_list = models.Department.objects.all()
        return rendre(...., {depart_list:depart_list})
    
    
    <input name='hostname' />
    <input name='ip' />
    <select name='dp_id'>
        {% for x in depart_list %}
            <option value="{{x.id}}">{{x.title}}</option>
        {% endfor%}
    </select>


    request.POST: 
        hostname
        ip
        dp_id
    
    models.Host.objects.create(hostname=hostname,ip=ip,depart_id=dp_id)

3. 编辑

     <select name='dp_id'>
        {% for x in depart_list %}
            <option value="{{x.id}}" selected>{{x.title}}</option>
        {% endfor%}
    </select>
"""