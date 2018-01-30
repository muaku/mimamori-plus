#!/usr/bin/env python
# -✳- coding: utf-8 -✳-

import subprocess
import os
import sys
from time import sleep

if __name__=='__main__':
    while True:
        commandText = u'/root/AquesTalkPi \"こんにちは,初めまして.\" | sox -t wav -c1 - -t wav -c2 /dev/stdout | aplay -Dhw:1,0'
        subprocess.call(commandText, shell=True)
        sleep(2)
        commandText1 = u'/root/AquesTalkPi \"私はフクロウです.\" | sox -t wav -c1 - -t wav -c2 /dev/stdout | aplay -Dhw:1,0'
        subprocess.call(commandText1, shell=True)
        sleep(3)
        commandText2 = u'/root/AquesTalkPi \"今日の温度は25度です.\" | sox -t wav -c1 - -t wav -c2 /dev/stdout | aplay -Dhw:1,0'
        subprocess.call(commandText2, shell=True)
        sleep(3)
        commandText3 = u'/root/AquesTalkPi \"あなたの心拍は64です.\" | sox -t wav -c1 - -t wav -c2 /dev/stdout | aplay -Dhw:1,0'
        subprocess.call(commandText3, shell=True)
        sleep(2)
        commandText4 = u'/root/AquesTalkPi \"呼吸は14です.\" | sox -t wav -c1 - -t wav -c2 /dev/stdout | aplay -Dhw:1,0'
        subprocess.call(commandText4, shell=True)
        sleep(3)
        commandText5 = u'/root/AquesTalkPi \"今日の調子はいいですね.\" | sox -t wav -c1 - -t wav -c2 /dev/stdout | aplay -Dhw:1,0'
        subprocess.call(commandText5, shell=True)
        sleep(30)