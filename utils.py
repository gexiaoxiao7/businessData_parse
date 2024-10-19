import pickle
import json
from openai import OpenAI
from config import api_key

client = OpenAI(
    api_key= api_key,
    base_url="https://api.deepseek.com",
)

instruction = """
你精通中文命名实体识别的任务，可以从给定的自然语言中提取出出资人（name）、出资额（should_capi）、stock_percent（出资百分比）。
如果不能解析出相关字段，则填一个""空字符串
示例输入：左强 出资 49.500000万人民币 比例 79.2000%;许剑文 出资 0.500000万人民币 比例 0.8000%;西藏险峰管理咨询有限公司 出资 9.375000万人民币 比例 15.0000%;西藏险峰华兴长青投资有限公司 出资 3.125000万人民币 比例 5.0000%;
示例输出(一个列表list,不需要【```json ```】格式)：
[{"name": "左强", "should_capi": "49.500000", "unit": "万", "currency": "人民币", "stock_percent": "79.2000%"}, {"name": "许剑文", "should_capi": "0.500000", "unit": "万", "currency": "人民币", "stock_percent": "0.8000%"}, {"name": "西藏险峰管理咨询有限公司", "should_capi": "9.375000", "unit": "万", "currency": "人民币", "stock_percent": "15.0000%"}, {"name": "西藏险峰华兴长青投资有限公司", "should_capi": "3.125000", "unit": "万", "currency": "人民币", "stock_percent": "5.0000%"}]
"""

def output_one_sentence(sentence):
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": instruction},
            {"role": "user", "content": sentence},
        ],
        stream=False
    )
    res = json.loads(response.choices[0].message.content)
    return res

def load_pkl(fp):
    """加载pkl文件"""
    with open(fp, 'rb') as f:
        data = pickle.load(f)
        return data

def load_file(fp: str, sep: str = None, name_tuple=None):
    """
    读取文件；
    若sep为None，按行读取，返回文件内容列表，格式为:[xxx,xxx,xxx,...]
    若不为None，按行读取分隔，返回文件内容列表，格式为: [[xxx,xxx],[xxx,xxx],...]
    """
    with open(fp, "r", encoding="utf-8") as f:
        lines = f.readlines()
        if sep:
            if name_tuple:
                return map(name_tuple._make, [line.strip().split(sep) for line in lines])
            else:
                return [line.strip().split(sep) for line in lines]
        else:
            return lines

def save_pkl(data, fp):
    """保存pkl文件，数据序列化"""
    with open(fp, 'wb') as f:
        pickle.dump(data, f)

