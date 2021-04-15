# mahimahi使用固定网络trace建立特定Link
## 安装mahimahi
见官网:  
http://mahimahi.mit.edu/  
$ sudo add-apt-repository ppa:keithw/mahimahi  
$ sudo apt-get update  
$ sudo apt-get install mahimahi  
我在执行第一步的时候报了个什么错  
但是似乎直接执行sudo apt-get install mahimahi就成功了(ubuntu18.04)    
不建议从source build  

## 建立mahimahi链路 
也可以见官网的example部分  
mm-delay 50     这个50的单位是ms  
mm-delay 20 mm-link --meter-all /usr/share/mahimahi/traces/Verizon-LTE-short.up /usr/share/mahimahi/traces/Verizon-LTE-short.down  


## 那么这个链路的工作原理是什么呢
在执行mahimahi的命令之前  
得先执行一个命令  
sudo sysctl -w net.ipv4.ip_forward=1  
然后执行mm-delay mm-link之类的命令  
在mahimahi终端外部，也就是你的本机终端执行  
ifconfig  
这时就会多出一个IP地址:（一般会有一个mtu 1500的标识)  
![Image text](https://github.com/xiaosayin/Experience_of_research/blob/main/img/mahi_local.jpg)  
那个100开头的IP地址  
因为是本机终端打开的，所以我在本机上运行puffer服务器，那么puffer服务器的地址应该是100.64.01  
还有一个destination  100.64.0.2，这个IP地址就是我开启的mahimahi终端容器的IP地址  
如果在mahimahi终端容器里面输入ifconfig  
那么destination会反过来  
如图所示：  
![Image text](https://github.com/xiaosayin/Experience_of_research/blob/main/img/mahi_con.jpg)
然后mahimahi引入的延时或者link就是这个虚拟容器和本机之间的链路  
## 利用mahimahi访问本地的puffer服务器  
调用python的selenium程序访问一个网站  
然后在mahimahi的虚拟容器内运行这个python脚本  
遇到了在本机终端运行python能够正常打开网页，但是mahimahi虚拟容器里面打开却连接不上的问题  
### 第一点，不要开任何代理和vpn
### 第二点检查http_proxy和https_proxy
也就是运行  
RUN $http_proxy  
RUN $https_proxy  
RUN $all_proxy  
如果有任何输出，则需要清空，不然无法正常打开网页  
清空命令：  
RUN  
export http_proxy=  
export https_proxy=  
export all_proxy=  
这样就可以正常访问到puffer了  
而且直接python脚本打开的网页中进行操作，mahimahi的模拟网络环境依然有效！  

# 查看mahimahi进程  
printenv MAHIMAHI_BASE   好像是查看本机在mahimahi下的local IP, 在mahimahi虚拟终端中运行  
以下指令在本机终端运行:  
ps -ef|grep mm-link  
或者  
ps -ef|grep mm-delay  
这个指令是查看mahimahi进程，因为不同的mahimahi进程他的IP地址不一样，所以尽量保证只有一个进程在运行  
一般第一个进程的虚拟IP地址是100.64.0.1 and 100.64.0.2，后面的进程就递增比如说100.64.0.3 and 100.64.0.4  
杀死mahimahi进程就是如下指令:  
pkill mm-delay  
pkill mm-link  


