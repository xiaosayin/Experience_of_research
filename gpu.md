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






 
 
 
