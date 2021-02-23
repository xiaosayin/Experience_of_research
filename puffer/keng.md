拉取子模块之前一定要把vpn设置好  
#如何设置git的代理  
$ git config --global https.proxy https://127.0.0.1:8889 
$ git config --global http.proxy http://127.0.0.1:8889 
上面的8889是端口号，对应qv2ray里面的入站设置，https里面的那个端口  
http和https都要设置！  
取消这个git和代理的关联  
$ git config --global --unset http.proxy  
