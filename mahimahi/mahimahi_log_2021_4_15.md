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







printenv MAHIMAHI_BASE  
pkill mm-delay  
pkill mm-link  
export http_proxy=  

