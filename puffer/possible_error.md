Web server and media server  
第1步，最后一句，generate a random string to be used as the web server key.尚未执行，也没搞懂该怎么生成一个随机的string.  
  
CREATE USER puffer WITH PASSWORD 'jj';   # 记录一下我设置的密码，暂且不清楚输入的时候有没有两个引号''  
  
记录在~/.bashrc    
export PUFFER_PORTAL_SECRET_KEY='yinwenpeiServer'  
export PUFFER_PORTAL_DB_KEY='jj'  

