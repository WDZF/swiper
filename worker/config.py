broker_url = 'redis://:fanding@www.fand.wang:6379/1'
broker_pool_limit = 100  # Borker 连接池, 默认是10

timezone = 'Asia/Shanghai'
accept_content = ['pickle', 'json']

task_serializer = 'pickle'

result_backend = 'redis://:fanding@www.fand.wang:6379/1'
result_serializer = 'pickle'
result_cache_max = 1000  # 任务结果最大缓存数量
result_expires = 3600  # 任务过期时间

worker_redirect_stdouts_level = 'INFO'
