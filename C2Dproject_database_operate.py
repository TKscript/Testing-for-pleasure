# -*- coding: utf-8 -*-
import os
import MySQLdb

databse_path = {
    'Agame1':r'C:\Users\Administrator\Desktop\qy_33047.sql',
    'Agame2': r'C:\Users\Administrator\Desktop\qy_cn_3_1_12085.sql',
    'Agame_BT':r'C:\Users\Administrator\Desktop\qy_20001_BT.sql',
    'Xgame':r'C:\Users\Administrator\Desktop\xgame_1886.sql',
    'Vgame':r'C:\Users\Administrator\Desktop\tqsy_kr_4_14_30001.sql',
    
}

C2D_database = {
    'Agame1':['qy_00001','qy_log_00001','qy_login'],
    'Agame2':['qy_00002','qy_log_00002','qy_login'],
    'Xgame':['xgame1','xgamelog1','xlogin'],
    'Vgame':['tqsy_00001','tqsy_log_00001','tqsy_login'],
}

CS_name = {
    'Agame':"'qy_01001'",
    'Xgame':"'xgame2'",
    'Vgame':"'tqsy_00002'",
}

CS = {
    'Agame':['qy_01001','qy_log_01001'],
    'Xgame':['xgame2','xgamelog2'],
    'Vgame':['tqsy_00002','tqsy_log_00002'],
}

find_CS = 'select schema_name from information_schema.schemata where schema_name = '
drop = 'drop database '
use = 'use '
create = 'create database '
path_root = 'mysql -u root -p****** '
link_sympol = ' < '

def changeRole(Role):
    Role.execute("SET @userid := 0")

    Role.execute("update role set userid=(@userid:=@userid+1), name= concat('ss', @userid)  ORDER BY role.`totalgrade` desc")  # userid按战力从1开始排序

    # Role.execute("update faction set name=(@userid:=@userid+1) ORDER BY faction.`createtime` desc")

    # Role.execute("update warband set name=(@userid:=@userid+1) ORDER BY warband.`createtime` desc")

    Role.execute("update role set bag = null")  # 清空背包

    Role.execute("delete from role where userid > 30")  # 删除低等级角色

    return

class database_operate:

    def __init__(self,C2D_database,CS_name,CS,key,databse_path):
        
        self.C2D_database = C2D_database
        self.CS_name = CS_name
        self.CS = CS
        self.key = key
        self.databse_path = databse_path

    def deleteCS(self):

        db = MySQLdb.connect("localhost", "root", "******", "%s" % self.C2D_database, charset="utf8")
        cursor = db.cursor()

        if self.C2D_database:
            if cursor.execute(find_CS + self.CS_name) == 1:
                cursor.execute(drop + self.CS[0])
                cursor.execute(drop + self.CS[1])
                db.close()
                print('the database of CS has been clear''\n''=================================')
        else:
            db.close()

        return

    def import_database(self):

        db = MySQLdb.connect("localhost", "root", "******", "%s" % self.C2D_database, charset="utf8")
        cursor = db.cursor()

        for i in self.key:
            command_drop = drop + i
            cursor.execute(command_drop)

        for j in self.key:
            command_creat = create + j
            cursor.execute(command_creat)

        real_path = path_root + self.C2D_database + link_sympol + self.databse_path
        os.system('%s' % real_path)

        cursor.execute(use + self.C2D_database)
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
        operate = database_operate(C2D_database['Agame1'][0],CS_name['Agame'],CS['Agame'],C2D_database['Agame1'],databse_path['Agame1'])
    elif op == '2':
        operate = database_operate(C2D_database['Agame2'][0], CS_name['Agame'], CS['Agame'], C2D_database['Agame2'],databse_path['Agame2'])
    elif op == '3':
        operate = database_operate(C2D_database['Agame1'][0], CS_name['Agame'], CS['Agame'], C2D_database['Agame1'],databse_path['Agame_BT'])
    elif op == '4':
        operate = database_operate(C2D_database['Xgame'][0], CS_name['Xgame'], CS['Xgame'], C2D_database['Xgame'],databse_path['Xgame'])
    elif op == '5':
        operate = database_operate(C2D_database['Vgame'][0], CS_name['Vgame'], CS['Vgame'], C2D_database['Vgame'],databse_path['Vgame'])
    else:
        print("not a correct database ! ! !"'\n''=================================')
        continue

    if operate:
        operate.deleteCS()
        operate.import_database()