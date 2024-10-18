source_params = {
    'host': '目标数据库地址',
    'user': '',
    'password': '',
    'db': '数据库名',
    'port': 3306  # 默认MySQL端口
}

target_params = {
    'host': '解析表所在的数据库地址',
    'user': '',
    'password': '',
    'db': '数据库名',
    'port': 3306  # 默认MySQL端口
}

# 定义要迁移的表名
source_table_name = 't_changerec_format'
target_table_name = 't_changerec_target_format'

# 设置deepseek的api_key
api_key = ""