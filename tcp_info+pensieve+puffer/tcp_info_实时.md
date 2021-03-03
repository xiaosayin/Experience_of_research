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
rl_test.py里面，需要更改get_puffer_info函数  
```python
def get_puffer_info(sock):
    json_len = sock.recv(2, socket.MSG_WAITALL)
    try:
        json_len_num = struct.unpack("!H", json_len)[0]
    except Exception:
        print "Failed to decode info from Puffer over IPC"
        sys.exit(1)
    json_data = sock.recv(json_len_num, socket.MSG_WAITALL)
    puffer_info = json.loads(json_data)
    delay = puffer_info['delay'];
    playback_buf = puffer_info['playback_buf'];
    rebuf_time = puffer_info['rebuf_time'];
    last_chunk_size = puffer_info['last_chunk_size'];
    next_chunk_size = puffer_info['next_chunk_sizes'];
    cwnd = puffer_info['cwnd'];
    rtt = puffer_info['rtt']
    
    return delay, playback_buf, rebuf_time, last_chunk_size, next_chunk_size, cwnd, rtt
```
