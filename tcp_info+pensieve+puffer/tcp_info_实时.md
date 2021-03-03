# 获取tcp_info到pensieve的rl_test.py  
最重要的是pensieve.cc文件，c++文件每次更改完需要重新编译(make)才能生效！  
在puffer目录下  
make -j CXXFLAGS='-DNONSECURE'  
然后pensieve.cc里面  
```c++
  json j;
  j["delay"] = trans_time; // ms
  j["playback_buf"] = client_.video_playback_buf(); // seconds
  j["rebuf_time"] = client_.cum_rebuffer(); // seconds
  j["last_chunk_size"] = (double)size; // bytes
  //j["last_chunk_size"] = (double) 1;
  j["next_chunk_sizes"] = next_chunk_sizes; // bytes
  j["cwnd"] = client_.tcp_info().value().cwnd;
``` 
