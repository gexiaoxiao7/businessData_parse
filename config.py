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

# model: "database2database" or "database2csv"
# 数据库到数据库迁移或者数据库到csv文件迁移
model = 'database2csv'

# wanted_eid: 如果为空则默认迁移整个数据表
wanted_eid = [
    'aaa',
    'bbb'
]
