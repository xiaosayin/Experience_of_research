 这里以 tensorflow_gpu==1.14.0为例  
 lspci | grep -i vga  查看显卡型号    
 gcc -v  查看gcc版本  
 记得顺序，  
 先装驱动，装好之后重启  
 再装cuda  
 再装cudnn  
 再装tensorflow_gpu  
 # 驱动和cuda版本的对应：  
 官网：https://docs.nvidia.com/cuda/cuda-toolkit-release-notes/index.html  
 ![Image text](https://github.com/xiaosayin/Experience_of_research/blob/main/img/sendpix1.jpg)  
 # cuda的版本和cudnn的版本参照下图：  
 https://www.tensorflow.org/install/source#gpu  
 该图片是tensorflow官方linux下的成功配置    
 ![Image text](https://github.com/xiaosayin/Experience_of_research/blob/main/img/sendpix0.jpg)  
 这次成功的选择是 nvidia_driver_version_460 + cuda 10.0 + cudnn 7.4.2  
 
 # 装驱动的几种方法
 ## 1. ppa装（这个方法装驱动确实成功了，但是装好cuda和cudnn之后，这个驱动却离奇失踪了)  
 sudo add-apt-repository ppa:graphics-drivers/ppa  ppa包管理  
 sudo apt update  
 ubuntu-drivers devices  查看驱动
 sudo ubuntu-drivers autoinstall  自动装推荐  
 ## 2. 图形界面直接装(在装好cuda和cudnn之后，通过这个方法重新装驱动，成功了)  
 因为CUDA 选择了CUDA 10.0版本，所以这里我选择的是：nvidia-driver-440:  
1、打开 “SoftWare & updates”  
2、打开" Additional Drivers"  
3、选择 “nvidia-driver-450” #这里我选择的440版本  
注：选择安装后记得重启  
![Image text](https://github.com/xiaosayin/Experience_of_research/blob/main/img/nvidia_driver_gnome.png)  

# cuda的安装   
官网： https://developer.nvidia.com/cuda-toolkit-archive  
安装之前仔细阅读online documentation/ installation Guide Linux  
进入安装界面：https://developer.nvidia.com/cuda-10.0-download-archive?target_os=Linux&target_arch=x86_64&target_distro=Ubuntu&target_version=1804&target_type=deblocal  
installer type: deb(local)  
![Image text](https://github.com/xiaosayin/Experience_of_research/blob/main/img/sendpix2.jpg)  
先点击下载右上角那个1.6G的deb文件  

```
sudo dpkg -i cuda-repo-ubuntu1804-10-0-local-10.0.130-410.48_1.0-1_amd64.deb
sudo apt-key add /var/cuda-repo-<version>/7fa2af80.pub
sudo apt-get update
sudo apt-get install cuda
最好指定安装的cuda版本
如：
sudo apt-get install cuda-10-0	
sudo apt-get install cuda-10-2
```
安装之后，输入如下指令：  
RUN cat /usr/local/cuda/version.txt  
出现以下内容说明安装成功：  
CUDA Version 10.0.130  
## cuda的卸载（没实验过）  
```
sudo apt remove cudnn*
sudo apt-get remove cuda*
sudo apt-get autoclean

cd /usr/local/
sudo rm -r cuda-10.2
```

# 安装cudnn  
官网: https://developer.nvidia.com/rdp/cudnn-archive  
https://docs.nvidia.com/deeplearning/cudnn/archives/index.html  documentaion including cudnn installation Guide  
![Image text](https://github.com/xiaosayin/Experience_of_research/blob/main/img/sendpix3.jpg)  
点击 Runtime,  Developer library , code Samples  
下载这三个deb文件,用dpkg安装    
```
sudo dpkg -i libcudnn7_7.6.4.38-1+cuda10.0_amd64.deb
sudo dpkg -i libcudnn7-dev_7.6.4.38-1+cuda10.0_amd64.deb
sudo dpkg -i libcudnn7-doc_7.6.4.38-1+cuda10.0_amd64.deb
```
测试安装  
cat /usr/include/x86_64-linux-gnu/cudnn_v7.h | grep CUDNN_MAJOR -A 2  
输出如下说明安装成功:  
```
#define CUDNN_MAJOR 7
#define CUDNN_MINOR 6
#define CUDNN_PATCHLEVEL 4
--
#define CUDNN_VERSION (CUDNN_MAJOR * 1000 + CUDNN_MINOR * 100 + CUDNN_PATCHLEVEL)

#include "driver_types.h"
```  
# 测试tensorflow的可用gpu  
``` python3
import tensorflow as tf
print(tf.__version__)
#输出'2.0.0'
print(tf.test.is_gpu_available())
#会输出True,则证明安装成功
```










 
 
 
