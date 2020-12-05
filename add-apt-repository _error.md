在用到 add-apt-repository 时，执行一直报错，报错内容如下：  
Traceback (most recent call last):  
File “/usr/bin/add-apt-repository”, line 10, in  
from softwareproperties.SoftwareProperties import SoftwareProperties, shortcut_handler  
ModuleNotFoundError: No module named ‘softwareproperties’  

解决方法：  
最终发现：原来是因为Python版本不同，Python的模块有些许的不同。  

解决方法：  
打开add-apt-repository文件，将第一行的#!/usr/bin/python3改为#!/usr/bin/python3.5 即可。  

先打开add-apt-repository文件：  
sudo gedit /usr/bin/add-apt-repository  
然后进行修改为#!/usr/bin/python3.5即可。这里取决于刚安装ubuntu时，系统自带的python3是哪个版本就修改哪个版本。  
OK，成功解决softwareproperties模块的问题。  
