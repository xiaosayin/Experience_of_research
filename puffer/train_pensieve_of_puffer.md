https://groups.google.com/g/puffer-stanford/c/I2gD2n818EY  
修改 multi_video_sim里面的env里面的参数，以匹配puffer  
puffer论文里面3.3节提到了要把video chunk lenghth 改成2.002 seconds 以及 buffer thresh hold = 15 seconds  
VIDEO_CHUNCK_LEN = 2000.0  # millisec  
BUFFER_THRESH = 17.0 * MILLISECONDS_IN_SECOND  

# multi_video_sim成功运行，可以放在puffer上运行  
先运行generate_video.py，在同一目录下创建videos文件夹，以及在videos文件夹下创建一个空文件0即可运行  

