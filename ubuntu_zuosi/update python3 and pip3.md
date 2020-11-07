# 升级python3
$ sudo apt uodate   # 更新源  
2.安装依赖库

$ sudo apt-get install zlib1g-dev libbz2-dev libssl-dev libncurses5-dev libsqlite3-dev libreadline-dev tk-dev libgdbm-dev libdb-dev libpcap-dev xz-utils libexpat1-dev liblzma-dev libffi-dev libc6-dev
$ wget 'https://www.python.org/ftp/python/3.8.2/Python-3.8.2.tgz'
$tar zxvf Python-3.8.2.tgz #解压
$cd Python-3.8.2
$sudo mkdir -p /usr/local/python3 #建立安装目录

##编译安装
#后面加上 --enable-optimizations 会自动安装pip3及优化配置, prefix也可以不要
$./configure --prefix=/usr/local/python3  --enable-optimizations
$make
$sudo make install

4. 删除软连接 pip 比较特殊
$ sudo rm -rf /usr/bin/python3
$ sudo rm -rf /usr/bin/pip3

5. 接上新的软连接
#添加python3的软链接
sudo ln -s /usr/local/python3/bin/python3.8 /usr/bin/python3
#添加 pip3 的软链接 这一步似乎没用上，因为装的时候没把Pip一起装下来   可以用which pip3查找位置，如果不在 /usr/bin/pip3，其他地方也没有，那么就要手动装pip
sudo ln -s /usr/local/python3/bin/pip3.8 /usr/bin/pip3

! 安装对应的python3.8 的pip，不然pip3无法对应到相应的python3.8

setuptools官网下载源码：https://pypi.org/project/setuptools/#files
pip官网下载源码：https://pypi.org/project/pip/#files

②因为我要把 pip 和 python3.8 关联在一起，所以运行 setup.py 都是用python3.8来运行的。
③安装的这个pip是包含pip和pip3的，pip是用来安装第三方模块的。

1.安装pip之前，需要安装setuptools
sudo unzip setuptools-40.6.2.zip
cd setuptools-40.6.2
sudo python3.7 setup.py build
sudo python3.7 setup.py install
2、安装pip
sudo tar -zxvf pip-18.1.tar.gz
cd pip-18.1
sudo python3.7 setup.py build
sudo python3.7 setup.py install

问题到这里并没有结束，
pip3 install numpy --user    #--user很重要！
然后出现了一个叫做什么  release.py 什么module的问题,这个问题和pip无关
于是最关键的一步:
$ sudo mv /usr/bin/lsb_release /usr/bin/lsb_release_back
lsb_release 我里面还改了一点东西，不知道有没有用，但是记录一下
就是把第一句话那个什么 #user .......(此处不记得了) python3改成了python2.7，并没有起作用，似乎把这个东西换个位置就好了
然后就好了
