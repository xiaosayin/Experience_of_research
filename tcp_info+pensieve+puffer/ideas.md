# 关于train  
puffer+pensieve的train并没有做更改，所以我应该可以直接将tcp_info放在pensieve里面进行train  
# 关于test 
1.puffer/src/abr里面的pensieve.cc就是向rl_test发送delay, video_chunk,等服务器信息的程序，发送实时的tcp_info需要改动这个.cc文件  
2.然后puffer/pensieve/multi_video_sim/rl_test.py也没有做很大改动，做出的决策遵循原版Pensieve，但是改动了原版放一个视频就停止的那一段（直接给删除了，这样服务器可以一直后台使用Pensieve)  
3.先这样  
