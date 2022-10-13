# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS

from  pymysql import cursors, connect


class MysqlHelper:
    def __init__(self,
                 host='39.97.191.233',
                 port=3306,
                 user='root',
                 password='yJNDSDcUjIDADJHe',
                 database='jumpserver',
                 charset='utf8',
                 cursor_type=cursors.DictCursor,):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database
        self.charset = charset
        self._cursor_type = cursor_type
        self._conn = None
        self._cursor = None



        # def __init__(self, host, port, user, password, database, charset,cursor_type=cursors.DictCursor):
        #     self.host = host
        #     self.port = port
        #     self.user = user
        #     self.password = password
        #     self.database = database
        #     self.charset = charset
        #     self._conn = None
        #     self._cursor = None
        #     self.cursor_type = cursor_type


    def _open(self):
        print('数据库连接已打开')
        self._conn = connect(host=self.host,
                             port=self.port,
                             user=self.user,
                             password=self.password,
                             database=self.database,
                             charset=self.charset)
        self._cursor = self._conn.cursor(cursor=self._cursor_type)

    def _close(self):
        print('关闭数据库连接')
        self._cursor.close()
        self._conn.close()

    def one(self, sql, params=None):
        result: tuple = None
        try:
            self._open()
            self._cursor.excute(sql, params)
            result = self._cursor.fetchone()
        except Exception as e:
            print(e)
        finally:
            self._close()
        return result

    def all(self, sql, params=None):
        result: tuple = None
        try:
            self._open()
            self._cursor.execute(sql, params)
            result = self._cursor.fetchall()
        except Exception as e:
            print(e)
        finally:
            self._close()
        return result

    def exe(self, sql, params=None):
        try:
            self._open()
            self._cursor.execute(sql, params)
            self._conn.commit()
        except:
            self._conn.rollback()
        finally:
            self._close()


    def exemany(self, sql, params=None):
        try:
            self._open()
            self._cursor.executemany(sql, params)  # 这个参数必须是列表中的元组或者元组中的元组类型。
            self._conn.commit()
        except Exception as e:
            print(e)
            self._conn.rollback()
        finally:
            self._close()




    # 对CRUD的封装,传入的值都是字典形式的，
    def insert(self, table_name, insert_dict):
        try:
            param = ''
            value = ''
            if (isinstance(insert_dict, dict)):
                for key in insert_dict.keys():
                    param = param + key + ","
                    value = value + insert_dict[key] + ','
                param = param[:-1]
                value = value[:-1]
            sql = "insert into %s (%s) values(%s)" % (table_name, param, value)
            self._cursor.execute(sql)
            id = self._cursor.lastrowid
            self._open()
            self._conn.commit()
        except:
            self._conn.rollback()
        finally:
            self._close()
        return id

    # where 也是一个字典
    def delete(self, table_name, where=''):
        try:
            if (where != ''):
                str = 'where'
                for key_value in where.keys():
                    value = where[key_value]
                    str = str + ' ' + key_value + '=' + value + ' ' + 'and'
                where = str[:-3]
                sql = "delete from %s  %s" % (table_name, where)
                self._open()
                self._cursor.execute(sql)
                self._conn.commit()
        except:
            self._conn.rollback()
        finally:
            self._close()

    def select(self, param, fields='*'):
        result=None
        table = param['table']
        try:
            if ('where' in param):
                thewhere = param['where']
                if (isinstance(thewhere, dict)):
                    keys = thewhere.keys()
                    str = 'where'
                    for key_value in keys:
                        value = thewhere[key_value]
                        str = str + ' ' + key_value + '=' + value + ' ' + 'and'
                    where = str[:-3]
            else:
                where = ''
            sql = "select %s from %s  %s" % (fields, table, where)
            self._open()
            self._cursor.execute(sql)
            result = self._cursor.fetchall()
        except Exception as e:
            print(e)
        finally:
            self._close()
        return result

    # 显示建表语句
    def showcreateTable(self, table):
        result = None
        try:
            sql = 'show create table %s' % (table)
            self._open()
            self._cursor.execute(sql)
            result = self._cursor.fetchall()[0]
        except Exception as e:
            print(e)
        finally:
            self._close()
        return result['Create Table']

    # 显示表结构语句
    def showcolumns(self, table):
        dict1 = {}
        try:
            sql = 'show columns from %s ' % (table)
            print(sql)
            print(self._cursor)
            self._open()
            self._cursor.execute(sql)
            result = self._cursor.fetchall()
            for info in result:
                dict1[info['Field']] = info
        except Exception as e:
            print(e)
        finally:
            self._close()
        return dict1



m=MysqlHelper()
print(m.cursor_type)

# res=m.showcolumns('test')
# print(res)

param={
    'table':'test'
}
res=m.select(param)
print(res)