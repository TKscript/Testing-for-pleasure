# -*- coding: utf-8 -*-

#需要存在库名（qy_0000x/ty_0000x/tqsy_0000x）,否则无法正常访问
#需要设置mysql与python的环境变量
#该文件需要放在C:\python路径下，可以发送快捷方式到桌面
#使用时替换库名、路径即可
#路径下不要带中文、空格

import MySQLdb
import os

#定义形参，传入实参后变成实参表示

def changeRole(Role):

    Role.execute("SET @userid := 0")

    Role.execute("update role set userid=(@userid:=@userid+1), name= concat('ss', @userid)  ORDER BY role.`totalgrade` desc")  #userid按战力从1开始排序

    Role.execute("update role set bag = null")  #清空背包

    Role.execute("delete from role where userid > 30")  #删除低等级角色
 
    return

# 清除跨服数据库

def deleteCS_qy(CS):

    qy = CS.execute("select schema_name from information_schema.schemata where schema_name = 'qy_01001'")

    if qy == 1:

        CS.execute("drop database qy_01001")
        CS.execute("drop database qy_log_01001")

    else:
        return
    return

def deleteCS_tqsy(CS):

    tqsy = CS.execute("select schema_name from information_schema.schemata where schema_name = 'tqsy_00002'")

    if tqsy == 1:

        CS.execute("drop database tqsy_00002")
        CS.execute("drop database tqsy_log_00002")

    else:
        return
    return


def update_database():

    op = raw_input(
        'please select your database''\n'
        '==================================''\n'
        '1.Agame1''\n'
        '2.Agame2''\n'
        '3.AgameBT''\n'
        '==================================''\n'
        '4.Xgame1''\n'
        '5.XgameBT''\n'
        '==================================''\n'
        '6.Vgame1''\n'
        '7.Vgame2''\n'
        '\n')

    if op == '1':

        db = MySQLdb.connect("localhost", "root", "tthw123", "qy_00001", charset = "utf8")

        cursor = db.cursor()

        deleteCS_qy(cursor)

        cursor.execute("drop database qy_00001")
        cursor.execute("drop database qy_log_00001")
        cursor.execute("drop database qy_login")
        print("delete success")
        cursor.execute("create database qy_00001")
        cursor.execute("create database qy_log_00001")
        cursor.execute("create database qy_login")
        print("create success")

        path = 'mysql -u root -ptthw123 qy_00001 < C:\\Users\\Administrator\\Desktop\\qy_cn_changeTime3_8_12064.sql'

        os.system(path)

        cursor.execute("use qy_00001")

        changeRole(cursor)

        db.close()

    elif op == '2':

        db = MySQLdb.connect("localhost", "root", "tthw123", "qy_00002", charset = "utf8")

        cursor = db.cursor()

        cursor.execute("drop database qy_00002")
        cursor.execute("drop database qy_log_00002")
        cursor.execute("drop database qy_login")
        print("delete success")
        cursor.execute("create database qy_00002")
        cursor.execute("create database qy_log_00002")
        cursor.execute("create database qy_login")
        print("create success")

        path = 'mysql -u root -ptthw123 qy_00002 < C:\\Users\\Administrator\\Desktop\\qy_cn_3_1_12085.sql'

        os.system(path)

        cursor.execute("use qy_00002")

        changeRole(cursor) 

        db.close()
    
    elif op == '3':

        db = MySQLdb.connect("localhost", "root", "tthw123", "qy_00001", charset = "utf8")

        cursor = db.cursor()

        deleteCS_qy(cursor)

        cursor.execute("drop database qy_00001")
        cursor.execute("drop database qy_log_00001")
        cursor.execute("drop database qy_login")
        print("delete success")
        cursor.execute("create database qy_00001")
        cursor.execute("create database qy_log_00001")
        cursor.execute("create database qy_login")
        print("create success")

        path = 'mysql -u root -ptthw123 qy_00001 < C:\\Users\\Administrator\\Desktop\\qy_20001_BT.sql'

        os.system(path)

        cursor.execute("use qy_00001")
        
        changeRole(cursor)

        db.close()

    elif op == '4':

        db = MySQLdb.connect("localhost", "root", "tthw123", "xgame1", charset = "utf8")

        cursor = db.cursor()

        cursor.execute("drop database xgame1")
        cursor.execute("drop database xgamelog1")
        cursor.execute("drop database xlogin")
        print("delete success")
        cursor.execute("create database xgame1")
        cursor.execute("create database xgamelog1")
        cursor.execute("create database xlogin")
        print("create success")

        path = 'mysql -u root -ptthw123 xgame1 < C:\\Users\\Administrator\\Desktop\\xgame_1886.sql'

        os.system(path)

        cursor.execute("use xgame1")

        changeRole(cursor)

        db.close()

    elif op == '5':

        db = MySQLdb.connect("localhost", "root", "tthw123", "xgame1", charset = "utf8")

        cursor = db.cursor()

        cursor.execute("drop database xgame1")
        cursor.execute("drop database xgamelog1")
        cursor.execute("drop database xlogin")
        print("delete success")
        cursor.execute("create database xgame1")
        cursor.execute("create database xgamelog1")
        cursor.execute("create database xlogin")
        print("create success")

        path = 'mysql -u root -ptthw123 xgame1 < C:\\Users\\Administrator\\Desktop\\BT_3722.sql'

        os.system(path)

        cursor.execute("use xgame1")

        changeRole(cursor)

        db.close()

    else:
        print("your input is not correct")
    
    if op == '1' or op == '2' or op == '3' or op == '4' or op == '5':
         print("load success")

    return

i = 1

while i:
    update_database()
    
    print("==================================")

os.system("pause")