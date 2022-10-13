# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS


import hashlib

file_name = {
    'user': '../db/user_info.json',      # 用户名和密码验证文件
    'teacher': '../db/teacher_info.txt',        # 老师详细信息
    'student': '../db/student_info.txt',        # 学生详细信息
    'classes': '../db/classes_info.txt',        # 班级详细信息
    'course': '../db/course_info.txt',      # 课程详细信息
    'school': '../db/school_info.txt',      # 学校信息
    'log_path': '../log.sh/test.log.sh',      # 日志文件
}

secret_key = 'fanliusong'.encode('utf-8').decode('utf-8')  # 保证肯定是 str 类型
print(secret_key)
print(type(secret_key))
