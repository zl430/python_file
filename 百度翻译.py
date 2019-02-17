import urllib.request
import urllib.parse
import json
#这个是百度翻译api的地址
url = 'http://fanyi.baidu.com/v2transapi'
#准备一下头
headers = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
}
#还有我们准备用Post传的值，这里值用字典的形式
values = {
    'from': 'zh',
    'to': 'en',
    'query': '死肥猪',
    'transtype': 'translang',
    'simple_means_flag': '3'
}
#将字典格式化成能用的形式
data = urllib.parse.urlencode(values).encode('utf-8')
#创建一个request,放入我们的地址、数据、头
request = urllib.request.Request(url, data, headers)
#访问
html = urllib.request.urlopen(request).read().decode('utf-8')
#利用json解析包解析返回的json数据 拿到翻译结果
print(json.loads(html)['trans_result']['data'][0]['dst'])