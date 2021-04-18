# -*- coding: utf-8 -*-
import os
import re
# import MySQLdb

#配置项如下
path_agame = [
    r'G:\Test_Environment\Agame',
    r'G:\Test_Environment\Agame2',
    r'G:\Test_Environment\Agame_BT',
    'F:\\Package_tool\\Agame_package\\versions\\',
]

path_xgame = [
    r'G:\Test_Environment\Xgame1',
    r'G:\Test_Environment\Xgame2',
    r'G:\Test_Environment\Xgame_BT3',
    'F:\\Package_tool\\Xgame_package\\versions\\',
]

path_vgame = [
    r'G:\Test_Environment\Vgame',
    r'G:\Test_Environment\Vgame2',
]


#下面的不用改
def killTask():

    task_List = ['LoginServer.exe','GameServer.exe','agame.exe','vgame.exe','sgame.exe','xgame.exe']
    find_Commond = 'tasklist | findstr '
    kill_Command = 'taskkill /f /im '

    for i in range(len(task_List)):
        task_Find = find_Commond + task_List[i]
        if os.system('%s' % task_Find) == 0:
            task_Kill = kill_Command + task_List[i]
            os.system('%s' % task_Kill)
    return

task_start = 'start /d '
folder_agame_vgame_sgame = ['\LoginServer','\GameServer','\Client']
folder_xgame = ['\XLoginServer','\XGameServer','\XGameClient']
path_symbol = '"'

program_agame = [' LoginServer.exe', ' GameServer.exe', ' agame.exe']
program_vgame = [' LoginServer.exe', ' GameServer.exe', ' vgame.exe']
program_xgame = [' LoginServer.exe', ' GameServer.exe', ' xgame.exe']
program_sgame = [' LoginServer.exe', ' GameServer.exe', ' sgame.exe']

def Agame_Xgame_Start(gameNumber,program,path_root,folder):

    gameNumber = int(gameNumber)
    if gameNumber == 1 or gameNumber == 2 or gameNumber == 3:
        for k in range(len(program)):
            path = task_start + path_symbol + path_root[gameNumber-1] + folder[k] + path_symbol + program[k]
            os.system('%s' % path)
    elif gameNumber == 4:
        version_list = os.listdir(path_root[gameNumber-1])
        num = []
        remove = []
        #剔除长度不符的元素
        for _ in range(len(version_list)):
            if len(version_list[_]) != 8 and len(version_list[_]) != 7:
                remove.append(version_list[_])
        for _ in remove:
            version_list.remove(_)
        #获得数字列表
        for version_id in range(len(version_list)):
            num.append(int(version_list[version_id][5:]))
        #获得元素序列，拿到指定元素
        for version_index in range(len(num)):
            if num[version_index] == max(num):
                version_last = version_list[version_index]
                break
        #拼接后启动程序
        if version_last:
            for k in range(len(program)):
                version_path = task_start + path_symbol + path_root[gameNumber - 1] + version_last + folder[k] + path_symbol + program[k]
                os.system('%s' % version_path)
    else:
        print('you made a wrong choice')

    return

def Vgame_Start(gameNumber):

    gameNumber = int(gameNumber)
    if gameNumber == 1 or gameNumber == 2:
        for k in range(len(program_xgame)):
            path = task_start + path_symbol + path_vgame[gameNumber-1] + folder_agame_vgame_sgame[k] + path_symbol + program_vgame[k]
            os.system('%s' % path)
    else:
        print('you made a wrong choice')

    return



while True:
    killTask()  # 启动新环境之前杀掉旧的进程
    game = raw_input(
        'please choose your game:\n''\n' 
        '1.Agame\n''\n'
        '2.Xgame\n''\n'
        '3.Vgame\n''\n'
        '====================\n')

    if game == '1':
        while True:
            game_environment = raw_input(
                'please choose your game environment:\n''\n'
                '1.No.1\n''\n'
                '2.No.2\n''\n'
                '3.BT\n''\n'
                '4.Version\n''\n'
                '5.back\n''\n'
                '====================\n'
            )
            killTask()  # 启动新环境之前杀掉旧的进程
            if game_environment == '1' or game_environment == '2' or game_environment == '3' or game_environment == '4':
                Agame_Xgame_Start(game_environment,program_agame,path_agame,folder_agame_vgame_sgame)
            elif game_environment == '5':
                break
            else:
                print('==============================================''\n''the process has been killed')

    elif game == '2':
        while True:
            game_environment = raw_input(
                'please choose your game environment:\n''\n'
                '1.No.1\n''\n'
                '2.No.2\n''\n'
                '3.BT\n''\n'
                '4.Version\n''\n'
                '5.back\n''\n'
                '====================\n'
            )
            killTask()  # 启动新环境之前杀掉旧的进程
            if game_environment == '1' or game_environment == '2' or game_environment == '3' or game_environment == '4':
                Agame_Xgame_Start(game_environment,program_xgame,path_xgame,folder_xgame)
            elif game_environment == '5':
                break
            else:
                print('==============================================''\n''the process has been killed')

    elif game == '3':
        while True:
            game_environment = raw_input(
                'please choose your game environment:\n''\n'
                '1.No.1\n''\n'
                '2.No.2\n''\n'
                '3.back\n''\n'
                '====================\n'
            )
            killTask()  # 启动新环境之前杀掉旧的进程
            if game_environment == '1' or game_environment == '2':
                Vgame_Start(game_environment)
            elif game_environment == '3':
                break
            else:
                print('==============================================''\n''the process has been killed')

    else:
        print('==============================================''\n''you made a wrong choice')

    print('==============================================')









