#coding=utf-8
import sys
#sys.path.append("c:\\python33\\lib\\site-packages\\baidu_aip-1.2.0.0-py3.3.egg\\aip")


#引入文字识别OCR SDK
from aip import AipOcr

# 初始化程序
APP_ID = '9321940'
API_KEY = 'Gba0ob75cct43Ocw6oFvRunI'
SECRET_KEY = 'PYD93uhNcZkbTPnGYl55H9EcGoGQovCe'

#读取图片
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

#初始化ApiOcr对象
aipOcr = AipOcr(APP_ID, API_KEY, SECRET_KEY)

# 定义参数变量
options = {
  'detect_direction': False,
  'language_type': 'CHN_ENG',
}


# 调用通用文字识别接口
result = aipOcr.general(get_file_content('apic25010.jpg'), options)
print(result)