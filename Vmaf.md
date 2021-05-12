~/bin/ffmpeg -i 0.mp4 -i /home/yinwenpei/video_encode/leno/working/video_canonicalizer/0.y4m -lavfi libvmaf="model_path=/home/yinwenpei/vmaf-2.1.1/model/vmaf_v0.6.1.json":log_path=/home/yinwenpei/vmaf_logfile.json:log_fmt=json -f null -  
这个命令仅限于两个视频尺寸一样，即长x高一样    

~/bin/ffmpeg -i /home/yinwenpei/video_encode/leno/working/video_canonicalizer/0.y4m -i 0.mp4 -lavfi "[0:v]setpts=PTS-STARTPTS[reference];
            [1:v]scale=1920:1080:flags=bicubic,setpts=PTS-STARTPTS[distorted]; \ 
            [distorted][reference]libvmaf=log_fmt=json:log_path=0.json:model_path=/home/yinwenpei/vmaf-2.1.1/model/vmaf_v0.6.1.json"     -f null -  
这个命令是两个长x高不一样  

