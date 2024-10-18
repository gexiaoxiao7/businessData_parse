source_params = {
    'host': 'localhost',
    'user': 'marshall',
    'password': '123456',
    'db': 'business_data',
    'port': 3306  # 默认MySQL端口
}

target_params = {
    'host': 'localhost',
    'user': 'marshall',
    'password': '123456',
    'db': 'business_data',
    'port': 3306  # 默认MySQL端口
}

# 定义要迁移的表名
source_table_name = 't_changerec_format'
target_table_name = 't_changerec_target_format'

# 设置deepseek的api_key
api_key = "sk-1cf0405d84f8419abc0a7de7bbd23f03"