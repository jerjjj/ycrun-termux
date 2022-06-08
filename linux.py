#coding = utf-8
#auto为自动模式，balance为均衡模式，powersave为卡顿模式，performance为费电模式，fast为性能模式
import os #引入os模块
print("1.切换到自动模式")
print("2.切换到均衡模式")
print("3.切换到卡顿模式")
print("4.切换到费电模式")
print("5.切换到性能模式")
print("6.如果你都不想，你也可以直接启动容器")
a=int(input("请输入序号选择"))
if a<1:#判断用户输入是否超出范围
    exit("请输入正确的序号")
elif a>6:
    exit("请输入正确的序号")
elif a==1:
    os.system('sudo sh /data/adb/modules/uperf/script/powercfg_main.sh auto')#切换到自动模式。
elif a==2:
    os.system('sudo sh /data/adb/modules/uperf/script/powercfg_main.sh balance')#切换到均衡模式
elif a==3:
    os.system('sudo sh /data/adb/modules/uperf/script/powercfg_main.sh powersave')#切换到卡顿模式
elif a==4:
    os.system('sudo sh /data/adb/modules/uperf/script/powercfg_main.sh performance')#切换到费电模式
elif a==5:
    os.system('sudo sh /data/adb/modules/uperf/script/powercfg_main.sh fast')#切换到极速模式
if a!=6:
    b=input("已经成功切换了,按任意键退出")
if a==6:
    os.system('debian')#启动容器并直接退出