import os

DBENGINE = os.getenv('DBENGINE', 'sqlite3')  # ENGINE OPTIONS: mysql, sqlite3, postgresql
DBNAME = os.getenv('DBNAME','lianjia.sqlite3')
DBUSER = os.getenv('DBUSER','root')
DBPASSWORD = os.getenv('DBPASSWORD','')
DBHOST = os.getenv('DBHOST','127.0.0.1')
DBPORT = os.getenv('DBPORT', 3306)
CITY = os.getenv('CITY','lf')  # only one, shanghai=sh shenzhen=sh......
REGIONLIST = (os.getenv("REGIONLIST") or "yanjiao").split(",")  # only pinyin support
