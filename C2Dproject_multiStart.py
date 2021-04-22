# -*- coding: utf-8 -*-

import os
import re

path = {

    'Agame':[
        r'G:\Test_Environment\Agame',
        r'G:\Test_Environment\Agame2',
        r'G:\Test_Environment\Agame_BT',
        r'F:\Package_tool\Agame_package\versions\1.01.049',],

    'Vgame':[
        r'G:\Test_Environment\Vgame',
        r'G:\Test_Environment\Vgame2'],
}

folder = ['\Client','\GameServer']

cl = {
    'Agame':r'\agame.exe',
    'Vgame':r'\vgame.exe',
}

gs = r'\GameServer.exe'

id = {
    'Agame':'serverID = ',
    'Vgame':['serverID = ','dummySvrID = '],
}

class multi_start:

    def __init__(self,path,cl,id):

        self.path = path
        self.cl = cl
        self.id = id

    def game_start(self):
        
        path_cl_root = self.path + folder[0]
        path_cl = path_cl_root + self.cl
        path_gs_root = self.path + folder[1]
        path_gs = path_gs_root + gs

        while True:

            envir = raw_input(
                'please choose your object''\n'
                '1.CL''\n'
                '2.GS''\n'
                '3.press any key to back''\n'
            )

            if envir == '1':
                os.chdir(path_cl_root)
                os.startfile(path_cl)
            elif envir == '2':

                while True:

                     num = raw_input(
                         'please input your serverID''\n'
                         'or input 5 to back''\n'
                     )

                     if num == '5':
                         break
                     elif re.search('[^0-9]',num) != None or num == '':
                         print('not a correct serverID ! ! !')
                         continue
                     else:
                         os.chdir(path_gs_root)
                         
                         try:

                            file = open('gsConfig.lua', 'r')
                            content = file.readlines()
                            file = open('gsConfig.lua', 'w')

                            if len(id) == 1:
                                for line in content:
                                    line = re.sub(r'(serverID = ).*\d','serverID = %s' % num,line)
                                    file.write(line)

                                file.close()
                                os.startfile(path_gs)

                            elif len(id) == 2:
                                for line in content:
                                    line = re.sub(r'(serverID = ).*\d', 'serverID = %s' % num,line)
                                    line = re.sub(r'(dummySvrID = ).*\d', 'dummySvrID = %s' % num,line)
                                    file.write(line)

                                file.close()
                                os.startfile(path_gs)

                         except IOError:

                            print('==========================''\n''there is no such file ! ! !''\n''==========================')
                            break

                         else:
                            print('==========================''\n''write success ~ ~ ~''\n''==========================')

            else:
                break

while True:
    op = raw_input(
        'please select your game''\n'
        '1.AgameNo.1''\n'
        '2.AgameNo.2''\n'
        '3.AgameBT''\n'
        '4.AgameVersion''\n'
        '===============''\n'
        '5.VgameNo.1''\n'
        '6.VgameNo.2''\n'
        '===============''\n'
    )

    if op == '1':
        start = multi_start(path['Agame'][0],cl['Agame'],id['Agame'])
        start.game_start()
    elif op == '2':
        start = multi_start(path['Agame'][1],cl['Agame'],id['Agame'])
        start.game_start()
    elif op == '3':
        start = multi_start(path['Agame'][2],cl['Agame'],id['Agame'])
        start.game_start()
    elif op == '4':
        start = multi_start(path['Agame'][3],cl['Agame'],id['Agame'])
        start.game_start()
    elif op == '5':
        start = multi_start(path['Vgame'][0],cl['Vgame'],id['Vgame'])
        start.game_start()
    elif op == '6':
        start = multi_start(path['Vgame'][1],cl['Vgame'],id['Vgame'])
        start.game_start()
    else:
        print('not a correct game')