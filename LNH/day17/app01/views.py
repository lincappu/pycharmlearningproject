from django.shortcuts import render,redirect,HttpResponse
from app01 import models
def test(request):

    # 查询所有用户信息
    # select * from userinfo
    # [obj1,obj2,obj3]
    # user_list = models.UserInfo.objects.all()
    # for obj in user_list:
    #     # 每个obj都是一行数据
    #     print(obj.id,obj.user,obj.pwd,obj.age)
    #

    # select * from userinfo where user=alex and pwd=123
    # [obj1,obj1]
    # [obj,]
    user_list = models.UserInfo.objects.filter(user='alex',pwd='123').all()

    # 根据条件获取数据库中的第一条数据
    # obj
    user = models.UserInfo.objects.filter(user='alex',pwd='123').first()

    return HttpResponse('....')



def login(request):
    if request.method == "GET":
        # 打开login.html文件
        # 找到特殊标记 {{msg}}
        # 并将第三个参数中字典中的对应值替换
        # 将替换完毕的字符串发送给用户浏览器
        return render(request,'login.html',{'msg':''})
    else:
        # 去请求体中获取数据
        username= request.POST.get('username')
        password = request.POST.get('password')

        # 连接数据库
        # 查询是否存在
        # 关闭数据库
        user = models.UserInfo.objects.filter(user=username,pwd=password).first()
        if user:
            # 在响应头中设置： location:http://www.baidu.com,无响应体
            # return redirect('http://www.baidu.com')
            # 要跳转的URL
            return redirect('/index/')
        else:
            return render(request, 'login.html',{'msg':'用户名或密码错误'})

def index(request):
    return render(request,'index.html')



def parts(request):
    """
    查看部门列表
    :param request:
    :return:
    """
    # [obj,]
    depart_list = models.Department.objects.all()

    return render(request,'parts.html',{'depart_list':depart_list})

def part_add(request):
    """
    添加部门
    :param request:
    :return:
    """
    if request.method == "GET":
        return render(request,'part_add.html')
    else:
        ti = request.POST.get('title')
        # 添加到数据: models.Department
        # 方式一：推荐
        models.Department.objects.create(title=ti)

        # 方式二：
        # obj = models.Department(title=ti)
        # obj.save()

        return redirect('/parts/')


def part_del(request):
    nid = request.GET.get('nid')
    # 去数据库Department表中将 id=nid，删除
    models.Department.objects.filter(id=nid).delete()
    return redirect('/parts/')

def part_edit(request):
    if request.method == 'GET':
        nid = request.GET.get('nid')
        # 根据id去数据库Department表中将 id=nid 一行数据，
        obj = models.Department.objects.filter(id=nid).first()
        if not obj:
            return HttpResponse('小伙子，别瞎搞我脾气可不好！！！')
        return render(request, 'part_edit.html', {'obj': obj})
    else:
        nid = request.GET.get('nid')
        title = request.POST.get('title')
        # 去数据库中找：id=nid的哪行数据，title更新为title
        models.Department.objects.filter(id=nid).update(title=title)
        return redirect('/parts/')


def example(request):
    """
    知识点补充
    :param request:
    :return:
    """
    return HttpResponse('....')

def example_add(request):
    """
    知识点添加
    :param request:
    :return:
    """
    return HttpResponse('example_add')

def example_edit(request,nid,xid):
    print(nid,xid)
    return HttpResponse('编辑')


def keng(request):
    return render(request,'keng.html',{'k1':123,'k2':"alex"})

def tpl(request):
    data_dict = {
        'k1': 123123,
        'k2':[11,22,33,'alex'],
        'k3':{'name':'李杰','age':18}
    }
    return render(request, 'tpl.html', data_dict)

def users(request):
    return HttpResponse('用户列表')

def hosts(request):
    return HttpResponse('主机列表')













