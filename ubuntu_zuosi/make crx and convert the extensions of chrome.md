# 怎么制作插件 以及 把制作好的插件传输给chrome
## 打包扩展程序为crx
### 1.打开chrome的扩展页面，查看扩展程序的ID
![Image text](https://github.com/xiaosayin/Experience_of_research/blob/main/image_store/extensions_id.JPG)  
我电脑的chrome extensions在这里 C:\Users\Yinwenpei\AppData\Local\Google\Chrome\User Data\Default\Extensions  
然后点进去相应的ID  
### 2. 生成crx
打包对应ID文件夹里的，以版本号位名称的文件夹，就在同一目录下生成了crx和pem
## 将扩展程序安装到chrome
将.crx文件后缀改为.zip，解压，然后加载相对应的解压之后的文件即可安装插件

