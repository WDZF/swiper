from celery import Celery

celery_app = Celery('tasks', broker='redis://:fanding@www.fand.wang:6379/0')


def call_by_worker(func):
    '''在celery中进行异步调用,是一个装饰器'''
    task = celery_app.task(func)
    return task.delay

