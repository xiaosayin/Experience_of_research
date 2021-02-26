# how to add pensieve on the puffer
puffer/src/settings.yml 配置  
experiments:  
  - num_servers: 1  
    fingerprint:  
      abr: pensieve  
      abr_config:  
        nn_path: /home/yinwenpei/puffer/third_party/pensieve/model/nn_model_ep_77400.ckpt  
        pensieve_path: /home/yinwenpei/puffer/third_party/pensieve/multi_video_sim/rl_test.py  
      cc: cubic  
enable_logging: true  

# 其他abr算法实验的配置
https://puffer.stanford.edu/data-description/  
下载这个页面里面的fake data  
该文件夹中有 logs/expt_settings记录了每一个实验的settings.yml的配置  
expt_settings里面的git_commit不用放在settings.yml里面  

# 新abr算法的配置  
work on progress  
参考documetion里面的说明  
