# -*- coding: utf-8 -*-
import os
import MySQLdb

#配置项
databse_path = [
    r'C:\Users\Administrator\Desktop\qy_cn_changeTime3_8_12064.sql',
    r'C:\Users\Administrator\Desktop\qy_cn_3_1_12085.sql',
    r'C:\Users\Administrator\Desktop\qy_20001_BT.sql',
    r'C:\Users\Administrator\Desktop\xgame_1886.sql',
]

#下面的不用管
databse_agame_1 = ['qy_00001','qy_log_00001','qy_login']
databse_agame_2 = ['qy_00002','qy_log_00002','qy_login']
databse_xgame = ['xgame1','xgamelog1','xlogin']
CS_insert = ["'qy_01001'","'qy_log_01001'","'xgame2'","'xgamelog2'"]
CS = ['qy_01001','qy_log_01001','xgame2','xgamelog2']
find_CS = 'select schema_name from information_schema.schemata where schema_name = '
drop = 'drop database '
create = 'create database '
use = 'use '
path_root = 'mysql -u root -ptthw123 '
link_sympol = ' < '


def changeRole(Role):
    Role.execute("SET @userid := 0")

    Role.execute(
        "update role set userid=(@userid:=@userid+1), name= concat('ss', @userid)  ORDER BY role.`totalgrade` desc")  # userid按战力从1开始排序

    # Role.execute("update faction set name=(@userid:=@userid+1) ORDER BY faction.`createtime` desc")

    # Role.execute("update warband set name=(@userid:=@userid+1) ORDER BY warband.`createtime` desc")

    Role.execute("update role set bag = null")  # 清空背包

    Role.execute("delete from role where userid > 30")  # 删除低等级角色

    return

def deleteCS(databse_game):
    db = MySQLdb.connect("localhost", "root", "tthw123", "%s" % databse_game[0], charset="utf8")
    cursor = db.cursor()
    if databse_game[0] == 'qy_00001':
        if cursor.execute(find_CS + CS_insert[0]) == 1:
            cursor.execute(drop + CS[0])
            cursor.execute(drop + CS[1])
            db.close()
            print('the database of CS has been clear''\n''=================================')
    elif databse_game[0] == 'xgame1':
        if cursor.execute(find_CS + CS_insert[2]) == 1:
            cursor.execute(drop + CS[2])
            cursor.execute(drop + CS[3])
            db.close()
            print('the database of CS has been clear''\n''=================================')
    else:
        db.close()
        return

def Import_Database(databse_game,databse_path_index):

    db = MySQLdb.connect("localhost", "root", "tthw123", "%s" % databse_game[0], charset = "utf8")
    cursor = db.cursor()
    for i in databse_game:
        command_drop = drop + i
        cursor.execute(command_drop)
    for j in databse_game:
        command_creat = create + j
        cursor.execute(command_creat)
    real_path = path_root + databse_game[0] + link_sympol + databse_path[databse_path_index]
    os.system('%s' % real_path)
    cursor.execute(use + databse_game[0])
    changeRole(cursor)
    db.close()
    print('the database has been imported''\n''=================================')

    return

while True:

    op = raw_input(
        'please select your database''\n'
        '==================================''\n'
        '1.Agame1''\n'
        '2.Agame2''\n'
        '3.AgameBT''\n'
        '==================================''\n'
        '4.Xgame1''\n'
        '==================================''\n'
        '5.Vgame1''\n''\n'
        )

    if op == '1':
        deleteCS(databse_agame_1)
        Import_Database(databse_agame_1,0)
    elif op == '2':
        Import_Database(databse_agame_2,1)
    elif op == '3':
        deleteCS(databse_agame_1)
        Import_Database(databse_agame_1,2)
    elif op == '4':
        deleteCS(databse_xgame)
        Import_Database(databse_xgame,3)

    else:
        print("not a correct database ! ! !"'\n''=================================')