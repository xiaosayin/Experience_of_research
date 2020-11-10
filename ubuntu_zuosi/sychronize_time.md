# 更新ubuntu的系统时间  
sudo apt-get update  
sudo apt-get install ntpdate  
sudo ntpdate time.windows.com  
# 将时间更新到硬件上  
sudo hwclock --localtime --systohc
