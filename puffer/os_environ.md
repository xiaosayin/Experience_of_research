# 把设置的环境os.environ先设置成常量运行  
a3c.py  line 54   ENTROPY_WEIGHT = float(os.environ['ENTROPY_WEIGHT'])  
multi_agnet.py  nn_model  
已经成功，之前踩坑感觉是因为videos和test_video那个文件夹里面的数据用了puffer给的那个generate.py以及generate_test_video.py产生的数据，不太正常的样子  
解决方法是用原版pensieve的multi_video_sim里面的generate.py以及generate_test_video.py去产生videos和test_video的数据  
然后使用puffer的pensieve那个multi_video_sim文件夹里面的multi_agent_entropy.py可以做到pensieve原文里面提到的熵递减（原版pensieve并没有实现)  
而且能够接着上次训练的模型继续训练  

