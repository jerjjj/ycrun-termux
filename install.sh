#！/bin/sh
cp -p linux.py /data/data/com.termux/files/home/
cp -p run.sh /data/data/com.termux/files/usr/etc/profile.d/
if [ $? -eq 0 ];then
  rm -rf linux.py
  rm -rf run.sh
  rm -rf install.sh
else
  echo 安装失败，请手动安装
fi