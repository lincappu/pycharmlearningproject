# !/usr/bin/env python3
# _*_coding:utf-8_*_


def help_sql(cmd):
    if cmd in func_dic.keys():
        print('{} usage:\n '.format(cmd))
        if cmd == 'select':
            print("\tselect * from staff_table;")
            print("\tselect name,age from staff_table where age > 22;")
            print("\tselect * from staff_table where dept = \"IT\";")
            print("\tselect * from staff_table where date like \"2013\";")
        elif cmd == 'insert':
            print("\tinsert talbe (Alex Li,22,136510546011,IT,2013-04-01);")
        elif cmd == "update":
            print("\tupdate staff_table set dept = \"Market\" where dept = \"IT\";")
        elif cmd == "delete":
            print("\tdelete table  5;")
    else:
        print('your input ERROR!')
    return


def input_sql():
    '''
    接受用户输入，做一些判断，转化 list 并一起返回。
    :return:sql
    '''
    exit_flag = False
    while exit_flag is not True:
        sql = input('sql > ').strip()
        sql_list = sql_to_list(sql)
        if sql.startswith('help'):
            cmd = sql_list[1]
            help_sql(cmd)
            continue
        elif sql == 'q' or sql == 'quit' or sql == 'Q' or sql == 'QUIT' or sql == 'exit' or sql == 'EXIT':
            print('已退出程序！')
            exit(1)
        elif len(sql_list) == 0:
            continue
        elif len(sql_list) < 2:
            continue
        elif not (sql.startswith('select') or sql.startswith('insert') or sql.startswith('update') or sql.startswith(
                'delete')):
            continue
        exit_flag = True
    return sql


def delete_quotes(str):
    '''
    删掉用户输入的条件值中带双引号。单引号不用去
    :param str:
    :return:
    '''
    if '"' in str:
        str = str.strip('"')
    return str


def sql_to_list(sql, delimiter=' '):
    '''
    将用户输入的字符串转化为列表的形式，
    :param sql:
    :param delimiter:
    :return:
    '''
    tmp_list = filter(None, sql.split(delimiter))
    sql_list = [item for item in tmp_list]
    return sql_list


def analyze(sql, table):
    '''
    分析用户输入sql 语句，作用：
    1.拿到 cmd
    2.判断表是否存在
    3.返回命令和要操作的表
    :param sql:
    :param sql_list:
    :param table:
    :return:
    '''
    sql_list = sql_to_list(sql)
    cmd = sql_list[0]
    if sql.startswith('select'):
        sql_table = sql_list[3]
        if sql_table in table:
            return cmd, sql_table
        else:
            return False
    if sql.startswith('insert') or sql.startswith('update') or sql.startswith('delete'):
        sql_table = sql_list[1]
        if sql_table in table:
            return cmd, sql_table
        else:
            return False

            # input_list = sql_to_list(sql)
            # cmd = input_list[0]
            # input_table = input_list[3]
            # if input_table in table:
            #     return cmd, input_table
            # else:
            #     return False


def file_to_data(sql_table):
    '''
    将文件中的数据读到内存中，以遍读取。这个方法是把所有的数据上来就读进内存中。
    :param sql_table:
    :return:
    '''
    n = 0
    struct_list = []
    data_list = []
    with open(sql_table, 'r', encoding='utf-8') as f:
        for line in f:
            if n == 0:
                # line = line.strip('\n')
                struct_list = line.strip('\n').split(',')
            else:
                # line = line.strip('\n')
                line_list = line.strip('\n').split(',')
                data_list.append(line_list)
            n += 1
    return struct_list, data_list


def data_to_file(struct_list, data_list, table):
    '''
    将内存中的数据写入到文件里
    :param struct_list:
    :param data_list:
    :param table:
    :return:
    '''
    with open(table, 'w', encoding='utf-8') as f:
        f.write(','.join(struct_list) + '\n')
        for sub_list in data_list:
            f.write(','.join(sub_list) + '\n')
        print('Write  Done!')


def get_cloum_number(colum_name, struct_list):
    '''
    获取列所对应的索引，然后用这个索引在数据项里面取值
    :param colum_name:
    :param struct_list:
    :return:
    '''
    colum_number = struct_list.index(colum_name)
    # print(colum_number)
    return colum_number


def auto_increament_id(data_list):
    '''
    insert 数据项时，获取新的 id
    :param data_list:
    :return:
    '''
    current_max_id = int(data_list[-1][0])
    new_index_id = current_max_id + 1
    return new_index_id


