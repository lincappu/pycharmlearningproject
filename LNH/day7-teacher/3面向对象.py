#游戏工作
#人狗大战
#人 、 狗
#人角色：攻击力 生命值 名字 等级
#狗角色：攻击力 生命值 名字 品种
def person(attack,life_value,name,level):
    def atk(dog_d):
        print('%s 打了 %s' % (name, dog_d['name']))
        dog_d['life_value'] -= attack
    person_dic = {'attack':attack,
              'life_value':life_value,
              'name':name,
              'level':level,
                  'atk':atk}
    return person_dic

def dog(attack,life_value,name,level):
    def bite(person_d):
        print('%s 咬了 %s' % (name, person_d['name']))
        person_d['life_value'] -=attack
    dog_dic = {'attack':attack,
              'life_value':life_value,
              'name':name,
              'level':level,
               'bite':bite}
    return dog_dic

alex = person(100,1000,'alex',2)
alex2 = person(1001,10000,'alex2',2)
egg = dog(200,2000,'egon',10)
alex['atk'](egg)
print(egg['life_value'])

# 面向对象编程
# 对象 - 角色
#   alex
#   egg
# 类 ：具有相同属性和方法的一类事物就是类
#   person
#   dog
# 对象和类的关系
# 对象是一个实实在在存在的事物，是独一无二的
# 类 是一个抽象的大致规范了一类事物的范围
#

