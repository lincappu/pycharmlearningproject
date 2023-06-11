# !/usr/bin/env python3
# _*_coding:utf-8_*_
# __author__：FLS


from celery.result import AsyncResult
from celery_task import app

async_result=AsyncResult(id="fcd39df9-9214-4952-a7eb-f95fd68051ba",app=app)

if async_result.successful():
    result=async_result.get()
    print(result)

    # result.forget() # 将结果删除，默认执行完成后结果不会自动删除
    # async.revoke(terminate=True) # 无论现在是什么时候都要终止任务
    # async.revoke(terminate=False) # 如果任务没有开始，才会终止

elif async_result.failed():
    print('执行失败')
elif async_result.status=='PENDING':
    print('任务等待执行中')
elif async_result.status=='RETRY':
    print('任务异常后正在重试')
elif async_result.status=='STARTED':
    print('任务执行中')