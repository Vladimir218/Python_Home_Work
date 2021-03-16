import re


pattern = re.compile(r'([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})'
                     r'.+\[(.+)\]'
                     r'.+(GET|POST|PUT|DELETE)'
                     r'\s([\/\w]+)\sHTTP.+"\s(\d+)'
                     r'\s(\d+)')

with open('nginx_logs.txt','r',encoding='UTF-8') as f:
    for line in f:
       print(pattern.findall(line))