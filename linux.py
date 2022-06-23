#coding = utf-8
#auto为自动模式，balance为均衡模式，powersave为卡顿模式，performance为费电模式，fast为性能模式
import os #引入os模块
print("1.切换到自动模式")
print("2.切换到均衡模式")
print("3.切换到卡顿模式")
print("4.切换到费电模式")
print("5.切换到性能模式")
print("6.启动容器")
print("7.退出")
a=int(input("请输入序号选择"))
if a<1:#判断用户输入是否超出范围
    exit("请输入正确的序号")
elif a>7:
    exit("请输入正确的序号")
elif a==1:
    e = os.system('sudo sh /data/adb/modules/uperf/script/powercfg_main.sh auto')#切换到自动模式。
elif a==2:
    e = os.system('sudo sh /data/adb/modules/uperf/script/powercfg_main.sh balance')#切换到均衡模式
elif a==3:
    e = os.system('sudo sh /data/adb/modules/uperf/script/powercfg_main.sh powersave')#切换到卡顿模式
elif a==4:
    e = os.system('sudo sh /data/adb/modules/uperf/script/powercfg_main.sh performance')#切换到费电模式
elif a==5:
    e = os.system('sudo sh /data/adb/modules/uperf/script/powercfg_main.sh fast')#切换到极速模式
elif a==7:
    exit()
if a != 6:
    if e == 32512:#如果报错
        g = int(input("检测到你未安装tsu,是否需要安装(1/0)"))#尝试安装tsu
        if g == 1:
            os.system('pkg install tsu')#安装tsu
            exit()
        elif g == 0:
            exit()
        elif g != 1:#序号错误
            exit("请输入正确的序号")
        elif g != 0:
            exit("请输入正确的序号")
if a!=6:
    b=input("已经成功切换了,按任意键退出")
if a==6:
    c = os.system('debian')#尝试启动容器
    if c == 0:#启动成功退出脚本
        exit()
    elif c ==32512:#启动失败
        d = int(input("检测到你未安装容器,是否要安装(1/0)"))#是否需要安装tome
        if d == 1:#如果需要,执行安装命令
            os.system('bash -c "$(curl -fsSL https://gitee.com/mo2/linux/raw/2/2)"')
        elif d == 0:#如果不需要退出脚本
            exit()
        elif d != 1:#序号输入错误的处理方式
            exit("请输入正确的序号")
        elif d != 0:
            exit("请输入正确的序号")
