#!/usr/bin/env python
#coding:utf-8
import string , random
import MySQLdb

fild = string.letters + string.digits

class mysql_init(object):
    def __init__(self, conn):
        self.conn = None

    #connect to mysql
    def connect(self):
        self.conn = MySQLdb.connect(
            host="localhost",
            port=3306,
            user="root",
            passwd="vizrtluo1987",
            db="reboot",
            charset="utf8"
        )

    def cursor(self):
        try:
            return self.conn.cursor()
        except(AttributeError, MySQLdb.OperationalError):
            self.connect()
            return self.conn.cursor()

    def commit(self):
        return self.conn.commit()

    def close(self):
        return self.conn.close()

def process():
    dbconn.connect()
    conn = dbconn.cursor()
    DropTable(conn)
    CreateTable(conn)
    InsertDatas(conn)
    QueryDatas(conn)
    dbconn.close()

def query(sql, conn):
    conn.execute(sql)
    rows = conn.fetchall()
    return rows

def DropTable(conn):
    conn.execute("DROP TABLE IF EXISTS 'user_key'") 

def CreateTable(conn):
    sql_create = '''CREATE TABLE 'user_key' ('key' varchar(50) NOT null)'''
    conn.execute(sql_create)

def InserDates(conn):
    insert_sql = "INSERT INTO user_key VALUES (%(value)s)"
    key_list = generate(200)
    conn.executemany(insert_sql,[dict(value=v) for v in key_list])

def DeleteDate():
    del_sql = "delete from user_key where id =2"
    execute(del_sql)

def QueryDate(conn):
    sql ="select * from user_key"
    rows = query(sql, conn)
    printResult(rows)

def printResult(rows):
    if rows in None:
        print "rows None"
    for row in rows:
        print row




def getRandom():
    return "".join(random.sample(fild,4))

def concatenate(group):
    return "-".join(getRandom() for i in range(group))

def generate(n):
    return [concatenate(5)  for i in range(n)]

if __name__ == '__main__':
    dbconn = mysql_init(None)
    process()
