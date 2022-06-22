#！/bin/sh
python3 linux.py
if [ $? -eq 127 ];then
  read -p "检测到未安装python,是否要安装(1/0)" NUM1
  if [ $NUM1 == 1 ];then
    apt install python3
  elif [ $NUM1 == 0 ];then
    exit
  elif [ $NUM1 != 1 ];then
    echo 请输入正确的序号
  elif [ $NUM1 != 0 ];then
    echo 请输入正确的序号
  fi
fi