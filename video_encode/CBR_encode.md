~/bin/ffmpeg -y -i jjlin1080.mp4 -c:v libx264 -b:v 1200k -pass 1 -f mp4 NUL && ~/bin/ffmpeg -i jjlin1080.mp4 -vf "scale=1280:-1" -c:v libx264 -b:v 1200k -maxrate 1200k -bufsize 500k -pass 2 test_720_CBR_1200k.mp4  
实现CBR码控，同时解决scale的问题  
-vf "scale=1280:-1"  这是调整大小  



