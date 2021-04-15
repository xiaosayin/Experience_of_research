# 挂全局代理
export https_proxy=127.0.0.1:8889  #这是qv2ray的代理端口  
# 查看代理  
RUN $http_proxy  
RUN $https_proxy  
RUN $all_proxy  
# 清空代理设置
RUN export http_proxy=  
RUN export https_proxy=  
RUN export all_proxy=  
# 挂github代理  
RUN  git config --global https.proxy https://127.0.0.1:8889  
RUN  git config --global http.proxy https://127.0.0.1:8889  
# 清空github代理  
RUN git config --global --unset http.proxy  
RUN git config --global --unset https.proxy  

# 想要看清楚github的代理是否挂成功，还是得查看这个文件  
~/.gitconfig
