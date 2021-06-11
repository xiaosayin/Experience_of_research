
1.打开终端，输入 cd /etc/default/  

2.接着输入sudo gedit /etc/default/grub  ，会提示输入密码，输入密码按回车即可  

3.现在进入了grub文件，找到GRUB_DEFAULT = 0，因为Ubuntu的顺序是从0开始的，并且windows对应第3个选项，所以将0改为2，  

5.按Ctrl+X，会有一个询问是否保存，输入Y保存修改后的grub文件，会有再次询问时，按回车确认退出  

6.输入 sudo update-grub更新grub文件  

至此设置完毕，然后重启系统，就可以看到默认是windows系统为第一启动项了，不用手动选择，就可以自动进入windows了。  
 