# 增删改查阶段
def select(sql, struct_list, data_list, sql_table):
    sql_list = sql_to_list(sql)
    select_colum = sql_list[1].split(',')
    all_cloum = False
    all_line = False
    if '*' in select_colum:  # 判断输出那些列
        all_cloum = True
    else:
        cloum_numbers_list = []
        for cloum_name in select_colum:
            number = get_cloum_number(cloum_name, struct_list)
            cloum_numbers_list.append(number)

    # 关键字过滤
    select_row = []  # 过滤后的行
    if 'where' in sql:
        condition_column_name = sql_list[5]
        condition_str = sql_list[6]
        condition_value = sql_list[7]
        condition_value = delete_quotes(condition_value)
        condition_column_number = get_cloum_number(condition_column_name, struct_list)

        if condition_str == '=':
            for line in data_list:
                if line[condition_column_number] == condition_value:
                    select_row.append(line)
        if condition_str == '>':
            for line in data_list:
                if line[condition_column_number] > condition_value:
                    select_row.append(line)
        if condition_str == '>=':
            for line in data_list:
                if line[condition_column_number] >= condition_value:
                    select_row.append(line)
        if condition_str == '<':
            for line in data_list:
                if line[condition_column_number] < condition_value:
                    select_row.append(line)
        if condition_str == '<=':
            for line in data_list:
                if line[condition_column_number] <= condition_value:
                    select_row.append(line)
        if condition_str == 'like':
            for line in data_list:
                if condition_value in line[condition_column_number]:
                    select_row.append(line)
    else:
        all_line = True
        select_row = data_list

    # 输出查询的结果
    print('select result:')
    print('#'.center(80, '#'))
    print('\033[1;31;1m{}\033[0m rows in set'.format(len(select_row)))
    if all_cloum is True:
        print('\033[1;34;1m{:<13} {:<13} {:<13} {:<13} {:<13} {:<13}\033[0m'.format(*struct_list))
        for line in select_row:
            print('{:<13} {:<13} {:<13} {:<13} {:<13} {:<13}'.format(*line))
            # print('\t')
    else:
        len_num = len(select_colum)
        format_str1 = '\033[1;34;1m{:13}\033[0m' * len_num
        format_str2 = '{:13}' * len_num
        print(format_str1.format(*select_colum))
        for line in select_row:
            row_list = []
            for s in cloum_numbers_list:
                row_list.append(line[s])
            print(format_str2.format(*row_list))
    print('#'.center(80, '#'))
    return True


def insert(sql, struct_list, data_list, sql_table):
    '''
    insert sql : insert   user_info.json  (Liusong Fan,22,13143236545,IT,2015-09-09)
    insert sql : insert   user_info.json  (Liusong Fan,22,13487654567,IT,2015-09-09)
    电话号码作为主键。
    目前只支持插入全部数据项。
    手机号码必须是11位
    :param sql:
    :param struct_list:
    :param data_list:
    :return:
    '''
    tmp_insert = sql_to_list(sql.strip().strip('insert').strip(), '(')
    insert_table = tmp_insert[0].strip()
    insert_info = (tmp_insert[1].strip('(').strip(')'))
    insert_list = insert_info.split(',')

    phone_number = insert_list[2]
    if len(phone_number) != 11:
        print("Phone number wrong(11 numbers), can't insert")
        return False
    phone_exist = False
    for item in data_list:
        if phone_number == item[3]:
            phone_exist = True
    if phone_exist:
        print("Phone number is exist, can't insert")
        return False
    else:
        new_index_id = auto_increament_id(data_list)
        insert_list.insert(0, str(new_index_id))
        data_list.append(insert_list)
    data_to_file(struct_list, data_list, insert_table)


def delete(sql, struct_list, data_list, sql_table):
    '''
    # delete  table 5
    使用按 id 号删除
    :param ql:
    :param struct_list:
    :param data_list:
    :param sql_table:
    :return:
    '''
    delete_flag = False
    delete_list = sql_to_list(sql.strip())
    delete_index_id = delete_list[2]
    for item in data_list:
        if delete_index_id == item[0]:
            delete_flag = True
            data_list.remove(item)
    if not delete_flag:
        print("ERROE:The delete id is not exist,can't delete")
        return True
    else:
        data_to_file(struct_list, data_list, sql_table)


def update(sql, struct_list, data_list, sql_table):
    '''
    update user_info.json set dept = "Market" where id = "1"
    set 的值和 where 的值要加"号
    id 是自增的不允许修改，phone 是主键，不允许重复
    set 和 where 只支持 =
    :param sql:
    :param struct_list:
    :param data_list:
    :param sql_table:
    :return:
    '''
    update_list = sql_to_list(sql)
    set_flag = update_list[2]
    modify_column = update_list[3]
    equal_flag = update_list[4]
    modify_value = update_list[5]
    modify_value = delete_quotes(modify_value)
    where_flag = update_list[6]
    condition_column = update_list[7]
    condition_str = update_list[8]
    condition_value = update_list[9]
    condition_value = delete_quotes(condition_value)
    modify_column_number = get_cloum_number(modify_column, struct_list)
    condition_column_number = get_cloum_number(condition_column, struct_list)

    modify_flag = False
    if modify_column == 'id':
        print("ERROR: you can't modify id column value")
        return False
    else:
        if set_flag == 'set' and equal_flag == '=' and where_flag == 'where' and condition_str == '=':
            phone_exists = False
            phone_number = modify_value
            for item in data_list:
                if phone_number == item[3]:
                    phone_exists = True
            if phone_exists:
                print("ERROR: you input phone number is exists, can't update")
                return False
            for d_list in data_list:
                if d_list[condition_column_number] == condition_value:
                    d_list[modify_column_number] = modify_value
                    modify_flag = True
            if modify_flag:
                data_to_file(struct_list, data_list, sql_table)
            else:
                print("ERROR: no match records")
        else:
            print("ERROR: you upate sql error, please input 'help update' get help")


func_dic = {
    '''
    要操作的数据类型
    '''
    'select': select,
    'update': update,
    'insert': insert,
    'delete': delete,
}


def main():
    exit_flag = False
    table = ['user_info.json']
    print('-'.center(60, '-'))
    print('Please input【help [select/update/insert/delete] to get help.')
    print('-'.center(60, '-'))
    while exit_flag is not True:
        sql = input_sql()
        res = analyze(sql, table)
        if not res:
            print('ERROR: your input sql table is not exists!')
            continue
        else:
            cmd = res[0]
            sql_table = res[1]
        struct_list, data_list = file_to_data(sql_table)
        if cmd in func_dic.keys():
            res = func_dic[cmd](sql, struct_list, data_list, sql_table)
            if not res:
                continue
        else:
            print('ERROR:  your command!')


if __name__ == '__main__':
    main()
