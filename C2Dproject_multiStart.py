# -*- coding: utf-8 -*-

import os
import re

path_agame = [
    r'G:\Test_Environment\Agame',
    r'G:\Test_Environment\Agame2',
    r'G:\Test_Environment\Agame_BT',
    r'F:\Package_tool\Agame_package\versions\1.01.049'
]

folder = ['\GameServer','\Client']

CL = r'\agame.exe'
GS = r'\GameServer.exe'

def Strat_Game(op):
    if op == '1' or op == '2' or op == '3' or op == '4':
        op = int(op) - 1
        path_CL_root = path_agame[op] + folder[1]
        path_CL = path_CL_root + CL
        path_GS_root = path_agame[op] + folder[0]
        path_GS = path_GS_root + GS
        while True:
            envir = raw_input(
                'please choose your object''\n'
                '1.CL''\n'
                '2.GS''\n'
                '3.back''\n'
            )
            if envir == '1':
                os.chdir(path_CL_root)
                os.startfile(path_CL)
            elif envir == '2':
                while True:
                     num = raw_input(
                         'please input your serverID''\n'
                         'or input 5 for back''\n'
                     )
                     if num == '5':
                         break
                     elif re.search('[^0-9]',num) != None or num == '':
                         print('not a correct serverID ! ! !')
                         continue
                     else:
                         os.chdir(path_GS_root)
                         file = open('gsConfig.lua', 'r')
                         content = file.readlines()
                         file = open('gsConfig.lua', 'w')
                         for line in content:
                             new_line = re.sub(r'(serverID = ).*\d', 'serverID = %s' % num, line)
                             file.write(new_line)
                         file.close()
                         os.startfile(path_GS)
            elif envir == '3':
                break
            else:
                print('you made a wrong choice')
    else:
        print('not a correct game')

while True:
    op = raw_input(
        'please select your game''\n'
        '1.AgameNo.1''\n'
        '2.AgameNo.2''\n'
        '3.AgameBT''\n'
        '4.AgameVersion''\n'
        '===============''\n'
    )
    Strat_Game(op)