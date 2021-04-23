# /puffer/src/settings.yml
## bola_basic
```
experiments:  
  - num_servers: 1  
    fingerprint:  
      abr: bola_basic_v1
      cc: bbr
```
## mpc 
```
experiments:  
  - num_servers: 1  
    fingerprint:  
      abr: robust_mpc
      cc: cubic
```

# get rebuf 
```c++
cout << "cum_rebuf: " << client_.cum_rebuffer() << endl; // seconds
  ofstream rebuf;
  rebuf.open("/home/yinwenpei/mahi_python/lenear_bbr_rebuf.log", ios::app); //file.open("flow.txt", std::ios::app);
  rebuf << client_.cum_rebuffer() << endl;
  rebuf.close();
```
