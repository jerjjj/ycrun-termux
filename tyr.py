#!/usr/bin/env python
#coding = utf-8
import os
import sys
import termios
with open('/data/data/com.termux/files/usr/etc/profile.d/run.sh','w') as file_read:
    file_read.write('tyr')
def runtype (num:int):#这个函数用来执行切换
    if num == 1:
        sta = os.system('sudo sh /data/adb/modules/uperf/script/powercfg_main.sh auto')
    elif num == 2:
        sta = os.system('sudo sh /data/adb/modules/uperf/script/powercfg_main.sh balance')
    elif num == 3:
        sta = os.system('sudo sh /data/adb/modules/uperf/script/powercfg_main.sh powersave')
    elif num == 4:
        sta = os.system('sudo sh /data/adb/modules/uperf/script/powercfg_main.sh performance')
    elif num == 5:
        sta = os.system('sudo sh /data/adb/modules/uperf/script/powercfg_main.sh fast')
    return sta#sta为状态码
def installer (num:int):#安装tsu和tome linux的函数(1为安装tsu,2为安装tome linux)
    if num == 1:
        os.system("pkg install tsu")
        os.system("tyr")
        exit()
    elif num == 2:
        os.system('bash -c "$(curl -fsSL https://gitee.com/mo2/linux/raw/2/2)"')
        os.system("tyr")
        exit()
    return null
def press_any_key_exit ():
    fd = sys.stdin.fileno()
    old_ttyinfo = termios.tcgetattr(fd)
    new_ttyinfo = old_ttyinfo[:]
    new_ttyinfo[3] &= ~termios.ICANON
    new_ttyinfo[3] &= ~termios.ECHO
    sys.stdout.write("成功切换，按任意键退出……")
    sys.stdout.flush()
    termios.tcsetattr(fd, termios.TCSANOW, new_ttyinfo)
    os.read(fd, 7)
    termios.tcsetattr(fd, termios.TCSANOW, old_ttyinfo)
try:
    userinpf = sys.argv[1]
    userinp = int(userinpf)
except IndexError:
    print("1.切换到自动模式")
    print("2.切换到均衡模式")
    print("3.切换到卡顿模式")
    print("4.切换到费电模式")
    print("5.切换到性能模式")
    print("6.启动tome linux")
    print("7.termux换源")
    print("8.退出")
    userinp = int(input("请输入序号"))
if userinp >=1 | userinp <=5:
    sta = runtype(userinp)
    if sta == 32512:
        chooseinp = int(input("未安装tsu,是否需要安装(1/0)"))
        if chooseinp == 1:
            installer(1)
        if chooseinp == 0:
            os.system("clear")
            os.system("tyr")
            exit()
    elif sta == 0:
        press_any_key_exit()            
elif userinp == 6:
    sta = os.system("debian")
    if sta == 32512:
        chooseinp = int(input("未安装tome linux,是否需要安装(1/0)"))
        if chooseinp == 1:
                installer(2)
        elif chooseinp == 0:
            os.system("clear")
            os.system("tyr")
            exit()
        elif 1 == 1:
            exit("请输入正确的序号")
elif userinp == 7:
    os.system("termux-change-repo")
    os.system("clear")
    os.system("tyr")
elif userinp == 8:
    exit()
elif 1 == 1:
    exit("请输入正确的序号")