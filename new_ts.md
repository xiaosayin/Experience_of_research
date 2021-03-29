ffmpeg -i jjlin1080.mp4 -bsf:v h264_mp4toannexb -codec copy -hls_list_size 0 -hls_time 96 output.m3u8  
ffmpeg -i seal_team.mkv -vcodec copy -acodec copy -f hls -hls_time 60 output.m3u8
