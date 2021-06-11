# 更新ubuntu的系统时间  
sudo apt-get update  
sudo apt-get install ntpdate  
sudo ntpdate time.windows.com  
# 将时间更新到硬件上  
sudo hwclock --localtime --systohc

# 第二种方法
ubuntu18.04+win10解决办法：  
安装ntpdate：  

执行命令：# sudo apt-get install ntpdate  
设置校正服务器：  

执行命令：# sudo ntpdate time.windows.com  
设置硬件时间为本地时间：  

执行命令：# sudo hwclock --localtime --systohc  
执行命令：# reboot  
