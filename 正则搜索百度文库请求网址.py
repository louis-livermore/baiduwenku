import re
import requests
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
}

url = 'https://wenku.baidu.com/view/30d005a32e3f5727a4e962d0.html'

res = requests.get(url, headers=headers)

regex = re.compile(r'htmlUrls.*\'')
string = regex.findall(res.text)[0]
print(string)

regex = re.compile(r'{.*}')
s = regex.findall(string)[0]
print(s)

sss = s.replace('\\x22', '"')
print(sss)

de = json.loads(sss)
haha = de['json'][0]['pageLoadUrl']
print(de['json'][0]['pageLoadUrl'])
result = de['json'][0]['pageLoadUrl'].replace('\\', '')
print(result)


string = ""
for item in de['json']:
    url = item['pageLoadUrl'].replace('\\', '')
    res = requests.get(url, headers)
    print(res.text)
    decode_json = json.loads(res.text[8:-1])

    for i in decode_json['body']:
        if type(i['c']) == str:
            string += i['c']

print(string)