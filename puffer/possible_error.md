# Web server and media server  
第1步，最后一句，generate a random string to be used as the web server key.尚未执行，也没搞懂该怎么生成一个随机的string.  
  
  
CREATE USER puffer WITH PASSWORD 'jj';   # 记录一下我设置的密码，暂且不清楚输入的时候有没有两个引号''  
  
# 记录在~/.bashrc    
export PUFFER_PORTAL_SECRET_KEY='yinwenpeiServer'  
export PUFFER_PORTAL_DB_KEY='jj'  
  
# 直接用这句话就可以启动web server， 浏览器输入127.0.0.1:8080可以验证是否成功,在目录puffer底下    
  ./src/portal/manage.py runserver 0:8080  
   
   
# 第8部分，这句话没怎么看懂 
where enforce_moving_live_edge allows for testing pre-recorded video (instead of live streaming), and the bitrate ladder of each channel must match what is pre-encoded in the media archive.  
  
# puffer  WEB端的用户：    
qianlike  
qianqianzi   
  
# 解决AttributeError: module 'argon2' has no attribute 'low_level'  的问题    
solved installing argon2_cffi, I will close the issue, thank you  

# 直接启动media server， 在目录puffer底下  
cd src/
RUN  ./media-server/run_servers settings.yml  
  

# 这个influxdb是用来记录data的  
[optional] start InfluxDB automatically after reboots  
sudo systemctl enable influxdb  

# influx的用户和密码  
CREATE USER puffer WITH PASSWORD 'jj' WITH ALL PRIVILEGE  

# 配置influx时，将influx password设置成环境变量  
If everything looks good, save the InfluxDB password in an environment variable INFLUXDB_PASSWORD.  
For instance, you may append one line to ~/.bashrc  
export INFLUXDB_PASSWORD='jj'  

then  source ~/.bashrc  

# 启动influx  
sudo systemctl start influxdb  #启动  
sudo systemctl restart influxdb #重启  




 
