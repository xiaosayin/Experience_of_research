# ZeroTier官网注册/登陆账号
这个就按照流程做就行了  
# Create A Network
点击创建一个新的网络，有一个network ID  
你要加入的设备都需要这个network ID  
# 客户端client
两台设备互相能够访问都需要添加ZeroTier的客户端  
https://www.zerotier.com/download/  
windows可以直接下载一个类似于app的  
然后添加那个network Id就行  
然后需要在那个create网络的页面勾选那个添加进来的设备  
![Image text](https://github.com/xiaosayin/Experience_of_research/blob/main/img/Zerotier_0.jpg)
# ubuntu18.04 Zerotier客户端配置
RUN  
curl -s https://install.zerotier.com | sudo bash  
RUN  
sudo zerotier-cli join 你的network ID  
显示join 200 OK就是成功了  
然后勾选那一栏里面的Managed IPs就是可以直接访问的  
# 彻底删除Zerotier 
## 1.通过dpkg删除zerotier-one服务
sudo dpkg -P zerotier-one
## 2.删除zerotier-one文件夹，该文件夹存储了address地址，删除后再次安装会获得新的address地址
sudo rm -rf /var/lib/zerotier-one/
