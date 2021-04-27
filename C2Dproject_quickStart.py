# -*- coding: utf-8 -*-
import os

program = {
    'Agame':[' LoginServer.exe', ' GameServer.exe', ' agame.exe'],
    'Xgame':[' LoginServer.exe', ' GameServer.exe', ' xgame.exe'],
    'Vgame':[' LoginServer.exe', ' GameServer.exe', ' vgame.exe'],
}

path_root = {

    'Agame':[
        r'G:\Test_Environment\Agame',
        r'G:\Test_Environment\Agame2',
        r'G:\Test_Environment\Agame_BT',
        'F:\\Package_tool\\Agame_package\\versions\\',],

    'Xgame':[
        r'G:\Test_Environment\Xgame1',
        r'G:\Test_Environment\Xgame2',
        r'G:\Test_Environment\Xgame_BT3',
        'F:\\Package_tool\\Xgame_package\\versions\\',],

    'Vgame':[
        r'G:\Test_Environment\Vgame',
        r'G:\Test_Environment\Vgame2',],
}

folder = {
    'Agame':['\LoginServer','\GameServer','\Client'],
    'Xgame':['\XLoginServer','\XGameServer','\XGameClient'],
    'Vgame':['\LoginServer','\GameServer','\Client'],
}


task_start = 'start /d '

path_symbol = '"'

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

class quick_start:
    
    def __init__(self,program,path_root,folder):

        self.program = program
        self.path_root = path_root
        self.folder = folder

    def game_start_normal(self):

        for k in range(len(self.program)):
            path = task_start + path_symbol + self.path_root + self.folder[k] + path_symbol + self.program[k]
            os.system('%s' % path)
        return

    def game_start_version(self):

        version_list = os.listdir(self.path_root)
        num = []
        remove = []
        # 剔除长度不符的元素
        for _ in range(len(version_list)):
            if len(version_list[_]) != 8 and len(version_list[_]) != 7:
                remove.append(version_list[_])
        for _ in remove:
            version_list.remove(_)
        # 获得数字列表
        for version_id in range(len(version_list)):
            num.append(int(version_list[version_id][5:]))
        # 获得元素序列，拿到指定元素
        for version_index in range(len(num)):
            if num[version_index] == max(num):
                version_last = version_list[version_index]
                break
        # 拼接后启动程序
        if version_last:
            for k in range(len(self.program)):
                version_path = task_start + path_symbol + self.path_root + version_last + self.folder[k] + path_symbol + self.program[k]
                os.system('%s' % version_path)
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

            if game_environment == '1':
                start = quick_start(program['Agame'], path_root['Agame'][0],folder['Agame'])
                start.game_start_normal()
            elif game_environment == '2':
                start = quick_start(program['Agame'], path_root['Agame'][1],folder['Agame'])
                start.game_start_normal()
            elif game_environment == '3':
                start = quick_start(program['Agame'], path_root['Agame'][2],folder['Agame'])
                start.game_start_normal()
            elif game_environment == '4':
                start = quick_start(program['Agame'], path_root['Agame'][3],folder['Agame'])
                start.game_start_version()
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

            if game_environment == '1':
                start = quick_start(program['Xgame'], path_root['Xgame'][0],folder['Xgame'])
                start.game_start_normal()
            elif game_environment == '2':
                start = quick_start(program['Xgame'], path_root['Xgame'][1],folder['Xgame'])
                start.game_start_normal()
            elif game_environment == '3':
                start = quick_start(program['Xgame'], path_root['Xgame'][2],folder['Xgame'])
                start.game_start_normal()
            elif game_environment == '4':
                start = quick_start(program['Xgame'], path_root['Xgame'][3],folder['Xgame'])
                start.game_start_version()
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

            if game_environment == '1':
                start = quick_start(program['Vgame'], path_root['Vgame'][0],folder['Vgame'])
                start.game_start_normal()
            elif game_environment == '2':
                start = quick_start(program['Vgame'], path_root['Vgame'][1],folder['Vgame'])
                start.game_start_normal()
            elif game_environment == '3':
                break
            else:
                print('==============================================''\n''the process has been killed')

    else:
        print('==============================================''\n''you made a wrong choice')

    print('==============================================')









