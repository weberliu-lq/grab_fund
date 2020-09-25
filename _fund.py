import requests
import json
import re

# code基金代码
def getFundInfo(code):
    nullResult="jsonpgz();"
    url = "http://fundgz.1234567.com.cn/js/%s.js"%code
    # 浏览器头
    headers = {'content-type': 'application/json',
               'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'}

    r = requests.get(url, headers=headers)
    # 返回信息
    content = r.text
    if content != nullResult :
        # content = jsonpgz({"fundcode":"161725","name":"招商中证白酒指数分级","jzrq":"2020-09-24","dwjz":"0.9503","gsz":"0.9505","gszzl":"0.02","gztime":"2020-09-25 15:00"});

        # 正则表达式
        pattern = r'^jsonpgz\((.*)\)'
        # 查找结果
        search = re.findall(pattern, content)
        # 遍历结果
        for i in search:
          data = json.loads(i)
          #print(data)

          # {
          #     'fundcode': '161725', 'name': '招商中证白酒指数分级',
          #     'jzrq': '2020-09-24',
          #     'dwjz': '0.9503', 昨日成交净值
          #     'gsz': '0.9515',  今日净值估算
          #     'gszzl': '0.12',  今日收益率
          #     'gztime': '2020-09-25 14:01'
          # }
          print("代码：{}，基金: {},今日净值估算：{}，收益率: {}".format(data['fundcode'],data['name'],data['gsz'],data['gszzl']))
    else:
        print("代码：{}".format(code)+",未查询到信息")