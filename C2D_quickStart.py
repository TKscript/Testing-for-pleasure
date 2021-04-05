# -*- coding: utf-8 -*-
import os
# import MySQLdb

def killTask():
    LS = os.system('tasklist | findstr LoginServer.exe')
    GS = os.system('tasklist | findstr GameServer.exe')
    CL_A = os.system('tasklist | findstr agame.exe')
    CL_V = os.system('tasklist | findstr vgame.exe')
    CL_S = os.system('tasklist | findstr sgame.exe')
    CL_X = os.system('tasklist | findstr xgame.exe')

    if LS == 0:
        os.system('taskkill /f /im LoginServer.exe')
    if GS == 0:
        os.system('taskkill /f /im GameServer.exe')
    if CL_A == 0:
        os.system('taskkill /f /im agame.exe')
    if CL_V == 0:
        os.system('taskkill /f /im vgame.exe')
    if CL_S == 0:
        os.system('taskkill /f /im sgame.exe')
    if CL_X == 0:
        os.system('taskkill /f /im xgame.exe')
    return

#防止某些电脑路径报错，全改成双斜杠的路径

def startTask_Agame_1():
    os.system('start /d "G:\\Test_Environment\\Agame\\LoginServer" LoginServer.exe')
    os.system('start /d "G:\\Test_Environment\\Agame\\GameServer" GameServer.exe')
    os.system('start /d "G:\\Test_Environment\\Agame\\Client" agame.exe')
    return

def startTask_Agame_2():
    os.system('start /d "G:\\Test_Environment\\Agame2\\LoginServer" LoginServer.exe')
    os.system('start /d "G:\\Test_Environment\\Agame2\\GameServer" GameServer.exe')
    os.system('start /d "G:\\Test_Environment\\Agame2\\Client" agame.exe')
    return

def startTask_Agame_version():
    os.system('start /d "F:\\Package_tool\\Agame_package\\versions\\1.01.048\\LoginServer" LoginServer.exe')
    os.system('start /d "F:\\Package_tool\\Agame_package\\versions\\1.01.048\\GameServer" GameServer.exe')
    os.system('start /d "F:\\Package_tool\\Agame_package\\versions\\1.01.048\\Client" agame.exe')
    return

def startTask_AgameBT_1():
    os.system('start /d "G:\\Test_Environment\\Agame_BT\\LoginServer" LoginServer.exe')
    os.system('start /d "G:\\Test_Environment\\Agame_BT\\GameServer" GameServer.exe')
    os.system('start /d "G:\\Test_Environment\\Agame_BT\\Client" agame.exe')
    return

def startTask_Vgame_1():
    os.system('start /d "G:\\Test_Environment\\Vgame\\LoginServer" LoginServer.exe')
    os.system('start /d "G:\\Test_Environment\\Vgame\\GameServer" GameServer.exe')
    os.system('start /d "G:\\Test_Environment\\Vgame\\Client" vgame.exe')
    return

def startTask_Xgame_1():
    os.system('start /d "G:\\Test_Environment\\Xgame1\\XLoginServer" LoginServer.exe')
    os.system('start /d "G:\\Test_Environment\\Xgame1\\XGameServer" GameServer.exe')
    os.system('start /d "G:\\Test_Environment\\Xgame1\\XGameClient" xgame.exe')
    return

def startTask_Xgame_2():
    os.system('start /d "G:\\Test_Environment\\Xgame2\\XLoginServer" LoginServer.exe')
    os.system('start /d "G:\\Test_Environment\\Xgame2\\XGameServer" GameServer.exe')
    os.system('start /d "G:\\Test_Environment\\Xgame2\\XGameClient" xgame.exe')
    return

def startTask_XgameBT_1():
    os.system('start /d "G:\\Test_Environment\\Xgame_BT2\\XLoginServer" LoginServer.exe')
    os.system('start /d "G:\\Test_Environment\\Xgame_BT2\\XGameServer" GameServer.exe')
    os.system('start /d "G:\\Test_Environment\\Xgame_BT2\\XGameClient" xgame.exe')
    return

def startTask_Sgame_1():
    os.system('start /d "E:\sgame1\LoginServer" LoginServer.exe')
    os.system('start /d "E:\sgame1\GameServer" GameServer.exe')
    os.system('start /d "E:\sgame1\Client" sgame.exe')
    return

killTask()  #输入前清理一遍进程

print('==============================================')

# i = int(raw_input("please enter the crycle index you want\n"))

i = 1

while i:

    op = raw_input(
    'please choose your environment:\n''\n'
    
    '1.Agame_NO.1\n'
    '2.Agame_NO.2\n'
    '3.Agame_version\n'
    '4.AgameBT_NO.1\n'   
    '==========================\n'
    '5.Vgame_NO.1\n'
    '==========================\n'
    '6.xgame_NO.1\n'
    '7.xgame_NO.2\n'
    '8.xgameBT_NO.1\n'
    '==========================\n'
    '9.Sgame_NO.1\n' '\n')


    killTask()  #启动新环境之前杀掉旧的进程

    # db = MySQLdb.connect("localhost", "root", "tthw123", "qy_login", charset = "utf8")
    # cursor = db.cursor()
    # cursor.execute("drop database qy_login")   #启动新环境之前清空qy_login
    # db.close()

    if op == '1':
        startTask_Agame_1()
    elif op == '2':
        startTask_Agame_2()
    elif op == '3':
        startTask_Agame_version()
    elif op == '4':
        startTask_AgameBT_1()
    elif op == '5':
        startTask_Vgame_1()
    elif op == '6':
        startTask_Xgame_1()
    elif op == '7':
        startTask_Xgame_2()
    elif op == '8':
        startTask_XgameBT_1()
    elif op == '9':
        startTask_Sgame_1()
    else:
        print('the process has been killed')

    print('==============================================')









