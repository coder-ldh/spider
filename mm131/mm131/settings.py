# -*- coding: utf-8 -*-

BOT_NAME = 'mm131'

SPIDER_MODULES = ['mm131.spiders']
NEWSPIDER_MODULE = 'mm131.spiders'


# Obey robots.txt rules
ROBOTSTXT_OBEY = False

#添加请求头
DEFAULT_REQUEST_HEADERS = {
'accept': 'image/webp,*/*;q=0.8',
'accept-language': 'zh-CN,zh;q=0.8',
'referer': 'https://www.mm131.com/',
'user-agent': 'Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36',
}

ITEM_PIPELINES = {
'mm131.mysqlpipelines.MySqlPipeline': 300,
}

#Mysql数据库的配置信息
MYSQL_HOST = '192.168.0.200'
MYSQL_DBNAME = 'jianshu'        #数据库名字，请修改
MYSQL_USER = 'root'             #数据库账号，请修改
MYSQL_PASSWD = '123456'         #数据库密码，请修改
MYSQL_PORT = 3306               #数据库端口，